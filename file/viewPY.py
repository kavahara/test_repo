# 1. лист компрехеншиен, где должны быть такие данные:
# числа, которые делятся на 3 и на 5, в противном случае строка
# "неизвестно", д.б. в диапазоне чисел от 1 до 100
list_ = [i if i%3==0 or i % 5==0 else 'unknow' for i in range(1,101)]
print(list_)

# 2. дан словарь
# dct = {'hello':None, 'world':None, 'programmer':None}
# dct = {k: len(k) for k, v in dct.items()}
# print(dct)

# 3. нужно создать три функции, одна регистрирует пользователя
# вторая производит логин, третья является менеджером, который хранить в себе
# список пользователей и при обращение к этой функции проверяет зарегистрирован
# ли этот пользователь, если да то выводит сообщение,
# если нет то вызывает функцию регистрации

# login = {'password':'login'}

# bd = {'kava':456}
# def login(name, paswrd):
#     print(f'user, {name}! ur log in successfully')
# def registration(name, paswrd):
#     global bd
#     bd[name] = paswrd
#     print(f'list of users: {bd}')
# def bdm():
#     name = input('enter ur name')
#     paswrd = input('enter ur pswrd')
#     if name in bd:
#         login(name, paswrd)
#     else:
#         print('ur not registered')
#         registration(name, paswrd)
#         print('ur has been register')

# bdm()

# 4. дана БД, реализовать CRUD, при помощи фукнции
# C-create, R-read/retrive, U-update, D-delete

# db = {'john':23, 'jack':52, 'alex':23, 'tom':34}
# def create():
#     global db
#     name = input('enter name: ')
#     age = input('enter age: ')
#     if name in db:
#         print('users have')
#     else:
#         db [name] = age
#         print('user added')
#         print(f'list of users{db}')
# def read():
#     print(db)
#     print('if u want change call func update, or delete')
# def update():
#     global db
#     print('which user ages u want change')
#     print(db)
#     name = input('enter name')
#     if name in db:
#         age = input('enter age')
#         db [name] = age
#         print(db)
#     else:
#         print('name not find')
# def delete():
#     name = input('enter delete name')
#     if name in db:
#         db.pop(name)
#     else:
#         print('users {name} not find, pls enter really name')
# # create()
# # read()
# update()

