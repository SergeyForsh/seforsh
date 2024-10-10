#print(1)
#print(2)
#print(3)
#name = input ('Введите Ваше имя: ')
#if name == 'Urban':    # после двоеточия обязательно отступ таб или 4 пробела условие if - "если"
#    print('Здравствуйте администратор')
#print('Привет', name)
#name = input ('Введите Ваше имя: ')
#if name == 'Urban':
#    print('Здравствуйте администратор')
#if name == 'Денис':
#    print('Здравствуйте преподаватель') #если Urban, то админ, если Денис, то преподаватель
#else:                  # else - "иначе" и двоеточие.
#    print('Привет', name)
#print()
#number=int(input('Введите число:'))  #Fizz, Buzz, FizzBuzz
#if number % 3==0:
#    print('Fuzz')
#if number % 5==0:
#    print('Buzz')
#if number % 3==0 or number % 5==0:  # Or - это не строгий оператор, то есть либо слева, либо справа
                                     # and - и - строгий оператор
#    print('FuzzBuzz')
#print()
#number=int(input('Введите число:'))  #Fizz, Buzz, FizzBuzz
#if number % 3==0:
#    print('Fuzz')
#elif number % 5==0:
#    print('Buzz')
#elif number% 3==0 and number % 5==0:
#    print('FuzzBuzz')
#  ДЗ к модулю 2_2
first = int(input('Введите 1-е число: '))
second = int(input('Введите 1-е число: '))
third = int(input('Введите 1-е число: '))
list_ = [first, second, third]
print(list_)
if list_[0] == list_[1]:
    if list_[1] == list_[2]:
        print(3)
    else:
        print(2)
elif list_[1] == list_[2]:
    print(2)
else:
    print(0)
print()
first = int(input('Введите первое произвольное число: '))
second = int(input('Введите второе произвольное число: '))
third = int(input('Введите третье произвольное число: '))
if first == second and first == third and second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)