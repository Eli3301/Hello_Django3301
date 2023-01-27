# This is a sample Python script.
import random


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# a = 4
# b = 8
# c = a + b
#
# print (c)

# print ("питон не учат только псы")

# a = input (('enter data'))
# print(a)

# a = 1
# if a > 1:
#     print("a > 1 ")
# if True:
#     print('Hello')

# a = int (input ('Введите целое число'))
# if a/2:
#     print("да")



# a = int (input("enter digit"))
# if a < 0:
#     print('число меньше 0')
# elif a == 0:
#     print ("число равно 0" )
# else:
#     print ('Число больше 0')


# a = int(input("enter 1st digit"))
# b = int(input("enter 2nd digit"))
# c = bool(input("enter true/false"))
#
# if a > 0 and b <= 0:
#     print ('and')
# elif a < 0 or b > 0:
#     print ('or')


# a = int(input("введите целое число"))
# b = int(input("введите целое число"))
# c = int(input("введите целое число"))
#
# if a > b and a > c:
#     print ('a')
# elif b > a and b > c:
#     print ('b ')
# else:
#     print("c")



# a = int(input("введите целое число"))
# b = int(input("введите целое число"))
# c = int(input("введите целое число"))
#
# if a > b and a > c:
#     print("Наибольшее:", a)
# else:
#     if  b > c:
#         print("Наибольшее:", a)
#     else:
#         print ("Наибольшее:", c)


# a = int(input('введите первое целое число:'))
# b = int(input('введите второе целое число:'))
# s = input("введите операцию:")
#
# if s == "+":
#     print(a + b)
# elif s == "-":
#     print(a - b)
# elif s == "*":
#     print(a * b)
# elif s == "%":
#     print(a % b)
# elif s== "^":
#     print(a ** b)


# a = int(input('введите первое целое число:'))
# b = int(input('введите второе целое число:'))
# c = int(input('введите третье целое число'))
# s = input("введите операцию:")
#
# if s == "+":
#     print(a + b + c)
# elif s == "-":
#     print(a - b - c)
# elif s == "*":
#     print(a * b * c)
# elif s == "%":
#     print(a % b % c)
# elif s== "^":
#     print(a ** b ** c)






# import random
# n = random.randint (100,999)
# print(n)
# s = str(n)
# a = int(s[0])
# b = int(s[1])
# c = int(s[2])
# print(a+b+c)


# оператор сложения строк
# a = "вот так работает"
# b = " конкатенация строк"
# print(a+b)

# оператор умножения строк
# str = "строка"
# print(10* str)

# длина строки (len)
# stra = 'Строка'
# print(len(stra))
# #функция выводит количество символов в строке

# a = input("Введите свое имя:")
# print("Привет," + a)
# print(3*a)


#домашнее задание презентация номер 1 задание 3


# name = input("Введите имя:")
# surname = input("Введите фамилию:")
# patronymic = input("Введите отчество:")
# age = int(input("введите возраст:"))
# city = input("Введите город:")
#
# print (name,surname,patronymic)
# print (age)
# print (city)


# s = "Hello"
# print(s[0], s[4], s[-5])
#


# s = "Hello world hello hello"
# print(s[0:4], s[1:3], s[1:])



# s = "Hello world hello hello"
# print(s[0:4:1], s[1:3], s[1:])

# s = "Hello"
# print(s[0:4:1], s[::1], s[0:5:2], s[::2])







# import random
# n = random.randint (100, 900 )
# print(n)
# s = str(n)
# a = int(s[0])
# b = int(s[1])
# c = int (s[2])
# print(a+b+c)



# s = "hello everybody"
# s_2 = "Hello Everybody"
# s_3 = "Hello everybody"
# # делаем строку заголовком
# print(s.title())
# # начинаем строку с заглавной буквы
# print(s.capitalize())
# # переводим строку в верхний регистр
# print(s.upper())
# # переводим строку в нижний регистр
# print (s.lower())
# # инверсия регистра
# print(s_2.swapcase())
# # проверям являются ли строки заголовками
# print(s.istitle())
# print(s_2.istitle())
# print(s_3.title())


# print("A".isdigit())
# print("A".isalpha())





# print(' and '.join(['dog', 'cat'])) #соединение
# print(' cat sam mat '.split(' ')) #разъединение


# s = str("Hello python")
# print(s[0:12:2])
# print(s[0:12:11])
# print(s.upper())
# print(s.swapcase())
# print("s".isdigit())
# print("s".isalpha())


# for i in range (4):
#     print(i)




# for i in range (100):
#     print(i)

# for i in "I am learning python":
#     print(i)


# range- числа


# a = input("введите строку")
# b = input ('введите символ')
# с =("")
#
# for i in a:
#     if i != b:
#        с += i
# print('Результат:',с)


# a = int(input('Введите начало: '))
# b = int(input('введите конец: '))
# c = int(input ('введите шаг: '))
# for i in range (a,b,c):
#     print(i)


# for i in range(94, 9184, 1):
#     if i%5==0:
#         print(i)

#массивы

# arr = ['string1', 'string2', 'string3']
# l = len(arr)
# print(arr,'длина:', l)


# arr = [1,7,9,10]
# for i in arr:
#     print(i)




# arr = [1,7,9,10]
# for i in arr:
#     if i == 9:
#         break
#     print(i)


# a = [10, 2, 3]
# print (a)
# a.append(7)
# print(a)

# arr = [1, 2, 5, 6, 7, 8, 9]
# sum = 0
# pr = 1
# for i in arr:
#     sum += i
#     pr *= i
# print('Сумма', sum)
# print('Произедение', pr)



# i = 0
# while i < 10:
#     print(i)
#     i = i + 1


# i = 0
# while i < 10:
#     print(i)
#     if i == 5:
#          break
#     i += 1



# i = 1
# result = 0
# while i <= 50:
#     result = result + i
#     i = i + 1
# print(result)


# i = 0
# while i < 10:
#     print(i)


# i = 0
# while i < 10:
#     print(i)
#     if i == 5:
#         break
#     i += 1


# i = 1
# while i <= 10:
#     print(i ** 2)
#     i +=1
#


# i = 15
# while i != 0:
#     print(i)
#     i -= 1


# a = int(input("введите первое число"))
# b = int(input('введите второе число'))
# while a < b:
#     a += 1
#     if a == 0:
#         break
#     print(a)



# for i in range(10):
#     print(i)
# else:
#     print('Ready')


# a = 0
# mas = []
# while a < 98:
#     a += 7
#     mas.append(a)
#
# print(mas, "Длина" , len(mas))


# total = 1
# while True:
#     x = int(input("enter a digit"))
#     if x == 0:
#         break
#     total *= x
#     print(total)



# total = 1
# while True:
#     x = int(input("enter a digit"))
#     if x == 0:
#         break
#     total *= x
#     print(total)



# a = float(input("enter a digit"))
# b = float(input("enter a digit"))
# c = str(input('choose the operation: +, -, /, *'))
#
# if c == '+':
#    print(a + b)
# if c == "-":
#    print(a - b)
# if c == "/":
#    print(a / b)
# if b == 0:
#    print('Делить на 0 нельзя')
# if c == "*":
#    print(a*b)
# if c == "0":
#    print("program terminated")


# while True:
#     a = float(input("enter a digit"))
#     b = float(input("enter a digit"))
#     c = str(input('choose the operation: +, -, /, *'))
#
#
#     if c == '+':
#        print(a + b)
#     elif c == "-":
#        print(a - b)
#     if b != "0" and c == "/":
#        pass
#     else:
#        print('Делить на 0 нельзя')
#     elif c == "*":
#        print(a*b)
#     # elif c == "0":
#     #    break
#     #
#
#    #  elif c == '/':
#    # print(a/b)


# elements = [1, 3, "a", 6, "b"]
# print(elements)

# elements = list()
# print(elements)

# elements = input()
# print(elements)

# import random
#
# c = [random.randint(0, 100) for i in range(10)]
# print(c)
# print(c[0])
# print(c[-1])
# print(c[5])
# print(c[-4])
#
#
# elements = []
# elements.append('a')
# elements.append('1')
# print(elements)



# elements = [1,3,'a',6, 'b']
# elements.insert(1,2,)
# print(elements)

# elements = [1,3,'a', 6, 'b']
# elements[1] = 5
# print(elements)

# elements = [1, 3, 'a', 6, 'b', 7]
# del elements[5]
# print(elements)


# elements = [1, 3, 'a', 6, 'b']
# elements.remove('a')
# print(elements)

# my_list = ['hello', 'world']
# elements = [1, 3, my_list, 6, 'a', 'b' ]
# del elements[2][1]

# elements = [1, 3, 6, 'a', 'abc' , 123, 435]
# if 'abc' in elements:
#     print("yes")

# a = [1, 3, 5]
# b = [1, 5, 8, 9]
# print(a+b)

# d = ["h", "e", 'l',]
# e = ['a', 'd', 'v']
# d.extend(e)
# print(d)

#d extend не возвращает новый список а дополняет текущий

# a = (1,3,5)
# b = (1,5,8,9)
# print(a)



# elements = [1, 2, 3, "meow", 6]
# elements_len = len(elements)
# i = 0
# while i < elements_len:
#     print(elements[i])
#     i += 1



# # clear
# a = [1, 2, 3]
# a.clear()
# print(a)
#
# # copy
# a = [1, 2, 3]
# b = a.copy()
# print(id(a), id(b), a, b)


# a = [1, 2, 3]
# b = a.copy()
# print(id(a)), id(b), a, (b)

# #count
# elements = ["one, "two", "three", "one", "two", "one"]
# print(elements.count("one"))
#
# #index
# elements = ["one, "two", "three", "one", "two", "one" ]
# print(elements.index("three"))
# #bug


# #pop
# elements = [1, 'meow', 3, 'meow']
# elements.pop(1) #удаляем элемент с индексом 1
# 'meow' #pop возвращает удаденнный элемент списка
# print(elements)
# elements.pop() #удаляем первый элемент списка
# print(elements)
# elements.pop(-1) #удаляем последний элемент списка
# # reverse
# a = [1,2,3]
# a.reverse()
# print(a)
#

# #sort(по возрастанию)
# elements = [3, 19, 0, 3, 102, 3, 1]
# elements.sort()
# print(elements)
#
# #sort(по убыванию)
# elements = [3, 19, 0, 3, 102, 3, 1]
# elements.sort(reverse=True)
# print(elements)

# # elements = [1, 2, 3, [5, 7, 8],'abc', 4]
# elements = [['яблоки', 50], ['апельсины', 190], ['груши', 100]]
# print(elements)
# print(elements[0][0])

# elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# prices1 = [20]
# a = prices1 * 10
# print(a)


# # elements = [1, 2, 3, [5, 7, 8],'abc', 4]
# elements = [['яблоки', 50], ['апельсины', 190], ['груши', 100]]
# print(elements[0])
# print(elements[1][0])


# elements[START:STOP:STEP]

# elements = [1, 3, 7, "пес"]
# elements.reverse()
# print(elements)

# elements = [1, 2, 3, 4, 5, 20]
# elements.remove(20)
# print(elements)

# list1 = [5, 10, 15, 20, 25, 50, 20]
# print("Список: /n", list1)
# ind = list1.index(20)
# list1[ind] = 200
# print("Измененный список: /n", list1)


# a = [4, 6, 'py', 'tell', 78]
# b = [44, 'hello', 56, 'exept', 3]
#
# a.extend(b)
# a.insert(3, 6)
# print(a)
# for i in a:
#     if type(i) is str:
#         a.remove(i)
# a.sort()
# print(a)
# print(len(a))


# list1 = [5, 10, 15, 20, 25, 50, 20]
# print("Список: /n", list1)
# ind = list1.index(50)
# list1[ind] = 200
# print("Измененный список: /n", list1)


# a = int(input("enter a digit:"))
# b = int(input("enter a digit:"))
# c = str(input("enter a string:"))
# d = float(input("enter a float digit:"))
# g = a + b + d
# print(c)
# print(g)

# if a == 4.2:
#     print("аккумулятор полностью заряжен")

# a = (1, 2, 3, 4, 5, 6)
# b = [1, 2, 3, 4, 5, 6]
# print(a.__sizeof__())
#
# print(b.__sizeof__())

# a = (10, 2.13, "square", 89, "C")
# b = [1, 2, 3]
# c = list(a)
# d = tuple(b)
# print(a,b,c,d)

# a = (10,22)
# c = (1,6,7)
# print(a+c)

# x = (1,2,3,4)
# z = x * 3
# print(z)

# a = (1,2,3,4,5,6,7,8,9)
# b = (1,8,7)
# print('max', max(a), 'min', min(a))


# import random
# a = [random.randint(0,100) for i in range(10)]
# b = tuple(a)
# print(b)
# print('max', max(a), 'min', min(a))


# A = (13.5, 43, 49, 67, 32, 12, 98, 6, 10, 34, 20, 55, 68, 14, 60, 14 )
# B = (53, 21, 4, 23, 76, 3, 43, 12, 54, 342, 21)
# a = (sum(A))
# b = (sum(B))
# print(a)
# print(b)
# if a > b:
#    print("сумма больше в кортеже A ")
# elif a < b:
#     print('сумма больше в кортеже В')
# print('max', max(A), 'min', min(A))
# print('max', max(B), 'min', min(B))
# z = A.index(min(A))
# n = B.index(min(B))
# print(z)
# print(n)


# import random
# a = [random.randint(0, 5) for i in range(5)]
# n = [random.randint(-5, 0) for i in range(5)]
# x = a+n
# b = tuple(a)
# m = tuple(n)
# y = tuple(x)
# print(x)
# print(x.count(0))


# a = ('one', 'two', 'three')
# c = ','. join(a)
# print(c)

# a = [4, 6, 'py', 'tell', 78]
# b =[44, 'hello', 56, 'exept', 3]
# a.extend(b)
# a.insert(3,6)
# print(a)
# for i in a:
#     if type(i) is str:
#         a.remove(i)
# a.count()
# print(a)


# d = {}
# d = {'dict':1, "dictionary": 2}
# print(d)

# d = dict(short="dict", long="dictionary")
# d_2 = dict([(1,1), (2,4)])
# print(d, "\n", d_2)


# d = dict.fromkeys(["a", "b"])
# d_2 = dict.fromkeys(["a", "b"], 100)
# print(d, '\n', d_2)

# d = {a: a ** 2 for a in range(8)}
# print(d)

# d = {2: 3, 3: 4, 4: 5}
# d[9] = 9 ** 2
# print(d[2])
# print(d)

# Months = {1:'Jan', 2:'Feb', 3:'Mar'}
# count = len(Months)
# print(count)

# prices = {"firecracker": 5,
#           "ball shell": 10,
#           "fontain" : 3,
#           "girandola" : 20,
#           "rocket" : 6
#           }
#
#
# print(prices)
# count = len(prices)
# print(count)


# Position = {'Manager': {'Director',
#                         'Deputy Director'},
#
#             'Teacher': {'Specialist',
#                         'Methodist',
#                         'Senior Lecturer'},
#             'Staff': {'Cleaner',
#                       'Porter',
#                       'Watchman'}}
# count1 = len(Position)
# count2 = len(Position['Manager'])
# count3 = len(Position['Staff'])
#
# print(count1)
# print(count2)
# print(count3)


# Salary = {'Director': 120800.0,
#          'Secretary': 101150.25,
#          'Locksmith': 188200.00,
#           'Manager': 2000.99}
# print(Salary)
# key = 'Secretary'
# if key in Salary:
#     del Salary['Secretary']
#     print(Salary)
# key2= 'Manager'
# if key2 in Salary:
#     del Salary[key2]
# print(Salary)


# Words = dict()
# count = int(input('Количество слов в словаре: '))
# i = 0
# while i<count:
#     print('Ввод слов')
#     wrd = str(input('Слово'))
#     value = int(input('Значение'))
#     if wrd not in Words:
#         Words[wrd] = value
#     i=i+1
# print(Words)


# Numbers = dict(zip([1, 2, 3], ['Pes', 'Kot', 'um gato']))
# print(Numbers)

# Months = {1: 'Jan', 2: 'Feb', 3:'Mar',
#           4: 'Apr', 5: 'May', 6: 'Jun',
#           7: 'Jul', 8: 'Aug', 9: 'Sep',
#           10: 'Oct', 11: 'Nov', 12: 'Dec'}
# for mn in Months:
#     print(mn, ': ', Months[mn])

# person = {'Name': 1,
#          'Age': 2,
#          'City': 3,}
# key = 'Age'
# print(key)

# person = {'name': "kelly", "age":25, "city": "New york"}
# print(person['age'])
# print(person['name'])
# print(person['city'])

# Models_data = {"BMW": ["model_1",
#         "model_2", "model_3"],
#        "Tesla": ["Model s",
#                 "Model A",
#                 "Model B"]}
# print(Models_data["BMW"][0], Models_data["BMW"][2])
# print(Models_data["Tesla"][0], Models_data['Tesla'][2])


# d1 = {"a": 100, "b": 200, "c": 300}
# d2 = {"a": 300, "b": 200, "d": 400}
# print(d1["b"] == d2["b"])

# Elements_list = dict(zip(["k", "l", "r", "u", "w", "l"], ['Pes', 'Kot', 'um gato', "rehearsal", "bastard", "python" ]))
# print(Elements_list)

#множество из цифр
# num_set={1, 2, 3, 4, 5, 6}
# print(num_set)

#множество из строк

# string_set = {"nicolas", 'michelle', "john", "mercy"}
# print(string_set)

#во множестве удобно хранить  данные, если нам не важно в каком порядке они будут выводиться.

# mixed_set = {2.0, "Nicholas", (1,2,3)}
# print(mixed_set)

# num_set = set([1, 2, 3, 1, 2])
# print(num_set)

# x = {}
# print(type(x))

# x = set()
# print(type(x))

# months = set(["Jan", "Feb", "March", "Apr", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"])
# for m in months:
#     print(m)



# months = set(["Jan", "Feb", "March", "Apr", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"])
# print("May" in months)


# months = set(["Jan", "Feb", "March", "Apr", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"])
# months.add("Feb")
# print(months)

#discard удаляет выбранный элемент множества.
#если выбранный элемент во множестве отсутствует, команда пропускается.
# num_set = {1, 2, 3, 4, 5, 6}
# num_set.discard(7)
# print(num_set)


#remove() удаляет выбранный элемент множества.
#если выбранный элемент во множестве отсутствует, интерпретатор выдает ошибку
# num_set = {1, 2, 3, 4, 5, 6}
# num_set.remove(3)
# print(num_set)

#pop удаление любого(обычно первого) элемента
# num_set = {1, 2, 3, 4, 5, 6}
# num_set.pop()
# print(num_set)

#clear очищает множество
# num_set = {1, 2, 3, 4, 5, 6}
# num_set.clear()
# print(num_set)


#объединение множеств, функция union()
# months_a = set(["Jan", "Feb", "March", "Apr", "May", "June"])
# months_b = set([ "July", "Aug", "Sep", "Oct", "Nov", "Dec"])
# all_months = months_a.union(months_b)
# print(all_months)

# x = {1, 2, 3}
# y = {4, 3, 6}
# z = {7, 4, 9}
# o = x. union(y, z)
# print(o)

# months_a = set(["Jan", "Feb", "March", "Apr", "May", "June"])
# months_b = set([ "July", "Aug", "Sep", "Oct", "Nov", "Dec"])
# print(months_a | months_b)


# x = {1, 2, 3}
# y = {4, 3, 6}
# z = {7, 4, 9}
# print(x | y | z)

# x = {1, 2, 3}
# y = {4, 3, 6}
# print(x & y)

# A = {1, 2, 3}
# B = {4, 3, 6}
# print(A - B)
# print(B - A)

# #есть повт элементы(False)
# string_set = {"nicolas", 'michelle', "john", "mercy"}
# names_b = {"Jeff","Jessy", "Jemma", "michelle" }
# x = string_set.isdisjoint(names_b)
#
# print(x)
#
#
# # нет повт элементов(True)
# string_set = {"nicolas", 'michelle', "john", "mercy"}
# names_b = {"Jeff","Jessy", "Jemma" }
# x = string_set.isdisjoint(names_b)
# print(x)


#длина множества
# names_a = {"Nicolas", "Michelle", "John", "Mercy"}
# print(len(names_a))

#неизменяемое множество занимает меньше памяти, чем кортежи.
# my_set = frozenset([1, 2, 3, -10, 40])
# print(type(my_set))

#задача1
# a = [0, 0, 1, 5, 6, 7, 8, 9, 9, 9]
# st = set(a)
# print(len(st) == len(a))


#task2

# # 1. создаем словарь
# dct = {1: 'value_1', 2: 'value2', 3: 'value_3'}
#
# # 2. добавляем в словарь элемент с ключом "str_key" и значением 12345
# dct['str_key'] = 12345
# print(dct)
#
# # 3. Добаляем в словарь новый элемент с ключом ('it', 'is', 'tuple') и значением [11, 22, 'list value, 33, {1, 2, 3}
# dct[("it", "is", 'tuple')] = [11, 22, 'list_value', 33, {1, 2, 3}]
# print(dct)
#
# # 4. получаем элемент словаря по ключу "str_key"
# # Способ 1: Напрямую - в случае отсутствия ключа формируется исключение
# item_by_key_v1 = dct['str_key']
# print(item_by_key_v1)
# # способ 2: Через функцию get() - в случае отсутствия ключа возвращается дефолтное значение "no item'
# item_by_key_v2 = dct.get('str_key', "No item")
# print(item_by_key_v2)
# # 5. Удаляем элемент с ключом "2" из словаря
# item_deleted = dct.pop(2, "no item")
# print(item_deleted)






#task3
# num_set = {1, 2, 3, 4, 5, 6}
# num_set2 = frozenset([1, 2, 3, -10, 40])
# print(num_set | num_set2)
# intersection = num_set & num_set2
# print(intersection)

# try:
#     a = 100/0
# except ArithmeticError:
#     a = 0
# print(a)

# my_list = [1, 2, 3, 4, 5]
# try:
#     my_list[6]
# except IndexError:
#
#     print("Этого индекса не существует")


# my_dict = {"a": 1, "b": 2, "c": 3}
# try:
#     value = my_dict["d"]
# except IndexError:
#     print("this index does not exist")
# except KeyError:
#     print("this key is not in the dictionary")
# except:
#     print("Another error occured")


# my_dict = {"a": 1, "b": 2, "c": 3}
# try:
#     value = my_dict["b"]
#
# except KeyError:
#     print("this key is not in the dictionary")
# finally:
#     print("operator finally has been executed")




# my_dict = {"a": 1, "b": 2, "c": 3}
# try:
#     value = my_dict["a"]
#
# except KeyError:
#     print("this key is not in the dictionary")
# else:
#     print("errors not found")
# finally:
#     print("operator finally has been executed")




# try:
#     a = int(input())
#     b = int(input())
#     c = a / b
# except ZeroDivisionError:
#      print("0")
# else:
#      print(c**2)
# finally:
#       print("operator finally has been executed")



# f = open('Text Document.txt.', "r")
# print(*f)
# f.close()


# x = open('Text Document.txt.', "r")
# print(x.readlines())

# f = open('Text Document.txt.', "r")
# try:
#     print(*f)
# finally:
#     f.close()


# with open('Text Document.txt.') as f:
#     print(*f)


# f = open('Text Document.txt', "r")
# print(f.read(5))
# print(f.read(10))

# x = open('Text Document.txt.', "r")
# print(x.readline())
# print(x.readline())
# print(x.readline())

# x = open('Text Document.txt.', "r")
# print(x.readline(3))
# print(x.readline(4))
# print(x.readline(5))


# f = open('xyz.txt', "w")
# f.write('hello \nworld')
# f.close()

# a = open('xyz.txt', "r")
# print(*a)


# import os
# os.rename("xyz.txt", "abc.txt")



# import os
# print("текущая директория:", os.getcwd())
# os.chdir('folder')
# print("текущая директория изменилась на folder:", os.getcwd())

# #возврат в предыдущую директорию
# import os
# print("текущая директория:", os.getcwd())
# os.chdir('..')
# print("текущая директория изменилась :", os.getcwd())

# import os
# os.makedirs('nested1/nested2/nested3')



# with open ('task1.txt') as f:
#     s = f.readlines()
#     print(s)
# for i in s:
#     i = i.replace('_', ' ')
#     l = i.split(' ')
# print(l)
# sum = 0
# for i in l:
#     if i.isdigit():
#         i = int(i)
#         sum += i
# print(sum)



# import os
# # os.mkdir('C:\\Users\\User\\Desktop\\Za')
# # f = open(r'C:\\Users\\User\\Desktop\\Za\\test_1.txt', 'w')
# # f1 = open(r'C:\\Users\\User\\Desktop\\Za\\test_2.txt', 'w')
# # f2 = open(r'C:\\Users\\User\\Desktop\\Za\\test_3.txt', 'w')
# # f.close()
# # f1.close()
# # f2.close()
# # os.rename('C:\\Users\\User\\Desktop\\Za\\test_1.txt', 'C:\\Users\\User\\Desktop\\Za\\ren_1.txt')
# # os.rename('C:\\Users\\User\\Desktop\\Za\\test_2.txt', 'C:\\Users\\User\\Desktop\\Za\\ren_2.txt')
# # os.rename('C:\\Users\\User\\Desktop\\Za\\test_3.txt', 'C:\\Users\\User\\Desktop\\Za\\ren_3.txt')
#
# os.remove('C:\\Users\\User\\Desktop\\Za\\ren_1.txt')
# os.remove('C:\\Users\\User\\Desktop\\Za\\ren_2.txt')
# os.remove('C:\\Users\\User\\Desktop\\Za\\ren_3.txt')
#
# os.rmdir('C:\\Users\\User\\Desktop\\Za')

# A = [1,2,3]
# B = ["pes", "kot", "lichoimec"]
# s = dict(zip(A,B))
# print(s)

# D = [1, 2, 3, 4, 5, 8, 0, 0]
# K = [3, 5, 7, 8, 9]
# print(len(D))
# print(len(K))

# a = {2, 5, 7, 8, 9, 0, 4, 6, 4, 7}
# print(type(a))

# a = ('hellomynameis')
s = dict.fromkeys("hellomynameis")
print(type(s))
























# os.chdir("D:\\pes\\Zadachi")
# f = open('D:\\pes\\Zadachi\\test1.txt', 'w')
# f1 = open('D:\\pes\\Zadachi\\test2.txt', 'w')
# f2 = open('D:\\pes\\Zadachi\\test3.txt', 'w')
#
# f.close()
# f1.close()
# f2.close()
#
# os.rename('D:\\pes\\Zadachi\\test1.txt', 'D:\\pes\\Zadachi\\rename1.txt')
# os.rename('D:\\pes\\Zadachi\\test2.txt', 'D:\\pes\\Zadachi\\rename2.txt')
# os.rename('D:\\pes\\Zadachi\\test3.txt', 'D:\\pes\\Zadachi\\rename3.txt')
#
# os.remove('D:\\pes\\Zadachi\\rename1.txt')
# os.remove('D:\\pes\\Zadachi\\rename2.txt')
# os.remove('D:\\pes\\Zadachi\\rename3.txt')
#
# os.rmdir('D:\\pes\\Zadachi')

