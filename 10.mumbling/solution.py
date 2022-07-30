# my solution
def accum(s):
    return '-'.join((v * (i + 1)).title() for i, v in enumerate(s))


# best solution
