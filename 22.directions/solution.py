# my solution
def directions(arr: list) -> list:
    '''
    Задача 22. Выбор кратчайшего пути.
    '''
    cases = {
        "NORTH": "SOUTH",
        "SOUTH": "NORTH",
        "EAST": "WEST",
        "WEST": "EAST"
    }
    stack = []
    for i in arr:
        if stack and stack[-1] == cases[i]:
            stack.pop()
        else:
            stack.append(i)
    return stack
