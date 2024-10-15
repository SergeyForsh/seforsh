def say_hello():
    print('Hello')
say_hello()
say_hello()

def say_hello(name):
    print('Hello', name)
say_hello('Sergey')    # принимающая функция
say_hello('Elena')
say_hello('Dima')
# возвращающая функция
import random
def lottery():
    tickets = [1,2,3,4,5,6,7,8,9,10]
    win = random.choice(tickets)
    return win
win = lottery() + lottery()
print(win)
def lottery(mon,thue):
    tickets = [1,2,3,4,5,6,7,8,9,10]
    win1 = random.choice(tickets)
    tickets.remove(win1)
    win2 = random.choice(tickets)
    print(mon, thue)
    return win1, win2

win1, win2 = lottery(mon:'mon',thue:'thue')
print(win1, win2)
            # почему? что не так?
win1, win2 = lottery(mon:'mon',thue:'thue')
#                             ^
# SyntaxError: invalid syntax
def lottery(*args, **kwargs):
    tickets = [1,2,3,4,5,6,7,8,9,10]
    win1 = random.choice(tickets)
    tickets.remove(win1)
    win2 = random.choice(tickets)
    print(*args)
    return win1, win2
                    # что опять не так?(синтаксис)
win1, win2 = lottery(*args:1,2,3,45,6,7,8,9,10)
print(win1, win2)
line 43
win1, win2 = lottery(*args:1,2,3,45,6,7,8,9,10)
#                               ^
# SyntaxError: invalid syntax
def test(a=2, b=True):
    print(a, b)

test(a:False, b:'ok')
                   # что опять не так?(синтаксис)
test(a:False, b:'ok')
line 52
#     test(a:False, b:'ok')
#           ^
# SyntaxError: invalid syntax