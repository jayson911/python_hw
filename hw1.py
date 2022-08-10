# strings
#
# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.
st = 'as 23 fdfdg544'
print(', '.join(i for i in st if i.isdigit()))

# #################################################################################
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі
st = 'as 23 fdfdg544 34'
print(', '.join(''.join(i if i.isdigit() else ' ' for i in st).split()))
# #################################################################################
#
# list comprehension
#
# 1)є строка:
# greeting = 'Hello, world'
greeting = 'Hello, world'
print([i.upper() for i in greeting])
# записати кожний символ як окремий елемент списку і зробити його заглавним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']
# greeting = 'Hello, world'
# i = list(str.upper(greeting))
# print(i)
#
# 2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]
#
print([i**2 for i in range(50) if i % 2])
# function
#
# - створити функцію яка виводить ліст
def func1(l):
    for i in l:
        print(i)
    func1(1, 2,3 )
# - створити функцію яка приймає три числа та виводить та повертає найбільше.
def func2(a, b, c):
    res = max(a, b, c)
    print(res)
    return res
func2(5, 23, 2)
# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
def func3(*args):
    print(max(args))
    return min(args)
# - створити функцію яка повертає найбільше число з ліста
def func4(l):
    return max(l)
# - створити функцію яка повертає найменьше число з ліста
def func5(l):
    return min(l)
# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
def func6(l):
    res = 0
    for i in l:
        res+1
# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
def func7(l):
    return sum(l) / len(l)
#
#
#
#
# ################################################################################################
# 1)Дан list:
#   list = [22, 3,5,2,8,2,-23, 8,23,5]
#   - знайти мін число
#   - видалити усі дублікати
#   - замінити кожне 4-те значення на 'X'
# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції
def find_min():
    l = [22, 3,5,2,8,2,-23, 8,23,5]
    print(min(l))

def del_duplicate():
    l = [22, 3,5,2,8,2,-23, 8,23,5]
    print(list(set(l)))

def swap_to_x():
    l = [22, 3,5,2,8,2,-23, 8,23,5]
    print(['X' if not (i+1)%4 else v for i, v in enumerate(l)])

def square(n):
    for i in range(n):
        if i == 0 or i ==n-1:
            print('*'*n)
        else:
            print('*'+' ' * (n - 2) + '*')

square(10)

# 3) вывести табличку множення за допомогою цикла while
# 4) переробити це завдання під меню
def multi_table():
    i = 1
    while i<=9:
        j = 1
        while j<=9:
            res = j*i
            print(res, end='')
            print ('  ' if res//10 else '   ', end= '')
            j += 1
        i += 1
        print()

multi_table()

while True:
    print('1) find_min')
    print('2) del_duplicate')
    print('3) swap_to_x')
    print('4) square')
    print('5) multi_table')
    print('9) exit')

    choice = input('make your choice: ')

    if choice == '1':
        find_min()
    elif choice == '2':
        del_duplicate()
    elif choice == '3':
        swap_to_x()
    elif choice == '4':
        square(5)
    elif choice == '5':
        multi_table()
    elif choice == '9':
        break


