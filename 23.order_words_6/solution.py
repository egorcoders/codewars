# my solution
def order(s: str):
    '''
    Задача 23. Сортировка слов в строке.
    '''
    dict = {}
    for i in s.split():
        dict[int(''.join(n for n in i if n.isdigit()))] = i

    ans = []
    for n in sorted(dict.keys()):
        ans.append(dict[n])

    return ' '.join(ans)


# best solution
def order2(words):
    return ' '.join(sorted(words.split(), key=lambda w: sorted(w)))
