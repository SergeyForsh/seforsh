import sqlite3
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
import pandas as pd

# Инициализация бота
API_TOKEN = "ВАШ_ТОКЕН_БОТА"  # Укажите токен бота
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Создаем подключение к базе данных
conn = sqlite3.connect("survey_results.db")
cursor = conn.cursor()

# Создаем таблицу для хранения данных
cursor.execute('''
CREATE TABLE IF NOT EXISTS survey (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    question TEXT NOT NULL,
    answer TEXT NOT NULL
)
''')
conn.commit()

# Вопросы для опроса
questions = [
    "Как вас зовут?",
    "Сколько вам лет?",
    "Какой у вас уровень удовлетворенности жизнью (от 1 до 10)?"
]
user_answers = {}  # Временное хранилище ответов пользователей


# Команда /start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user_answers[message.from_user.id] = []  # Инициализируем список ответов
    await message.answer("Добро пожаловать в опросник! Начнем опрос. Вот первый вопрос:")
    await ask_question(message.from_user.id, 0)


# Задаем вопрос
async def ask_question(user_id, question_index):
    if question_index < len(questions):
        question = questions[question_index]
        await bot.send_message(user_id, question)
    else:
        await bot.send_message(user_id, "Спасибо за участие в опросе!")
        save_results(user_id)
        del user_answers[user_id]  # Удаляем временные данные


# Сохраняем результаты в базу данных
def save_results(user_id):
    answers = user_answers[user_id]
    for question, answer in zip(questions, answers):
        cursor.execute("INSERT INTO survey (user_id, question, answer) VALUES (?, ?, ?)",
                       (user_id, question, answer))
    conn.commit()


# Обрабатываем ответы на вопросы
@dp.message_handler()
async def handle_answers(message: types.Message):
    user_id = message.from_user.id
    if user_id in user_answers:
        user_answers[user_id].append(message.text)
        question_index = len(user_answers[user_id])
        await ask_question(user_id, question_index)
    else:
        await message.answer("Начните с команды /start для участия в опросе.")


# Команда /results для экспорта данных
@dp.message_handler(commands=['results'])
async def export_results(message: types.Message):
    df = pd.read_sql("SELECT * FROM survey", conn)
    if df.empty:
        await message.answer("Результатов пока нет.")
    else:
        # Сохраняем результаты в Excel
        df.to_excel("survey_results.xlsx", index=False)
        with open("survey_results.xlsx", "rb") as file:
            await message.answer_document(file, caption="Результаты опроса")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
