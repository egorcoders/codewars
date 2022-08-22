# my solution
def square_number(n: int):
    '''
    Задача 2.
    
    Вычисление квадратного корня числа.
    '''
    if not isinstance(n, int):
        return 'Число n не целое.'
    elif n < 0:
        return 'Число n не положительное.'
    elif (n ** 0.5).is_integer():
        return int(n ** 0.5)
    return None
