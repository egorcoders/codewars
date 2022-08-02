# my solution


# best solution
# 1
def calculate(operation, n):
    if not operation:
        return n
    if operation['symbol'] == '+':
        return n + operation['number']
    elif operation['symbol'] == '-':
        return n - operation['number']
    elif operation['symbol'] == '*':
        return n * operation['number']
    elif operation['symbol'] == '/':
        return n // operation['number']


def zero(operation=None):
    return calculate(operation, 0)


def one(operation=None):
    return calculate(operation, 1)


def two(operation=None):
    return calculate(operation, 2)


def three(operation=None):
    return calculate(operation, 3)


def four(operation=None):
    return calculate(operation, 4)


def five(operation=None):
    return calculate(operation, 5)


def six(operation=None):
    return calculate(operation, 6)


def seven(operation=None):
    return calculate(operation, 7)


def eight(operation=None):
    return calculate(operation, 8)


def nine(operation=None):
    return calculate(operation, 9)


def get_operation(symbol, n):
    return {
        'symbol': symbol,
        'number': n,
    }


def plus(n):
    return get_operation('+', n)


def minus(n):
    return get_operation('-', n)


def times(n):
    return get_operation('*', n)


def divided_by(n):
    return get_operation('/', n)


# 2

def calculate(operation, n):
    if not operation:
        return n
    if operation['symbol'] == '+':
        return n + operation['number']
    elif operation['symbol'] == '-':
        return n - operation['number']
    elif operation['symbol'] == '*':
        return n * operation['number']
    elif operation['symbol'] == '/':
        return n // operation['number']


zero = lambda operation=None: calculate(operation, 0)
one = lambda operation=None: calculate(operation, 1)
two = lambda operation=None: calculate(operation, 2)
three = lambda operation=None: calculate(operation, 3)
four = lambda operation=None: calculate(operation, 4)
five = lambda operation=None: calculate(operation, 5)
six = lambda operation=None: calculate(operation, 6)
seven = lambda operation=None: calculate(operation, 7)
eight = lambda operation=None: calculate(operation, 8)
nine = lambda operation=None: calculate(operation, 9)

get_operation = lambda symbol, number: {'symbol': symbol, 'number': number}

plus = lambda n: get_operation('+', n)
minus = lambda n: get_operation('-', n)
time = lambda n: get_operation('*', n)
divided_by = lambda n: get_operation('/', n)

# 3

def zero(f = None): return 0 if not f else f(0)
def one(f = None): return 1 if not f else f(1)
def two(f = None): return 2 if not f else f(2)
def three(f = None): return 3 if not f else f(3)
def four(f = None): return 4 if not f else f(4)
def five(f = None): return 5 if not f else f(5)
def six(f = None): return 6 if not f else f(6)
def seven(f = None): return 7 if not f else f(7)
def eight(f = None): return 8 if not f else f(8)
def nine(f = None): return 9 if not f else f(9)

def plus(y): return lambda x: x+y
def minus(y): return lambda x: x-y
def times(y): return lambda  x: x*y
def divided_by(y): return lambda  x: x/y
