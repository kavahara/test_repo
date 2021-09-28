### def 
# функция именнованый блок кода выполняет 
# какое либо действие и возвращает нам что либо или не возвращает ничего

# def add_func(): #ключевое слово для функции надо называть 
# # так которое будет показывать ее действие
#     print(10+5)  # тело функции через табуляцию

# add_func()

# def add_nums(first, second): #задаем параметры # необязательно должна быть переменная
#     print(first+second) #принием аргумент 
#     # pass # пропустить чтобы в дальнейшем сделать с ней что либо

# def add_nums (num1, num2):
#     return num1 + num2
# result = add_nums(10,100)

# print(result)

# def hello(name, surname, age):
    # print(f'hello, {name} {surname}! you {age} years old')

# name, surname, age = input('enter ur name'), input('enter ur surname'), int(input('enter ur age'))
# hello(name,surname,age)

# позиционный аргумент нужно передавать аргументы в определенной позиции 
# именнованый аргумент можно передать аргумент указав "параметры=аргумент"
# всегда идет сперва позиционный аргумент потом именованный

# defaultные значение
# они ставятся после обязательных

# def hello(name, surname='unknow', age='unknow'):
#     print(f'hello, {name} {surname}! you {age} years old')

# hello(name='alex', surname='n', age=23)

# def func(*args): одна звездочка
# args позиционный аргумент название может быть какое угодно
# главное поставить звездочку*

# def func(**kwargs): две звездочки

# def func(*args, **kwargs): # необязательно называть так но по веб8,
#     print(f'this args {args}') # tuple неизменяемый итерируемый упорядочный, позиционный аргументы
#     print(f'this kwargs {kwargs}') # dict словари, именнованый аргумент

# func('hello', 'j', 1, 52, name='alex', surname='di', age='24')

# def add_func(num1, num2):
#     return num1 + num2

# def sub_func(num1, num2):
#     return num1 - num2

# def mult_func(num1, num2):
#     return num1 * num2

# def div_func(num1, num2):
#     return num1 / num2

# def handler(operation, num1, num2):
#     switcher = { 
#         '+':add_func(num1, num2),
#         '-': sub_func(num1, num2),
#         '*': mult_func(num1, num2),
#         '/': div_func(num1, num2)
#     }
#     return switcher[operation]

# num1 = int(input('enter 1st num:'))
# operation = input('choose from: "+", "-", "*", "/" ')
# num2 = int(input('enter 2nd num:'))
# result = handler(operation, num1, num2)

# print(result)

# string = input('enter str').lower()
# def translat_str(string):
#     intab = "qwertyuiop[]asdfghjkl;'zxcvbnm,."
#     outtab  = "йцукенгшщзхъфывапролджэячсмитьбю"
#     # print(len(intab) == len(outtab))
#     transtab = str.maketrans(intab, outtab)
#     return string.translate(transtab)

# result = translat_str(string)

# print(result)

# def get_string_length(string):
#     return len(string)
# # print(get_string_length(lkanskjfna))
# print(get_string_length('naisf'))