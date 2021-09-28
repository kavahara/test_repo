# [] внутри списка может быть список, также имеет индекс

# fst = [ 'hello', 2, ['jon','hiaf'] ] 
# один проход цикла называется интерация
# for i in fst:
#     print (i)

# fst = [1,2,3[5,25]] 
# for i in fst:
#     if 
#     for j in i:
#         print(f'элемент второго списка{j}')
#     print (i)

# a = 'hello'
# b = 150
# for i in b:
#     print(i)

# name1 = input('enter ur name with space: ').lower().split()
# guest = input('enter ur name: ').lower()
# if guest in name1:
#     print('secess!')
# else:
#     print('error!')


# print('a' in 'kajgbska')


# lst_of_frnds = ['alex', 'tom', 'sam', 'michael', 'kis']

# ' welcome to party, name'/

# for friend in lst_of_frnds:
#     print (f'welcome to party, {friend}!')

# for i in lst_of_frnds:
#     for j in i:
#         print(j)


# method of list
# list.append(x) добавляет элемент в конец списка

# .append добавляет в список данные
# lst = ['somedata1', 'somedata2']
# new_data = input('enter simething:')
# lst.append(new_data)
# print(lst)\

# list.extend(L) расширяет список list, добавляя в конец все 
# элементы списка L

# lst1  = ['somedata1', 'somedata2']
# lst2 = ['somedata3', 'somedata4']
# lst1.extend(lst2)
# print(lst1)


# lst1  = ['somedata1', 'somedata2']
# # lst1.insert(i,x ) добавляет елемент по индексу
# lst1.insert(0, 'some data3')
# print(lst1)

# list.remove(x) удаляет первое вхождение,
# в противном случае ошибка vallueError

# lst = ['h','e','l','l','o']
# lst.remove('h')
# print(lst)
# lst.remove('l')
# print(lst)


# list.pop ([i]) удаляет элемент по индексу и возвращает его

# lst = ['h','e','l','l','o']
# lst.pop(1)
# print (lst)
# removed_elem = lst.pop(1)
# print (removed_elem)


# list.index(x, [start [,end]]) возвращает индекс элемента
# lst = ['h', 'e', 2, 4, 'f','k', 'l']
# print(lst.index('k', 3, 6))

# lst.count () подсчет элемента
# lst = ['h', 'e,', 'l', 'l', 'o']
# print(lst.count('e'))

# lst.sort ([key=функция]) сортировка
# lst = [1,6,5,4,9,2,3]
# lst.sort()
# print(lst)

# list.reverse() разворачивает список

# lst = ['h', 'e,', 'l', 'l', 'o']
# lst.reverse()
# print(lst)

# list.clear() очищает список

# lst = ['h', 'e,', 'l', 'l', 'o']
# lst.clear
# print(lst)

# list.copy () копия списка

# lst1 = ['h', 'e,', 'l', 'l', 'o']
# lst2 = lst1.copy()
# print(lst2)

# for i in lst:
#     if 
#     for j in i:
#         print(f'элемент второго списка{j}')
#     print (i)

#     дан список
#     # lst=[1,2,4,'hello', [1,'data',5]]
#     задача пеоебрать список циклом и если это элемент первого
#     списка вывести сообщение типа это элемент 1го списка
#     если второго то это эл-т 2го списка

# домашка

# lst=[1,2,4,'hello', [1,'data',5]]
# for i in lst:
#     print(f'элемент{i}')
# for i in lst:
#     print(f'элемент{i}')
        
#         print('int_')
#                 print('str_')
# if isinstance(lst, (int,str)):
#     print(lst)
# for a in lst:
#     print(isinstance(lst,list))
# for i in lst:
#     print(f'элемент первого списка{i}')
#     for j in i:
#         print(f'элемент второго списка{j}')
