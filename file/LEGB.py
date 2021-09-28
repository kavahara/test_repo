# LEGB - local Enclosed Global Built
# global and local variable 
# x = 'this global variable'

# def some_func():
#     x = 'this local variable'
#     print(x)

# print(x)


# enclosed variable
# def some_func():
#     x = 'this enclosed variable'
#     # print(x)
#     def some_func2():
#         x = 'this local variable'
#         print(x)
#     return some_func2()

# print(some_func())

# встроенные функции
# locals() globals() эти функции возвращают словари

# x = 'some data'
# def func():
#     pass
# print(globals()) # показывает что находится на глобальном уровне

# print(x is globals()['x']) # если это словарь значит можно обратиться к нему 
# обращаемся и спрашиваем является ли Х глобальной переменной
# можно делать все тоже самое что и со словарем

# globals()['new key'] = 'hello world'
# print(globals())

# можно использовать если например код слишком большой
# чтобы увидеть какие есть переменные, чтобы не терять время листая
# показывает не упорядочно не стоит ориентироватся на порядок

# locals
# def some_func():
#     some_str = 'hello'
#     locals()['num'] = 525
#     print(locals())
#     def func():
#         print(locals())
#     return func()

# some_func()

# def func():
#     print(globals())

# func()

#    # global nonlocal

# x = 0
# def counter():
#     x = 1
#     return x

# print(counter())

# counter()
# print(x)


# x = 0
# def counter():
#     global x
#     x += 1
#     print(x)

# counter()
# counter()
# counter()
# counter()
# counter()
# counter()
# print(f'это значение глобальной переменной {x}')

#  # nonlocal
# x = 100

# def f():
#     x = 20
#     def g():
#         nonlocal x
#         x = 40
#     g()
#     print(x)
# f()


# def some_func():
#     x = 100
#     z = 'hello'
#     return
#     # return она читает как верни заверши
#     print(f'{x}{z}')
# some_func() # после return работать не будет(с принтом будет)

# поиск идет по принципу слева на право(снизу вверх) local>enclosed>global>built-in

# def type(x):
#     return 'hello kava'

# x = 100
# print(type(x))
# видит команду которая находится рядом то есть выше этой самой команды
# если он находится ниже не прочитает и обратится к встроенной функции которая выше

# global нужно для того чтобы обратиться к глобальной
# и изменить его потому что с локальной не указав глобал нельзя изменить

# nonlocal нужно для того чтобы обратиться к переменной которая выше(т.е. родительский)
# на один уровень выше

