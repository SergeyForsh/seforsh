phone_book = {'Sergey': 89313262685, 'Elena': 89217895733} # ключ и значение
print(phone_book)
phone_book = {'Sergey': 89313262685, 'Elena': 89217895733}
print(phone_book['Sergey'])
phone_book = {'Sergey': 89313262685, 'Elena': 89217895733}
print(phone_book)
phone_book ['Sergey'] = 1234567
print(phone_book)
phone_book ['Max'] = 987654321 # не существующий ключ добавляется
print(phone_book)
del phone_book ['Max']            # удаляем
print(phone_book)
phone_book.update({'Saahov':89995885,'Vova':899765455,  #добавляем.
                   'Anna':81234567})                    # порядок может быть не строгим
print(phone_book)
print(phone_book.get ('Sergey'))  #значение по указанному ключу
print(phone_book.get ('Olya'))    #ключ не найден не существует
print(phone_book.get ('Olya', 'Такого ключа нет'))
print(phone_book.pop('Sergey'))
phone_book = {'Sergey': 89313262685, 'Elena': 89217895733}
print(phone_book)
print(phone_book.pop('Sergey'))    #метод поп удаляет значение и возвращает значение
print(phone_book)
phone_book = {'Sergey': 89313262685, 'Elena': 89217895733}
print(phone_book)
a= phone_book.pop('Sergey')  #сохраняем переменную
print(phone_book)
print(a)                  #выводим ее получаем 89313262685
print(phone_book)
phone_book.update({'Saahov':89995885,'Vova':899765455,'Masha':89313262686})
list_ = [1,2,3,4]
list_.pop(0)
print(list_)
print(phone_book)
print(a)
phone_book.update({'Saahov':89995885,'Vova':899765455,'Masha':89313262686})
print(phone_book.keys())  #метод кейс-получаем список ключей в книге
phone_book.update({'Saahov':89995885,'Vova':899765455,'Masha':89313262686})
print(phone_book.values()) #метод валуес выводит значение
phone_book.update({'Saahov':89995885,'Vova':899765455,'Masha':89313262686})
print(phone_book.items())  #метод итемс возвращает пары-ключ/значение

phone_book = {'Sergey': [89313262685,89313262686], 'Elena': 89217895733,
              'Vova':899765455,'Masha':89313262686}  #тел.книга список [1, 2, 3, 4]
#изменять можно только значения, но не ключ.  Словарь!
print(phone_book)
