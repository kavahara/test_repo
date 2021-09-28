books = {'financial':'theodor draiser', 'rich dad,poor dad':'robert kiosaki', 'think and get rich':'napoleon hill'}
readers = {}
def get_info():
    print(f'Списко книг на данный момент: {books}')
    print(f'Сейчас читают книги{readers}')
    return 'its all'

# def namebook():


def manager():
    print(get_info())
    tb = 'Взять'
    gb = 'Вернуть'
    tagb = input(f'Вы хотите {tb} или {gb} книгу?')
    if tagb == 'взять':
        name_book = input('Введите название книги:')
        name_reader = input('Введите ваше имя:')
        global books
        global readers
        truenb = (k for k in books.keys() if name_book == k)
        if truenb in books:
            global readers
            readers = {name_reader: {truenb:v for truenb,v in books.items} }
        print(readers)
    # elif tagb == 'вернуть':
    #     name_book = input(f'Какую книгу вы хотите {gb}?')
    #     print(name_book)
    else:
        print('Введите "взять" или "вернуть"!')

manager()