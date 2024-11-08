# рассылка писем
def send_email(message, recipient,sender = "university.help@gmail.com"):
    if (("@" and (".com" or ".ru" or ".net")) not in (recipient or sender) or ("@" or (".com" or ".ru" or ".net"))
            not in (recipient or sender)):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    elif sender != "university.help@gmail.com":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

send_email('messagje','university.help@gmail.com','@.com')
send_email('messagje','university.help@gmail.com')
send_email('messagje','universi@.com')
send_email('messagje','universi@.co')
send_email('messagje','universi.com')

print()
import re
def is_valid_email(email):
    # Простой регулярное выражение для проверки валидности email
    return re.match(r"[^@]+@[^@]+\.[a-zA-Z]{2,}", email) is not None

def send_email(message, recipient, sender="university.help@gmail.com"):
    if not is_valid_email(recipient) or not is_valid_email(sender):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}: некорректный адрес.")
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    else:
        if sender == "university.help@gmail.com":
            print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
        else:
            print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

# Примеры вызовов функции
send_email('message', 'university.help@gmail.com', '@.com')
send_email('message', 'university.help@gmail.com')
send_email('message', 'university@.com')
send_email('message', 'university@.com')
send_email('message', 'university@.com')

### Объяснение изменений:
# - Добавлена функция `is_valid_email`, использующая регулярное выражение для проверки,
#   что адрес электронной почты корректен.
# - Упрощены условия для проверки валидности адресов.
# - Проверка на совпадение отправителя и получателя вынесена в начало, что позволяет избежать лишних проверок.
print()
import re
def is_valid_email(email):
    # Проверяем, что email содержит символ '@' и заканчивается на '.com', '.ru' или '.net'
    return re.match(r"^[^@]+@[^@]+\.(com|ru|net)$", email) is not None
def send_email(message, recipient, *, sender="university.help@gmail.com"):
    # Проверка на корректность email отправителя и получателя
    if not is_valid_email(recipient) or not is_valid_email(sender):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    # Проверка на отправку самому себе
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    # Проверка на отправителя по умолчанию
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
# Примеры вызовов функции
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!',
           'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

### Объяснение кода:
#1. **Функция `is_valid_email`**: Определяет, является ли email корректным, проверяя наличие `@`
#     и соответствие доменному окончанию с помощью регулярного выражения.
#2. **Функция `send_email`**:
#  - Проверяет корректность email-адресов.
#  - Если адреса некорректные, выводит сообщение о невозможности отправки.
#  - Проверяет, не пытается ли пользователь отправить письмо самому себе.
#  - Если отправитель по умолчанию, выводит сообщение об успешной отправке.
#  - В противном случае выводит сообщение о нестандартном отправителе.