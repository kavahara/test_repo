# mark = int(input())
# if mark >=90:
#     print('Отлично, Ваша оценка 5!')
# else:
#     if mark >=80:
#         print('Здорово, Ваша оценка 4!')
#     else:
#         if mark >=70:
#             print('Хорошо, Ваша оценка 3!')
#         else:
#             if mark >=60:
#                 print('Вам стоит подучить материал')
#             else:
#                 print('Вы не сдали экзамен')

# number = int(input())
# if number <0:
#     print('negative')
# else:
#     if number >0:
#         print('positive')
#     else:
#         if number == 0:
#             print('zero')

# x = int(124)
# y = int(136)
# z = int(152)
# if x>=y<=z:
#     print(y)
# elif x>=z<=y:
#     print(y)
# else:
#     print(x)

# x = int(input())
# y = int(input())
# if (x%y) == 0:
#     print(f'x делится на y')
#     print("Частное: %d" % (x//y))
# else:
#     print(f'x не делится на y')
#     print("Частное: %d" % (x//y))
#     print("Остаток: %d" % (x%y))


# year = int(input())
# if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
#     print('YES')
# else:
#     print('NO')

# nums=[1,2,4,5,6,7,8,10,9]
# target=(3)
# if target in nums:
#     print('Да')
# else:
#     print('Нет')


# num = int(input())
# a = ord('a')
# z = ord('z')
# A = ord('A')
# Z = ord('Z')
# if a<=num<=z or A<=num<=Z:
#     print(f'Это буква "{chr(num)}"')
# else:
#     print(f'Это не буква, а символ "{chr(num)}"')


# greeting = input()
# if 'Hi' in greeting:
#     print('Привет!')
# else:
#     print('NO')


# str_a = '50'
# b = 10
# c = int(str_a) + b
# print ("The value of c = ",c) 

# count = int(0)
# number = input()
# if type(number) == int:
#     count=number
#     print(count)
# else:
#     print('error')

# count = int(0)
# number = input()
# if number.isnumeric():
#     count=int(number)
# print(count)

# labels = ['i','l','o','v','e','u']
# for i in labels:
#     print(f'I like brand {i}')

# string='jkagajal'
# print(string[1::2])

# name_of_list = 'hi'
# new_list = name_of_list[(len(name_of_list) + 1) // 2:] + name_of_list[:(len(name_of_list) + 1) // 2]
# print(new_list)

# string = 'asd,asdad,324234,1234567890,qwert,yuiopdwdqwdcxzc,sdsaasd'
 
# for i in string.split(','):
#   if(len(i) > 10):
#     print('%s\r\n%s' % (i[:10], i[11:]))
#     continue  
#   print(i)


    # name_of_list = list('hello')
    # new_list = name_of_list[(len(name_of_list) + 1) // 2:] + name_of_list[:(len(name_of_list) + 1) // 2]
    # for i in new_list:
    #     print(f"['{i}']")
    # print(new_list)
    # new_list = (len(name_of_list) // 2) + (len(name_of_list) % 2)
    # z = name_of_list[new_list:] + name_of_list[:new_list]
    # for i in z:
    #     print(i)
    #     print(f"['{i}']\n")
    # n = (len(name_of_list) // 2) + (len(name_of_list) % 2)
    # z = name_of_list[n:] + name_of_list[:n] 

#     name_of_list = ['Школа']
# a = name_of_list[0]
# result = list(a)
# half1 = result[:int((len(result)+1)/2)]
# half2 = result[int((len(result)+1)/2):]
# new_list = half2 + half1
# print(new_list)

# list_ = ['Школа', 'devil']
# a = list_
# result = list(a)
# half1 = result[:int((len(result)+1)/2)]
# half2 = result[int((len(result)+1)/2):]
# new_list = half2 + half1
# print(new_list)

# list_ = input().split(",")
# tuple_ = tuple(list_)
# print(list_)
# print(tuple_)

# list_ = [1, 2, 3, 4, 5]
# new_list = [str(x) for x in list_]
# print(new_list)

# list_ = [1,2,3,4,5,6,7,8,9,10]
# new_list = list(map(str, list_))
# print(new_list)

# list_ = [1,2,3,4,5,6,7,8,9]
# new_list= ['четное' if i%2 == 0 else 'нечетное' for i in list_]
# print(new_list)

# list_ = list(range(20))
# print(list_)

# list_ = list(range(0,101,2))
# print(list_)

# list1 = [1,2]
# list2 = [3,4]
# a = sum(list1+list2)
# print(a)

# import random
# list1 = random.sample(10,1)
# list2 = random.sample(range(10,20))
# a = sum(list1 + list2)
# print(a)

# list1 = input().split(',')
# list1.sort()
# list_ = list1
# print(list_)

# list_ = [1,51,1]
# if list_[0]==list_[1] or list_[1]==list_[2] or list_[2]==list_[0]:
#     print('yes')
# else:
#     print('ERROR')

# list_ = list(range(55,9185,5))
# print(list_)

# a = {i ** 2 for i in range(10)}
# print(a)

# a = {i ** 2 for i in range(10)}
# print(len(a))

# a = {i ** 2 for i in range(10)}
# a.add('Hello world!')
# print(a)

# a = {i ** 2 for i in range(10)}
# b = {i ** 2 for i in range(15)}
# a.update(b)
# print(a)

# a = {i ** 2 for i in range(10)}
# a.discard(2)
# print(a)

# a = {i ** 2 for i in range(10)}
# a.remove(1)
# print(a)

# a = {i ** 2 for i in range(10)}
# a.clear()
# print(a)

# a = {i ** 2 for i in range(10)}
# b = {i ** 2 for i in range(15)}
# a.intersection(b)
# print(a)

# a = {i ** 2 for i in range(10)}
# b = {i ** 2 for i in range(15)}
# a.difference(b)
# print(a)

# a = {i ** 2 for i in range(10)}
# b = {i ** 2 for i in range(10)}
# a.union(b)
# print(a)

# a = {'world', 5, 'john'}
# b = {'world', 5, 'john'}
# if a.issubset(b):
#     print('Подмножество!')

# a = {i ** 2 for i in range(10)}
# b = {i ** 2 for i in range(10)}
# if a.issuperset(b):
#     print('Надмножество!')

# robert = {5, 7, 11, 10, 28}
# kail = {1, 5, 14, 8, 22}
# merri = {19, 20, 3, 11, 10}
# if robert.intersection(kail):
#     print('kail ')
# if robert.intersection(merri):
#     print('merri')

# tilek = {'Dodo','ImperiaPizza','FreshBox'}
# timur = {'OchakKebab','FreshBox'}
# alexandr = {'FreshBox','KFC'}
# elina = {'Dodo','ImperiaPizza','FreshBox','OchakKebab','KFC'}
# # print(tilek&timur&alexandr&elina)
# elina.intersection_update(tilek,timur,alexandr)
# print(elina)

# ingredients = {"cыр чеддар","грибы", "соус","шпинат"}
# ingredients.add("помидор")
# ingredients.discard("колбаса")
# ingredients.remove("шпинат")
# ingredients.add("базилик")
# ingredients.discard("сыр чеддар")
# ingredients.add("сыр моцарелла")
# print(ingredients)

# a = [set(), set(), set()]
# inp1 = input().split()
# inp2 = int(input())
# for i in range(len(a)):
#     if inp2 == i +1:
#         a[i].update(set(inp1))
#     else:
#         a[i].add('default value')
# print(a)

# import random
# a = sample.random(range(1, 6))
# b = sample.random(range(1, 6))
# a.pop()
# b.pop()
# a.intersection(b)
# print(a)

# a = {'x': 1, 'y': 2, 'z': 1}
# print([i for i in a.keys()][0])

# a = {'a': 1, 'b': 2, 'c': 1}
# remove_elem = a.pop('a')
# print({remove_elem})

# a = {'a': 1, 'b': 2, 'c': 1}
# a.update({'f': 55})
# print(a)


# a = {'a': 1, 'b': 2, 'c': 1}
# a.clear()
# print(a)

# a = {'a': 1, 'b': 2, 'c': 1}
# print([i for i in a.keys()])

# a = {'a': 1, 'b': 2, 'c': 1}
# b = a.copy()
# print(b)

# a = {'a': 1, 'b': 2, 'c':3}
# for k in a.keys():
#     print(k)

# a = {'a': 1, 'b': 2, 'c': 3}
# for v in a.values():
#     print(v)

# a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6}
# for k in a: 
#     if a[k] % 2 == 0:
#         a[k] = 2
# b = a.copy()
# print(b)

# a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# b = {k: v for k, v in a.items() if v is not None}
# a.clear()
# a.update(b)
# print(a)

# a = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
# a = {k:v/5 for k, v in a.items()}
# print(a)

# a = {'apple': 2, 'orange': 5, 'banana': 10}
# b = a.copy()
# for k, v in b.items():
#     if b[k] % 2 == 0:
#         del a[k]
# print(a)

# a = {'a': 1, 'b': 2, 'c': 3}
# b = {v:k for k,v in a.items()}
# print(b)

# a = {'a': 3, 'b': 2}
# print(sum(a.values()))

# a1 = {'abc1': 'a1', 'abc2': 'a2', 'abc3': 'a3'}
# print(a1)
# a2 = dict(abc1 = 'a1', abc2 = 'a2', abc3 = 'a3')
# print(a2)
# a3 = dict([("abc1", "a1"), ("abc2", "a2"), ("abc3", "a3")])
# print(a3)

# d = {'a': 10, 'b': 9, 'c': 3}
# result = 1
# for key in d:    
#     result = result * d[key]
# print(result)

# string = "pythonist"
# dict_ = {i: string.count(i) for i in string}
# print(dict_)

# #A)
# School =  {'5a':10,'5b':7,'5c':8,'6a':4,'6b':8,'6c':9,'7a':12,'7b':12,'7c':13,} 
# for i in range(5):
#     School.update( { input(f'Название класса № { i + 1 } : '): int(input(f'Количество учеников класса № { i + 1 } : ')) } )
# print(School)
# #B)
# ClassName = input('Введите класс: ')
# if ClassName in School:
#     print(f'Количество учеников в классе  { ClassName } :  { School[ClassName] } ')
# else:
#     print('Такого класса на существует')
# #C)
# for i in range(3):
#     School.update( { input(f'Название изменяемого класса  { i + 1 } : '): int(input(f'Количество учеников изменяемого класса  { i + 1 } : ')) } )
# print(School)
# #D)
# for i in range(2):
#     School.update( { input(f'Название нового класса  { i + 1 } : '): int(input(f'Количество учеников нового класса  { i + 1 } : ')) } )
# print(School)
# #E)
# del School[input(f'Название расформировываемого класса: ')]
# print(School)

# school =  {'5a':10,'5b':12,'6a':9,'6b':10,'6c':12,'7a':12,'8a':7,'8b':9,'9a':5,'9b':6,'9c':13,}
# school ['9a'] = 4
# school ['9b'] = 10
# school ['6a'] = 11
# school ['7b'] = 5
# school ['8c'] = 6
# del school ['9c']
# total = sum(school.values())
# print(total)

# list_ = [item for item in range(1, 101)] 
# print(list_)

# list_ = [item for item in range(1, 51,2)] 
# print(list_)

# 1
# list_ = [i for i in range(1, 101)]
# print(list_)

# 2
# list_ = [n for n in range(1, 51) if n % 2 == 1]
# print(list_)

# 3
# list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# int_list = [i for i in list_ if i>0 and i % 2 == 0]
# print(int_list)

# 4
# list_ = [i ** 2 for i in range(1,26)]
# print(list_)

# 5
# str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# int_list = [int(i) for i in str_list]
# print(int_list)

# 6
# list_ = [n if n % 2 == 1 else n ** 2 for n in range(1, 11)]
# print(list_)

# 7
# list_ = [True if i % 2 == 0 else False for i in range(1, 11)]
# print(list_)

# 8
# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ]
# new_list = ['shorter' if len(i) < 4 else 'longer' for i in list_name]
# print(new_list)

# 9
# dict_ = {k: k**2 for k in range(1,11)}
# print(dict_)

# 10
# n = int(input())
# dict_ = {k: k**2 for k in range(1,501) if k%n==0}
# print(dict_)


# a = {'a': 1, 'b': 5, 'c': 4, 'd': 3}
# dict_= {k: list(range(1,v+1)) for k,v in a.items()}
# print(dict_)


# dict_ = {'first': 1, 'second': 2, 'third': 3} 
# a = {k: 'even' if v % 2 == 0 else 'odd' for k,v in dict_.items()}
# print(a)

# string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
# words = string_.split()
# list_ = [number for number in words if not number.isalpha() ]
# print(list_)


# dict_ = {'Timur': {'history': 90, 'math': 95, 'literature': 91},
# 'Olga': {'history': 92, 'math': 96, 'literature': 81},
# 'Nik': {'history': 84, 'math': 85, 'literature': 87}}
# valuesList = list(dict_.values())
# valuesList  
# a = {key: "".join([key2 for key2, val2 in val.items() if val2 == max(val.values())]) for key, val in dict_.items()}
# print(a)

# my_dict = {'first': {'a': 1}, 'second': {'b': 2}} 
# vallist = list(my_dict.values())
# a = {key: ([val2 for val2 in val.values()]) for key, val in my_dict.items()}
# # a = {key: "".join([key2 for key2, val2 in val.items() if val2 == max(val.values())]) for key, val in my_dict.items()}
# print(a)

# cash = int(input())
# if cash < 0: 
#     raise ValueError ('Сумма не может быть отрицательной!')
# else:
#     print(cash)


# тернарный оператор данных
# это if else в одной строчке также работает для других
# num1 = 33
# num2 = 44
# result = num1 if num1>num2 else num2
# print(f'the highets value is {result}')

# if num1> num2:
#     result = num1
# else:
#     result = num2
# print(f'the highets value is {result}')

# i = 1
# while i < 6:
#     print(i)
#     i += 1

# i = 2
# while i < 7:
#     print(i)
#     if i == 3:
#         break
#     i += i

# i = 1
# while i < 9:
#     print(i)
#     i += 1
# else:
#     print('is not longer than 9')

# itterable object
# c = [1,2,3,4,5,6] #list
# c = {'a':1, 'b':2, 'c':3} #dict

# for i in c:
#     print(c[i])

# fruits = ['apple', 'banana', 'grapes']

# for i in fruits:
#     if i == 'banana':
#         continue
#     print(i)

# a = 4
# b = 5
# a = b
# print(a)

# моржовый оператор потому что похож на моржа :=
# print(a := 2 + 4)

    # while (value := input("enter something:") !=""):
    #     print("nice")

    # похожие только которое выше удобнее и красивее 
    # короче и экономит время

    # while True:
    #     x = input('enter smth')
    #     print('nice')
    #     if x== '':
    #         break


# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ]
# new_list = ['shorter' if len(i) < 4 else 'longer' for i in list_name]
# print(new_list)

# если только if else то он перед for
# если только if то он после for

# dict_ = {'Timur': {'h': 90, 'm': 95, 'l': 91},
# 'vlad': {'h': 93, 'm': 95, 'l': 98}}
# #,'Nik': {'h': 84, 'm': 85, 'l': 87}}

# dict_ = {k1:v2 for k1, v1 in dict_.items() for k2, v2 in v1.items() 
# if max(v1.values()) == v2}
# print(dict_)

# dict_ = {'first': {'a': 1}, 'second': {'b': 2}} 
# a = {key: ([val2 for val2 in val.values()]) for key, val in dict_.items()}
# # a = {key: "".join([key2 for key2, val2 in val.items() if val2 == max(val.values())]) for key, val in my_dict.items()}
# # print(a)

# val_ = {k1:v2 for k1, v1 in dict_.items() 
# for k2,v2 in v1.items()}
# print(val_)

# import random
# a = (random.randrange(0,10))
# while True:
#     num1 = input('guess the number')

#     if num1.lower() == 'exit':
#         print('game over')
#     elif int(a) > int(num1):
#         print('number is lower')
#     elif int(a) < int(num1):
#         print('number is bigger')
#     elif int(a) == int(num1):
#         print('congrulations you win\n type exit for quit game')

# ограничиить чтобы пользователь вводил только в диапазоне указаном в рандоме

# def add(num1,num2):
#     num1+num2
#     return add
# print(add)

# def get_string_length(str_):
#     return len(str_)
# print(get_string_length('hello'))


# def get_type(int_,str_):
#     print(type(int_))
#     print(type(str_))
#     return
# get_type(5, 's')

# def divide(st, nd):
#     return st/nd
# print(divide(2,4))

# Создайте переменную dict_ в котором будет хранится словарь.

# Затем создайте функцию

# def dictionary()

# которая принимает этот словарь. Пройдитесь по dict_ циклом и распечатайте все его ключи внутри функции.

# dict_ = {'i': 1, 'love':2, 'you':3}
# def dictionary(dict_):
#     for k in dict_:
#         print(k)
#     return
# dictionary(dict_)

# num = 7
# def check(num):
#     if num % 2 == 0:
#         return ("It is even number")
#     else:
#         return("It is odd number")
#     return 
# print(check(num))


# def is_palindrome(string):
#     string = string.replace(' ','').lower()
#     return True if string == string[::-1] else False
# print(is_palindrome('довод')) 

# def max_num(num1,num2):
#     return max(num1,num2)
# print(max_num(10, 12)) 

# def multiply_list(list_):
#     result = 1
#     for n in list_:
#         result = result*n
#     return result
# print(multiply_list([1, 2, 3, 4, 5, 6])) 

# def sum_digits(sum_):
#     return sum([int(i) for i in str(sum_)])
# print(sum_digits(105))

# function
# def foo():
#     var = 'переменная foo'
#     print("переменная в foo: ",var)
#     def bar():
#         global var
#         var = 'переменная bar'
#     bar()
# foo()
# print("переменная в foo: ", var)

# x = 'Я глобальная переменная!'
# print(x)
# def my_func():
#     global x
#     x = 'Я могу изменяться'
# my_func()
# print(x)
# print(globals())

# num = 3
# def mul():
#     global num
#     num =num * num
#     return num
# mul()
# mul()
# print(mul())

# num = 3
# def mul():
#     global num
#     num =num ** 2
# mul() 
# mul()
# mul()
# print(num)

# balance = 0
# def get_salary(amount):
#     global balance
#     balance = balance + amount
# def pay_bills(amount, log_name):
#     global balance
#     balance = balance - amount
#     print(f'Вы заплатили {amount} сом за {log_name}')
# def get_balance():
#     print(f'У вас на счету {balance} сом')
# get_salary(1000)
# get_balance()
# pay_bills(400, 'кабельное тв')
# get_balance()

# result = 0
# def pow_first(x,y):
#     global result
#     result = pow(x,y)
# def pow_second(z):
#     global result
#     result = result%z
# pow_first(2, 3)
# pow_second(3)
# print(result)


# a = {'Мурат': 24, 'Эржан': 21, 'Чынгыз': 24, 'Алтынай': 17, 'Асема': 16}
# for k, v in a.items():
#     if v >= 17:
#         print(f'{k}, Вы можете войти в клуб')
#     else:
#         print(f'{k}, извините, Вы не проходите по age-control')

# a = ['pipi', 'papa', 'mama']
# b = [x.capitalize() for x in a]
# print(b)

# def count_symbols(string):
#     gl = ['а','е','ё','и','о','у','ы','э','ю','я']
#     sl = ['б','в','г','д','ж','з','й','к','л','м','н','п','р','с','т','ф','х','ц','ч','ш','щ']
#     os = 0
#     gls = 0
#     sls = 0
#     for i in list(string.lower()):
#         if i in gl:
#             gls += 1
#         elif i in sl:
#             sls += 1
#         else:
#             os += 1
#     return f'Количество гласных: {gls}, согласных: {sls}, остальных символов: {os}'
# print(count_symbols('Мурат супер!'))

# a = []
# a = list(range(11))
# print(a)

# a = []
# def range_(a):
#     a = list(range(11))
#     return a
# print(range_(a))
# print(a)

# a = [1, 3, 4, 6, 8, 6, 8, 9, 0, 3]
# # a = [i for i in a if i<7]
# for i in a:
#     if i < 7:
#         print(i,end = '')
# print(a)

# from functools import reduce
# list_ = [1,2,3,4]  
# result = reduce(lambda x, y: x + y, list_)
# print(result)

# import functools
# list_ = [1,2,3,4]
# result = functools.reduce(lambda x, y: x + y, list_)
# print(result)

# list_ = [1,2,3,4]
# result = sum(list_)
# print(result)

# list_ = [1, 5, -9, 6, -4] 
# # list_ = [5, 8, 4, 6, 7] 
# result = all(i >= 3 for i in list_)
# print(result)

# list_ = [1, 5, -9, 6, -4] 
# list_ = [5, 8, 4, 6, 7] 
# result = any(i == -i for i in list_)
# print(result)

# list_ = [1, 2, 3, 4]
# result=list(map(lambda x: x ** 2, list_))
# print(result)

# list_ = [1, 2, 3, 4]
# result=list(filter(lambda x: x % 2== 0, list_))
# print(result)

# list_ = ['inheritance', 'solid', 'polymorphism', 'dry', 'yagni',]
# result = list(filter(lambda x: len(x)>7 ,list_))
# print(result)

# import functools
# list_ = [5, 6, 7, 8] 
# result = functools.reduce(lambda x,y: x*y  ,list_)
# print(result)

# list_ = [1,2,3,4,5,6,7,8,9]
# odd_count = len(list(filter(lambda x: (x%2 != 0) , list_)))
# even_count = len(list(filter(lambda x: (x%2 == 0) , list_)))
# result = (f'even: {even_count}, odd: {odd_count}')
# print(result)

# list_ = [-1, 2, 3, 5, -3, 7, ]
# list_ = [i for i in list_ if i<0]
# for i in list_:
#     if i <0:
#         print (True)
#     else:
#         print (False)

# list_ = [-1, 2, 3, 5, -3, 7, ] 
# result = list(map(lambda i:True if i>0 else False, list_))
# print(result)

# list_ = ['Paul', 'George', 'Ringo', 'John']
# import functools
# result = functools.reduce(lambda x, y: x if len(x) > len(y) else y, list_)
# print(result)

