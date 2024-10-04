set_ = {1,2,3,4,5,1,2,3,'String', True, (1,2,3)}   #коллекция 1,2,3 - повторяются
print(set_)
list_ = [1,1,2,3,4,5,2]                 #не повторяющиеся значения
list_ = set(list_)
print(set(list_))
print(list_.discard(1))  # удалена (1)
print(list_)

set_ = {1,2,3,4,5,1,2,3,'String', True, (1,2,3)}   #коллекция 1,2,3 - повторяются
print(set_)
list_ = [1,1,2,3,4,5,2]
list_ = set(list_)
print(set(list_))
print(list_.remove(1))  # удалена (1)
print(list_)            # discard & remove одинаково

et_ = {1,2,3,4,5,1,2,3,'String', True, (1,2,3)}   #коллекция 1,2,3 - повторяются
print(set_)
list_ = [1,1,2,3,4,5,2]
list_ = set(list_)
print(set(list_))
print(list_.add(10))  # добавить (10)
print(list_)





