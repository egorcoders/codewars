# https://contest.yandex.ru/contest/13888/problems/A/

'''
Чтобы поднять на N-й этаж M-этажного дома новый холодильник, Витя вызвал
бригаду грузчиков. Оплата работы грузчиков производится так: за подъем
холодильника на один этаж требуется заплатить 200 рублей, за спуск на
один этаж — 100 рублей. За подъем и спуск на лифте плата не взимается.
Несмотря на то, что в Витином доме есть лифт, ему возможно все же
придется заплатить грузчикам, поскольку лифт останавливается только на
каждом K-м этаже, начиная с первого (то есть на этажах с номерами 1, K+1,
2K+1, 3K+1, …). Требуется вычислить, какой минимальной суммы денег
достаточно, чтобы грузчики доставили холодильник с первого этажа на N-й.
'''


# my solution
def elevator(s):
    m, n, k = [int(i) for i in s.split(' ')]
    up = 200
    down = 100
    k_floors = range(1, m + 1, k)
    return min([
        up * (n - i) if n >= i
        else down * (i - n)
        for i in k_floors
    ])


if __name__ == '__main__':
    s = input()
    print(elevator(s))

# case_result_lst = [
#     [
#         '20 7 4', 200,
#     [
#         '20 7 2', 0,
#     [
#         '100 100 99', 0,
# ]