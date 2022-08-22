# my solution
def string_to_tuple(s: str):
    '''
    Задача 1.
    
    Преобразование наиболее частого символа в кортеж.
    '''
    if not s:
        return 'Строка пустая.'
    elif not s.isalpha():
        return 'Строка содержит недопустимые символы.'
    else:
        lst = list(s.lower())
        a = max(set(lst), key=lst.count)
        return (a, lst.count(a))
