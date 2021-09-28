# range([start], stop, [step])
# for i in range(1, 51):
#     print(i)

# 1 способ
# list_ = list(range(1, 101))
# print(list_)

# 2 способ
# lst_2 = []
# for i in range(1,101):
#     lst_2.append(i)
# print(lst_2)

# 3 способ
# new_list = [expression for item in iterable if condition == True]
# lst_3 = [i for i in range(1,101)]
# print(lst_3)

# пример lsit comprehension
# lst = ['apple','potato','banana','tomato']
# lst = [i for i in lst if i != 'potato']
# print(lst)

# lst = ['apple','potato','banana','tomato']
# lst = [i for i in lst if i !='tomato' and i !='banana']
# print(lst)

# num_lst = list(range(1,21))
# print(num_lst)

# str_lst = ['четное' if i%2 == 0 else 'нечетное' for i in num_lst]
# print(str_lst)

# num_lst2 = [2 if i == 'четное' else 1 for i in str_lst]
# print(num_lst2)

# lst_odd = [i for i in num_lst if not i%2 == 0]
# print(lst_odd)

# lst = ['mike', 'john', 'woddu', 'jackson']
# lst = ['name ' + i.upper() for i in lst ]
# print(lst)

# dict coprehension
# dct = {k: k ** 2 for k in range(6)}
# print(dct)

# dct = {x ** 2: x ** 3 for x in range(11)}
# print(dct)

# dct = {1:None, 2:None, 3:None, 4:None, 5:None}
# dct = {k: 'четное' if k % 2 == 0 else 'нечетное' for k,v in dct.items()}
# print(dct)

# lst = ['apple', 'vabank', 'tomato', 'scam', 'k']
# dct = {k: len(k) for k in lst if len(k) > 5}
# print(dct)

# import random
# name_list = ['vaivi', 'kava', 'aleksandr', 'morty','rick']
# rndm_num = random.sample(range(1, 10), len(name_list))
# gues_order_stack = {name_list[i]: rndm_num[i] for i in range(len(name_list))}
# print(gues_order_stack)

# при помощи цикла сделать так чтобы был такой результат
# список чтобы из списка нашел самое маленькое значение и написал готово
# потом взял новый список и также нашел малькое значение и написал готово
# пока все ключи не будут готовы


# import random
# lst = ['vaivi', 'kava', 'aleksandr', 'morty','rick']
# rndm = random.sample(range(1, 10), len(lst))
# gords = {lst[i]: rndm[i] for i in range(len(lst))}
# # print(gords)
# gordl = len(gords)
# gorstv = list(gords.values())
# while gordl>0:
#     for key, value in gords.items():
#         if (type(value) == int):
#             if value == min(gorstv):
#                 gords[key] = 'готово!'
#                 print(gords)
#                 gorstv.remove(min(gorstv))
#         else:
#             pass
#     gordl -= 1
