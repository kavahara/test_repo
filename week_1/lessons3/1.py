# print('Hello \n' * 5)
# a = 'Hello'
# print(len(a))
# 'Hello'
# 0 1 2 3 4
# print (a[2])
# print (a[2])
# индексация слова s='kava' то есть s='0 1 2 3' or s='-4 -3 -2 -1'
# 's'[start, stop, step] откуда начинается,где заканчивается, шаг
# если ставить минус то будет с конца -3,-1 
# указывать надо с большего на меньший минус

# method str
# some_data = input('Enter some string: ')
# some_data = 'HEllllloooooo'
# замена символа по шаблону replace
# some_data.replace(шаблон, замена, макс. кол замен)
# print( some_data.replace('E', '$'))

# split() разделитель
# some_data = 'avadakedavra'
# print(some_data.split('a')) любое значение для разделителя
# по умолчание метод сплит делит по пробелу

# список через квадратные скобки 
# строка через кавычки

# a= 'hello'
# print(a.upper())
# print(a.lower())

# print(a.capitalize())
# print(a.count('e', 0, 5)) requir, option


# a= 'hello'
# print(a.swapcase()) меняет местами верхний и нижний регистр
# print(a.title()) первую букву каждого слово превращает в верхний регистр,
# реагирует на запятую, пробелы, точку, дефис, число
# print(a.zfill (15)) метод при котором нужно ввести столько цифр если нет
# покажет ноль
# a= 'hello'
# print(a.strip()) удаляет пробелы по краям
# print(a.lstrip()) удаляет пробелы слева a.rstrip удаляет справа пробелы
# можно задать букву которую нужно удалить по бокам через метод стрип

# a= 'hello'
# print(a.islower()) is это true or false в данном примере
# показывает состоит ли слово из нижнего регистра