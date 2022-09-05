# # my solution
# def directions(arr: list) -> list:
#     '''
#     Задача 22. Выбор кратчайшего пути.
#     '''
#     cases = {
#         "NORTH": "SOUTH",
#         "SOUTH": "NORTH",
#         "EAST": "WEST",
#         "WEST": "EAST"
#     }
#     stack = []
#     for i in arr:
#         if stack and stack[-1] == cases[i]:
#             stack.pop()
#         else:
#             stack.append(i)
#     return stack


def fn(arr):
    arr = ''.join(lst)
    cases = {
        0: '()',
        1: '{}',
        2: '[]',
    }
    while True:
        if cases[0] in arr:
            arr = arr.replace(cases[0], '')
        elif cases[1] in arr:
            arr = arr.replace(cases[1], '')
        elif cases[2] in arr:
            arr = arr.replace(cases[2], '')
        else:
            return arr


lst = ['(', '(', ')', '}']

print('Ответ хуевый:', fn(lst))
