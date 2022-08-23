# my solution
from math import ceil


def century(year):  return ceil(year / 100)

# best solution
def century2(year):  return (year + 99) // 100
