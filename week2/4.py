# {} пустой dictionary
# {key:value, key:value, ...} key должны быть уникальными и неизменяемы
# value может быть любое
# dct = {}
# print(type(dct))

# dct = {'name':'john', 'age':25, 'hobby': ['fishing','footbal','auto']}
# print(dct['age'])
# print(dct['hobby'][1])

# методы словарей
# dict.clear() - очищение
# dct = {'name':'john', 'age':25, 'hobby': ['fishing','footbal','auto']}
# dct.clear()
# print(dct)

# dict.copy() - копирование словаря
# dct = {'name':'john', 'age':25, 'hobby': ['fishing','footbal','auto']}
# dct1 = dct.copy()
# print(dct)

# dict.fromkeys(seq[,value]) создает словарь
# с ключами из q значениями value по умолчанию None
# dct = {'name':'john', 'age':25, 'hobby': ['fishing','footbal','auto']}
# lst = ['name', 'age', 'hobby']
# dct = dict.fromkeys(lst, 'данных нет')
# print(dct)

# dcit.get(key, [default]) возвращает значение по ключу
# если такого нет по стандарту выдает None
# dct = {'name':'john', 'age':25, 'hobby': ['fishing','footbal','auto']}
# print(dct.get('name', 'no element dict'))

# dict.items() возвращает список из кортежей
# ключ - значение
# dct = {'name':'john', 'age':25, 'hobby': ['fishing','footbal','auto']}
# lst = list(dct.items())
# print(dct.items())

# dict.keys() возвращает список из ключей
# dct = {'name':'john', 'age':25, 'hobby': ['fishing','footbal','auto']}
# print(dct.keys())

# dict.values() - возвращает список из значений
# dct = {'name':'john', 'age':25, 'hobby': ['fishing','footbal','auto']}
# print(dct.values())

# dict.pop(key, [default]) удаляет элемент по ключу,
# если нет default то ошибка
# dct = {'name':'john', 'age':25, 'hobby': ['fishing','footbal','auto']}
# remove_elem = dct.pop('age')
# print(f'this deleted elem {remove_elem}\n this dict {dct}')

# dct = {'name':'john', 'age':25, 'hobby': ['fishing','footbal','auto']}
# remove_elem = dct.pop('surname', 'net takogo key')
# print(f'this deleted elem {remove_elem}\n this dict {dct}')

# dict.popitem() - удаляет рандомную пару ключ-значение
# dct = {'name':'john', 'age':25, 'hobby': ['fishing','footbal','auto']}
# remove_elem = dct.popitem()
# print(remove_elem)

# dict.setdefault(key, [default]) возвращает знач по ключу,
# если такого нет, то создаст со значением None
# dct = {'name':'john', 'age':25, 'hobby': ['fishing','footbal','auto']}
# elem = dct.setdefault('name')
# elem = dct.setdefault('surname', 'jackson')
# print(f'это значение {elem}, а это сам словарь {dct}')

# dict.update([other]) update dict другим dict
# dct = {'name':'john', 'age':25 }
# dct.update({'surname': 'jackson'})
# print(dct)

# cicle in dict 
# dct = {'name':'john', 'age':25, 'surnname':'jackson'}
# for k, v in dct.items():
#     print(f'this key {k}, this value {v}')

# for k in dct.keys():
#     print(k)

# for v in dct.values():
#     print(v)

# dct = {'name':'john', 'age':25, 'surnname':'jackson'}
# lst_k = []
# lst_v = []

# for k, v in dct.items():
#     lst_k.append(k)
#     lst_v.append(v)
# print(lst_k, lst_v)

# tuple кортеж неизменяемый упорядоченный итерируемый тип данных
# хранит любые типы данных
# tpl = tuple()
# tpl1 = ()

# tpl = ('hellp', [1,2])
# tpl[1].append('3')
# print(tpl)

# index(),count()
# tpl = ('hello', 'world', 1, 2)
# print(tpl.count('hello'))
# print(tpl.index('world'))

# frozenset неизменяемый в отличие от set и не имеет методов
# st = {'hello', 1, 2, 'world'}
# fst = frozenset(st.copy())
# print(fst)

# list1 = input().split(',')
# list1.sort()
# list_ = list1
# print(list_)
