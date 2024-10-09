tuple_ = (1, 2, 3, 4, True, 'String') #кортеж неизменяемая
print(tuple_)
tuple_2 = (1, 2, 3, 4)
print(tuple_2)
tuple_3 = (1, 2, 3, 4)
tuple_ = (1, 2, 3, 4)
list_ = ([1, 2, 3, 4])
print(type(tuple_3))
print(type(tuple_[0]))
print(tuple_[0])
print(tuple_.__sizeof__())
print(list_.__sizeof__())
tuple_ = ([1, 2], 0)
print(tuple_)
tuple_ [0] [0]= 2
print(tuple_)
tuple_ = ([1, 2], 0) + (1, 2)
print(tuple_)
tuple_ = (1, 2) *3            #умножить (3 раза)
print(tuple_)
immutable_var_ = (1, 2, True, 'Str')
print(immutable_var_)
mutable_list_ =([1, 2, 3, 4])
print(mutable_list_)
print()
tuple_ = 3, 8.0, "Word", True
print('Immutable tuple: ', tuple_)
print('Types of data')
print(type(tuple_[0]))
print(type(tuple_[1]))
print(type(tuple_[2]))
print(type(tuple_[3]))
# Изменить кортеж невозможно по своим свойствам,
# однако если кортеж содержит в себе список заключенный в квадратные скобки [],
# то возможно изменять элементы списка включенные в кортеж
tuple_1 = 3, 8, ["Word", True]
print(tuple_1)
tuple_1[2][1] = False
print(tuple_1)
list = [3, 5, 8, 4]
print(list)
print('Mutable list: ')
list[1] = 20
print(list)
list.append('Modified')
print(list)
list.extend('Whata')
print(list)
list.remove(8)
print(list)
