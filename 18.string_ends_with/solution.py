# my solution
def solution_function(string, ending):
    return string[-len(ending):] == ending or ending == ''


# best solution
def solution_function(string, ending):
    return string.endswith(ending)

