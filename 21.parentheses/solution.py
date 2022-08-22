# my solution
def parentheses_order(s: str) -> bool:
    '''
    Задача 3.
    
    Проверка симметрии скобочной последовательности.
    '''
    while True:
        if '()' in s:
            s = s.replace('()', '')
        else:
            return not s

print(parentheses_order('(())'))
