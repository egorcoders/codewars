# https://contest.yandex.ru/contest/13888/problems/C/

'''
Известно, сколько времени электропоезд тратит на проезд между любыми
двумя соседними станциями своего маршрута. Известно время отправления с
начальной станции. Напишите программу, которая вычислит время отправления
электропоезда с каждой станции его маршрута (для последней станции это
будет время прибытия — временем стоянки поезда на станциях мы пренебрежем).
'''


# # my solution
# def train(t, n, s):
#     m, n, k = [int(i) for i in s.split(' ')]
#     up = 200
#     down = 100
#     k_floors = range(1, m + 1, k)
#     return min([
#         up * (n - i) if n >= i
#         else down * (i - n)
#         for i in k_floors
#     ])


# if __name__ == '__main__':
#     t = input()  # departure time
#     n = input()  # number of stations
#     s = input()  # time per setation
#     print(train(t, n, s))
# 07:00
# 4
# 10 5 3

# case_result_lst = [
#     [
#         '20 7 4', 200,
#     [
#         '20 7 2', 0,
#     [
#         '100 100 99', 0,
# ]

# hours, minutes = map(int, input().split(":"))
hours, minutes = [int(i) for i in input().split(':')]
amount = int(input())
# delays = [0] + list(map(int, input().split()))
delays = [0] + [int(i) for i in input().split()]

# print(hours, minutes)

for delay in delays:
    _hours, minutes = divmod(minutes + delay, 60)
    _, hours = divmod(hours + _hours, 24)
    print(f'{hours:02d}:{minutes:02d}')
