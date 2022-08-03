# my solution
from re import sub


def printer_error(s):
    print = 'abcdefghijklm'
    error = str(sum(i not in print for i in s))
    return error + '/' + str(len(s))


# best solution
def printer_error(s):
    return '{}/{}'.format(len(sub('[a-m]','',s)), len(s))
