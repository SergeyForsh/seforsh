name= input('Введите Ваше имя: ')          #str -строка! ввод внизу в терминале с клавиатуры
print('Здравствуйте,', name)
current_year = 2024                                  #int -число!
date_of_birth = input('В каком году вы родились?: ') #str -строка! ввод внизу в терминале с клавиатуры
age = current_year - int(date_of_birth)              #текущий год минус год рождения
print('В этом году Вам ', age, 'лет')
#my_string =input ('привет, я строка в верхнем регистре'.lower().upper())
#print(my_string)
#print('привет, я строка в нижнем регистре'.upper().lower())
# .upper() верхний регистр .lower() нижний регистр
print('my_string'.upper())
print('my_string'.upper().lower())
print('привет, я строка в нижнем регистре'.replace('привет', 'пока')) #замена слов
print('привет, я строка в нижнем регистре'.replace(' ', '#'))         #убрать пробелы или #







