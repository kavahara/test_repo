# список книг {назв.книги: автор}
# books = {'Financial': 'Theodor Draiser',
#  'Rich dad, poor dad': 'Robert Kiyosaki',
#  'Think and get rich': 'Napoleon Hill'}

# список читателей {имя: {назв.книги: автор}}
#  {'Alex': {'Financial': 'Theodor Draiser'}} 

# функция, которая выводит информацию о книгах 
# которые есть и о читателях
# На данный момент список читателей такой: 
#  {'Alex': {'Financial': 'Theodor Draiser'}} 
#  Список книг такой: 
#  {'Rich dad, poor dad': 'Robert Kiyosaki', 'Think and get rich': 'Napoleon Hill'}

# функцмя, которая регистрирует читателя и выдает книгу
# Какую книгу вы хотите получить? Выберите из
#  {'Financial': 'Theodor Draiser', 'Rich dad, poor dad': 'Robert Kiyosaki', 'Think and get rich': 'Napoleon Hill'}
#  Введите только название: Financial
# Введите ваше имя: Alex
# Ваша заявка успешно оформлена!

# функция, которая возвращает книгу
# Вы хотите взять книгу либо вернуть? Введите "взять" или "вернуть": вернуть
# Введите имя: Alex
# Вы хотите вернуть: {'Financial': 'Theodor Draiser'}? да/нет: да
# Книга успешно возвращена!

# функция менеджер, которая распределяет 
# вызов других функций

# на моменте когда добавляешь две книги

# books = {'financial': 'theodor draiser', 'rich dad, poor dad': 'robert kiyosaki', 'think and get rich': 'napoleon hill'}

books = {'one':'oone', 'two':'twoo', 'three':'threee', 'o':'oo', 'a':'aa'}
readers = {}

def get_info(): # информация о readers
    # print(f'Список книг на данный момент: {books}')
    print(f'Сейчас читают книги{readers}')
    tarb()
    return 'its all'
def registation(): # добавляет пользователя в readers
    global books
    global readers
    namebook = input('Введите только название книги!').lower()
    if namebook in books:
        name = input('Введите ваше имя').lower()
        if name in readers:
            readers[name].update({namebook:books[namebook]})
            books.pop(namebook)
        else:
            readers[name] = {namebook:books[namebook]}
            books.pop(namebook) 
            print('wrong something')
        # readers.update({k: v for k, v in books.items() if namebook == k })
        print(f'Книга взята под именем {name}')
    else:
        print('{name} название книги не найдено введите реальное название!!!')
def delete(): # удаляет пользователя
    global readers
    global books
    name = input('Чтобы вернуть книгу введите ваше имя').lower()
    if name in readers:
        books.update(readers[name])
        readers.pop(name)
        print('книга успешно возвращена!')
    else:
        print('Введеное имя не найдено! ')
def add_(): # добавляет книгу
    global books
    author = input('Введите имя автора: ')
    namebk = input('Введите книгу автора: ')
    books[namebk] = author
def del_(): # удаляет книгу
    global books
    namebkk = input('Введите название книги котору хотите удалить:')
    books.pop(namebkk)
def addbook(): #добавляет книги используя add_ and del_
    namenewbook = input('Вы хотите add или del?').lower()
    if namenewbook == 'add':
        add_()
    elif namenewbook == 'del':
        del_()
def tarb(): # manager
    print(f'Список книг: {books}')
    tanr = input('Вы хотите take или return книгу? Или вы хотите change библеотеку?').lower()
    if tanr == 'take':
        registation()
    elif tanr == 'return':
        delete()
    elif tanr == 'change':
        addbook()
    else:
        print('Введите только take, return или change!')
    get_info()
# registation()
# delete()
tarb()