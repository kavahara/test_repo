# встроенная функция
# map lamda zip filter
# функия высшего порядка

# lambda это анонимная функция которая имеет краткую запись

# def add_nums(a, b):
#     return a+b
# result = add_nums(10, 5)
# print(result)

# lambda тоже функция которая не имеет имя но можно поместить в переменную
#  после : в lambda это return
#  с помощью переменной в которую помещена lambda можно вызывать несколько раз
# а так она на один раз

# result = lambda a, b: a + b
# print(result(10,2))
# print(type(result))

# map
# нужна для того чтобы применить для итерируемого обькта
# map под капотом это цикл

# lst = [1,2,3,4,5]
# lst_new = []
# for i in lst:
#     lst_new.append(str(i))
# print(lst_new)


# lst = [1,2,3,4,5]
# lst_new = [str(i) for i in lst]
# print(lst_new)

# # map(function, iterables_obj)
# lst = [1,2,3,4,5]
# # lst_new = list(map(lambda i: str(i), lst))
# def num_to_str(i): 
#     return str(i)
# lst_new = list(map(num_to_str, lst)) 
# # тоже самое что с lambda отличе в 
# # том что lambda одноразовая
# print(lst_new)

# filter
#  просто фильтрует выдает True или False при заданом условии

# # filter(function, iter_obj)
# # lst = [i for i in range(1,11)]
# lst = list(range(1,11))
# # print(lst)
# new_list = list(filter(lambda i: i % 3 == 0, lst))
# print(new_list)

# reduce()
# для суммирования или вычитания чисел в списке

# func, iterable_obj

# from functools import reduce
# lst = [1,2,3,4,5]
# def func(x, y):
#     return x**y
# # result = reduce(lambda x, y: x + y, lst)
# result = reduce(func, lst)
# print(result)

# print(pow(3,2))

# # # zip()
# # функция для обьединения данных
# employers_numbers  = [2,9,18,28]
# employers_name = ['john', 'kila', 'rick', 'morty']
# employers_sphere = ['it', 'broker', 'cook', 'bank']
# zipped_values = zip(employers_numbers, employers_name, employers_sphere)
# # print(zipped_values)
# zipeed_list = list(zipped_values)
# print(zipeed_list)
