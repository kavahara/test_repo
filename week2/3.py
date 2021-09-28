# a = {'hello', 1, 2}
# print(type(a))
# print(a)
# for i in a:
#     print(i)

# lst = ['765','877','987','765','657','877']
# a = set(lst)
# lst = list(a)
# print(a)

# a = set() пустой set
# a = set{} пустой dictionary

# операция над множеством
# a = {'hello', 1, 2}
# print(len(a))

# a = {'hello', 1, 2}
# print('hello' in a)

# set.isdisjoint(other) true if not have общего
# a = {'hello', 1, 2}
# b = {'world', 5, 'john'}
# print(a.isdisjoint(b))

# set == other похожи ли множества сета, сравнивает
# a = {'hello', 1, 2}
# b = {'world', 5, 'john'}
# print(a == b)

# set.issubset(other) является ли set подset база.сравни(другое множ-во)
# возвращает true если множ-во b явл подмнож-ом a 
# a = {'world', 5, 'john','tom'}
# b = {'world', 5, 'john'}
# print(b.issubset(a))
# print(b<=a) аналог issubset

# set.issuperset(other) есть ли элементы множества в другом множестве
# возвращает true если множ-во a явл надмнож-ом b
# a = {'world', 5, 'john','tom'}
# b = {'world', 5, 'john'}
# print(a.issuperset(b))
# print(a>=b) аналог set.issuperset

# set.union(other, ...) объединяет множества
# a = {'world', 5, 'john','tom'}
# b = {'world', 5, 'john'}
# c = {15 ,'jack'}
# print(b.union(c))
# print(a|c) аналог set.union

# set.intersection (other, ...) пересечение одноого или нескольких множества
# a = {'world', 5, 'john','tom'}
# b = {'world', 5, 'john'}
# c = {15 ,'jack'}
# print(b.intersection(a))
# print(b & c) аналог set.intersection

# set.difference(other, ...) разница между множ-ми
# a = {'world', 5, 'john','tom'}
# b = {'world', 5, 'john'}
# c = {15 ,'jack'}
# print(b.difference(c))
# print(b - c) аналог set.difference

# set.symmetric_difference(other, ...) показывает те элементы которых нет во множествах,
# игнорирует похожие значения
# a = {'world', 5, 'john','tom'}
# b = {'hello', 5, 'thanks', 7}
# c = {15 ,'jack','tom'}
# print(b.symmetric_difference(c))
# print(b ^ c) аналог set.symmetric_difference
# print(b^c^a)

# set.copy() копирования множества
# a = {'world', 5, 'john','tom'}
# b = a.copy()
# print(b)

# операции изменяющие множества

# set.update(other, ...)
# a = {'world', 5, 'john','tom'}
# b = {'hello', 5, 'thanks', 7}
# a.update({'hello'}) добавляет целое
# a.update('hello') добавляет каждый символ если нет литералов {}
# a.update(b) обновляет множество a не меняя b
# print(a)
# print(b |= a) аналог set.update()
# print(b)

# set.intersection_update обновляет пересекаемые значения множества
# a = {'world', 5, 'john','tom'}
# b = {'hello', 5, 'thanks', 7}
# c = {10,52}
# a.intersection_update(b)
# print(a)
# b &= c аналог set.intersection_update

# set.difference_update обновление разницы множества
# a = {'world', 5, 'john','tom'}
# b = {'hello', 5, 'thanks', 7}
# c = {10,52}
# a.difference_update(b, c)
# b -= c аналог set.difference_update
# print(a)

# set.symmetric_difference_update обновление не уникальных
# значений множества
# a = {'world', 5, 'john','tom'}
# b = {'hello', 5, 'thanks', 7}
# c = {10,52}
# b.symmetric_difference_update(c)
# b ^= c аналог set.symmetric_difference_update
# print(b)

# set.add(elem) добавления в множества
# b = {5,7, 'hello'}
# b.add('Hello')
# print(b)

# set.remove(elem) удаляет элемент из множества если он есть,
# если нет то выдаст ошибку
# b = {5,6,'hello'}
# b.remove(5)
# print(b)

# set.discard(elem) удаляет если есть такой элем,
# если нет то не выдает ошибку
# b = {5,6,'hello'}
# b.discard(5)
# print(b)

# set.pop() удаляет случайно
# b = {5,6,'hello'}
# b.pop()
# print(b)

# set.clear() очистка множ-ва
# b = {5,6,'hello'}
# b.clear()
# print(b)


# name_of_list = list('hello')
# a=str(name_of_list)
# new_list = (a[(len(a) + 1) // 2:] + a[:(len(a) + 1) // 2])
# # for i in new_list:
# #     print(i)
# print(new_list)