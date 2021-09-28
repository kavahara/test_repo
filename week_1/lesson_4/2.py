# while (истина) бесконечный цикл

# while True:
#     print('Hello')

# counter = 0
# while True:
#     counter += 1
#     print(counter)

# counter = 0
# while counter < 10:
#     print(f'сейчас число {counter}')
#     counter += 1

# calcul

# num_1 = int(input('enter 1st num'))
# symbol_operation = input('choice from "+,-,/,*":')
# num_2 = int(input('enter 2nd num'))

# if symbol_operation == '+':
#     print(num_1 + num_2)
# elif symbol_operation == '-':
#     print(num_1 - num_2)
# elif symbol_operation == '/':
#     print(num_1 / num_2)
# elif symbol_operation == '*':
#     print(num_1 * num_2)
# else:
#     print('error')

# while True:
#     pass

# play = True
# while play:
#     num_1 = int(input('enter 1st num'))
#     symbol_operation = input('choice from "+,-,/,*":')
#     num_2 = int(input('enter 2nd num'))
    
#     if symbol_operation == '+':
#         print(num_1 + num_2)
#     elif symbol_operation == '-':
#         print(num_1 - num_2)
#     elif symbol_operation == '/':
#         print(num_1 / num_2)
#     elif symbol_operation == '*':
#         print(num_1 * num_2)
#     else:
#         print('error')

#     one_time = input('do you want continue? "yes" or "not":')
#     if one_time.lower() == 'yes':
#         pass
#     elif one_time.lower() == 'not':
#         play = False
#         print('see you!')
#     else:
#         print('try again')


# continue - начинает след шаг
# for i in 'hello world':
#     if i == 'o':
#         continue
#     print(i*2)


# oper break досрочно прерывает цикл
# for i in 'hello world':
#     if i == 'o':
#         break
#     print (i*2)

# a = 'helllo'
# a_len = len(a)
# while a_len > 0:
#     if a[a_len - 1] == 'o':
#         a_len -= 1
#         continue
#     print(a[a_len - 1])
#     a_len -= 1


# else 

# for i in 'helloo woolrd':
#     if i == 'i':
#         break
# else: print('not')