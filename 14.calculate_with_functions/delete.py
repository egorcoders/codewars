# def calculate(operations, n):
#     if not operations:
#         return n
#     if operations['sign'] == '-':
#         return n - operations['value']


# five = lambda operations=None : calculate(operations, 5)
# seven = lambda operations=None : calculate(operations, 7)


# get_operation = lambda operation, x: {'sign': operation, 'value': x}
# minus = lambda x: get_operation('-', x)

# seven = lambda operations=None : calculate(operations, 7)


# def calculate(operations, n):
#     if not operations:
#         return n
#     if operations['sign'] == '-':
#         return n - operations['value']


# def seven(operations=None):
#     return calculate(operations, 7)


# def five(operations=None):
#     return calculate(operations, 5)


# def get_operation(operation, x):
#     return {
#         'sign': operation,
#         'value': x
#     }


# def minus(x):
#     return get_operation('-', x)





def calculate(operation, n):
    if not operation:
        return n
    if operation['symbol'] == '+':
        return n + operation['number']


def seven(operation=None):
    return calculate(operation, 7)


def get_operation(symbol, n):
    return {
        'symbol': symbol,
        'number': n,
    }


def plus(n):
    return get_operation('+', n)


print(seven(plus(seven())))
