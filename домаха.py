# a = int(input("enter an integer digit"))
# b = int(input("enter an integer digit"))
# c = str(input("enter a string"))
# d = float(input('enter a float digit'))
# e = a + b + d
# print(c)
# print(e)


# a = 1
# b = 5.8
# c = True
# d = ("ты че кот")
#
# a = str(a)
# b = str(b)
#
# print(a)
# print(b)
# print(c)
# print(d)


# Name = input('enter your name')
# Surname = input('enter your surname')
# patronymic = input('enter your patronymic')
# city = input('enter your city')
# age = int(input('enter your age'))
#
# print(Name, Surname, patronymic, age)
# print(city)
# print(age)

# a = int(input('введите число'))
# b = int(input('введите число'))
# c = int(input('введите число'))
#
# print(a+b+c)
# print(a-b-c)
# print(a*b*c)
# print(a/b/c)

# import random
# n = random.randint (100,999)
# print(n)
# a = n//100
# b = (n//10)%10
# c = n % 10
# print(a+b+c)

# a = int(input("введите целое число"))
# if a%2 == 0:
#     print('четное')
# else:
#     print("нечетное")

# a = int(input())
# b = int(input())
# c = int(input())
#
# if a>b and a>c:
#     print(a)
# elif b>a and b>c:
#     print(b)
# else:
#     print:c


# a = int(input("введите число"))
# l = input()
# c = int(input("введите число"))
#
# if l == "+":
#     print(a + c)
# elif l == "-":
#     print(a - c)
# elif l == "*":
#     print(a * c)
# elif l == "/":
#     print(a / c)


# x = int(input("введите число"))
# if  x > 0:
#     y=(2*x-10)
#     print(y)
# elif x == 0:
#     y=0
#     print(y)
# else:
#     y=2*abs(x)-1
#     print(y)


# n = int(input())
# z = int(input())
#
# a = (n < z)
# if a:
#     print(n, "меньше", z)
#

# презентация 2 творческое задание

# print("Программа для диагностики компрессора холодильника")
# a = int(input("введите значение сопротивления между правым верхним выходным контактом в омах"))
# b = int(input("ввелите значение сопротивления между верхним левым выходным контактом в омах"))
# if a == 15 and b == 20:
#      print("компрессор исправен")
# else:
#     print('компрессор неисправен')


# print("Rechargable batteries checker")
#
# value1 = str(input('enter the type of your battery'))
# if value1 == ("li-ion"):
#     print("Li-ion type of battery was chosen")
#     a = float(input("enter the voltage "))
#     if a = 2.4:
#         print("battery  is critically low")
#     elif a == 4.2:
#         print("battery is full")
#     else:
#         print('battery is ok')
#
#
# elif value1 == ("Li-fe"):
#     print("Li-fe type of battery was chosen")
#     b = float(input("enter the voltage "))
#     if b <= 2.5:
#         print('battery  is critically low')
#     elif b >= 3.64:
#         print('battery is full')
#     else:
#         print("battery is ok")
#
#
# elif value1 == ('ICR'):
#     print("ICR type of battery was chosen")
#     c = float(input("enter the voltage"))
#     if c <= 2.5:
#         print('battery  is critically low')
#     elif c >= 4.1:
#          print("battery is full")
#     else:
#         print("battery is ok")
#
#
# elif value1 == ('li-ti'):
#     print("Li-ti battery was chosen")
#     z = float(input("enter the voltage"))
#     if z <= 1.8:
#          print('battery  is critically low')
#     elif z >= 3.64:
#          print("battery is full")
#     else:
#          print("battery is ok")
#
#
# elif value1 == ('Pb'):
#     print("Pb battery")
#     v = float(input('enter the voltage'))
#     if v == 2.11:
#         print("battery is full")
#     elif v <= 1.8:
#         print('battery  is critically low')
#     else:
#         print("battery is ok")


# year = int(input())
# if year % 4!= 0:
#     print("usual year")
# elif year % 100 == 0:
#     if year % 400 == 0:
#         print('leap year')
#     else:
#         print('usual year')
# else:
#     print('leap year')


# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# if a+ b <= c or a + c <= b or b + c <= a:
#     print("Треугольник не существует")
# elif a !=b and a != c and b != c:
#     print("Разносторонний")
# elif a == b == c:
#     print("Равносторонний")
# else:
#     print("Равнобедренный")


# from math import sqrt
# x = float(input("x="))
# y = float(input("y="))
# r = float(input("r="))
# h = sqrt(x ** 2 + y ** 2)
# print("Расстояние до точки от начала координат равно %.2f" % h)
# if h > r:
#     print("Точка находится за пределами круга")
# else:
#     print('Точка при принадлежит кругу ')


# a = str('нафан')
# s = ''.join(a.split())
# print(a)
# print(s)
# if str('нафан') == "".join(reversed('нафан')) :
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# a = str('revival, stronghold, crusader, game, holy land')
# print(a[3])
# print(a[44])
# print(a[0:5])
# print(a[0:44])
# print(a[2], a[4], a[6], a[8], a[10], a[12], a[14], a[16], a[18], a[20], a[22], a[24], a[26], a[28], a[30], a[32], a[34], a[36], a[38], a[40], a[42], a[44] )
# print((a[1], a[3], a[5], a[7], a[9], a[11], a[13], a[15], a[17], a[19], a[21], a[23], a[25], a[27], a[29], a[31], a[33], a[35], a[37], a[39], a[41], a[43]), a[45] )
# d = ''.join(reversed('revival, stronghold, crusader, game, holy land'))
# print(d)
# print(a[-46], a[-44], a[-42], a[-42], a[-40], a[-38], a[-36], a[-34], a[-32], a[-30], a[-28], a[-27], a[-25], a[-23], a[-22], a[-20], a[-18], a[-16], a[-14], a[-12], a[-10], a[-8], a[-6], a[-4], a[-2])
# print(len(a))




#for cycle

# a = str(input("введите строку"))
# b = str(input("введите символ"))
# c = ''
# for i in a:
#     if i != b:
#         c = c + i
# print('результат: ', c)



# a = int(input("введите начало"))
# b = int(input("введите конец"))
# c = int(input("введите шаг"))
# for i in range (a, b, c):
#     print(i)

# a = int(54)
# b = int(9184)
# for i in range (a, b,):
#     if i%5 == 0:
#      print(i)


# arr = ['string1', 'string2', 'string3']
# l = len(arr)
# print(arr, 'Длина', l)



# arr = [1, 7, 9, 10]
# for i in arr:
#     print(i)


# arr = [1, 7, 9, 10]
# for i in arr:
#     print(i)
#     if i == 9:
#         break


#добавление элемента в конец массива имя массива.append(значение)
# a = [1, 7, 9, 10]
# print(a)
# a.append(7)
# print(a)


# array.append(x) добавление элемента в конец массива(не требует ввода доп переменной)


# array.pop()    удаляет какой-то элемент из массива . по умолчанию удаляется последний элемент  не требует ввода доп переменных
# array.remove(x) удалить первое вхождение х из массива.   не требует доп переменных
# array.reverse() обратный порядок элементов в массиве не требует доп переменных


# array.count(x)  возвращает количестао вхождений х в массив(ТРЕБУЕТ ВВОДА ДОП ПЕРЕМЕННОЙ)
# array.index(x)  номер первого вхождения в массив (ТРЕБУЕТ ВВОДА ДОП ПЕРЕМЕННОЙ)



# arr = ["jocker", "jocker", "sherkhan", "lemmi"]
# print(arr)
# arr.reverse()
# print(arr)
#


# a = [1, 5, 8, 9]
# d = sum(a)
# print(d)





# a = [1, 5, 8, 9]
# sum = 0
# pr = 1
# for i in a:
#     sum = sum+i
#     pr = pr * i
# print("сумма", sum)
# print("произведение", pr)
#




# for i in range(1,10):
#     a= i*i
#     print(a)


# for i in range(1,6): #первый цикл работает медленнее второго
#     for j in range(1,6):
#         print(i*j, '', end='')
#     print()

##первый цикл работает медленнее второго!


##кортежи
# import random
# a = random.randint(0,5)
# b = random.randint(0,5)
# s = random.randint(0,5)
# d = random.randint(0,5)
# w = random.randint(0,5)
# q = random.randint(0,5)
# e = random.randint(0,5)
# r = random.randint(0,5)
# j = random.randint(0,5)
# t = random.randint(0,5)
# e = (a, b, s, d, w, q, e, r, j, t, e)
# print(e)
# print('max', max(e), 'min', min(e))





# import random
# a = random.randint(0,5)
# b = random.randint(0,5)
# s = random.randint(0,5)
# d = random.randint(0,5)
# w = random.randint(0,5)
# q = random.randint(0,5)
# e = random.randint(0,5)
# r = random.randint(0,5)
# j = random.randint(0,5)
# t = random.randint(0,5)
#
# A = random.randint(-5,0)
# B = random.randint(-5,0)
# C = random.randint(-5,0)
# D = random.randint(-5,0)
# W = random.randint(-5,0)
# Q = random.randint(-5,0)
# E = random.randint(-5,0)
# R = random.randint(-5,0)
# J = random.randint(-5,0)
# T = random.randint(-5,0)
#
#
# e = (a, b, s, d, w, q, e, r, j, t, e)
# E = (A, B, C, D, W, Q, E, R, J, T, E)
# print(e)
# print(E)
# S = (e+E)
# print(S)
# print (S.count(0))



#Словари
# person = dict(zip(["name","age","city"],["Yelisei", 21, "Brest"]))
# key = person["age"]
# print(key)


# d = {}
# print(type(d))



# d = dict(short="dict", long='dictionary')
# d_2 = dict([(1,1), (2,4)])
# print(d, '\n', d_2)


# d = dict.fromkeys(['a','b'])
# d_2 = dict.fromkeys(['a','b'], 100)
# print(d, '\n', d_2)



# d = {a: a ** 2 for a in range(7)}
# print(d)

# изменение и добавление данных в словаре по ключу
# d = {1: 2, 2:4, 3:9}
# d[4] = 4**2 #задаем либо добавляем значение ключу
# print(d[1])
# print(d)


