# my solution
def solution(string, ending):
    return string[-len(ending):] == ending or ending == ''


# best solution
def solution(string, ending):
    return string.endswith(ending)

