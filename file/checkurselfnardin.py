# #     #task 1
# a = {'John':
# {'history': 90, 'math': 95, 'literature': 91}, 'Rose': {'history': 92, 'math': 96, 'literature':
# 81},
# 'Kelly': {'history': 84, 'math': 85, 'literature': 87}}
# result = {k1:{k2 for k2, v2 in  v1.items() if v2==max(v1.values())} for k1, v1 in a.items()}
# print(result)

#     #task 2
# c = int(input("Enter ur cash: "))
# if c > 0:
#     raise Exception ('сумма не должна быть отрицательной')

#     #task 3
# import functools
# list_ = [1,2,3,4]
# result = functools.reduce(lambda x,y: x + y, list_)
# print(result)

# # task 4
list_ = [1,2,3,4]
list_ = list(filter(lambda x: x%2==0, list_))
# result = [i for i in list_ if i%2==0]
# print(result)
print(list_)

