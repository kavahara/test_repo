# try except 
# try попробуй какое либо условие 
# если будет ошибка то сделай то что написано в except
# то есть пропусти ошибку и сделай след действие

# print(10/0)
# print(1+"1")

# print()

# try:
#     a = "Azamat" #(logic expression)
# except NameError:
#     print(a)

# try:
#     num1 = 1
#     num2 = 0
#     print(num1 / num2)
# except ZeroDivisionError:
#     print("На ноль делить нельзя")

# IndentationError это ошибка отступа в какой либо команде

# try:
#     a = int(input("enter num: "))
#     b = input("enter something")
#     print(a + b)
# except TypeError:
#     print("ok")
# except ZeroDivisionError:
#     print("ok2")


# TypeError ошибка при различных типов
# for example when str + int or str + bool

# ZeroDivisionError ошибка при которой значение будет равняться нулю

# OSError ошибка оперативной памяти

# try:
#     a = int(input("enter num: "))
#     b = int(input("enter something"))
#     print(a + b)
# except TypeError, ZeroDivisionError, OSError:
#     print("ok")

# finally команда которая будет работать 
# если даже другие не сработали

# except если ничего не написать то он будет ловить все возможные ошибки
# но по рекомендации web8 надо указывать какую именно ошибка нам нужна

# try:
#     num1 = int(input("enter the first num: "))
#     num2 = int(input("enter the second num: "))
#     num1 / num2
# except ValueError:
#     print("enter only intagers")
#     raise NameError
# except ZeroDivisionError:
#     print("you cant divide by zero")
# else:
#     print("succesfully divided")
# finally:
#     print("worked")

# try:
#     num1 = int(input("enter 1st num"))
#     operations = input("choose one form: '+', '-', '*', '/'.")
#     num2 = int(input("enter 2nd num"))
#     operations_dict = {'-': num1 - num2, '+': num1 + num2, '/': num1 / num2, '*': num1 * num2}
#     print(operations_dict[operations])
# except ArithmeticError:
#     print('arithmetic error occured')
# else:
#     print('congrulation u can do it')
# finally:
#     print('if you want try again this shit')


# a = ('makers', )
# print(type(a))

# a = ('a', 1, [1,2], 'a', {'a'})
# print(a.count('a'))

# b = {1,2,3,4,3,4}
# print(b.index(3))
# print(b)

# tuple have 2 value index and count

