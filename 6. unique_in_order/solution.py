# my solution
def unique_in_order(itr):
    itr = list(itr)
    itr.append(' ')
    return [itr[i] for i in range(len(itr) - 1) if itr[i + 1] != itr[i]]

# best solution
from itertools import groupby


def unique_in_order2(iterable):
    return [k for (k, _) in groupby(iterable)]
