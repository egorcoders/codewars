# my solution
def remove_every_other(my_list):
    return [v for i, v in enumerate(my_list) if not i % 2]


# best solution
def remove_every_other(my_list):
    return my_list[::2]
