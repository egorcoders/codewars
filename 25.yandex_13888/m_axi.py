# https://contest.yandex.ru/contest/13888/problems/B/

'''
В час пик на остановку одновременно подъехали три маршрутных такси,
следующие по одному маршруту, в которые тут же набились пассажиры.
Водители обнаружили, что количество людей в разных маршрутках разное,
и решили пересадить часть пассажиров так, чтобы в каждой маршрутке
было поровну пассажиров. Требуется определить, какое наименьшее
количество пассажиров придется при этом пересадить.
'''


# my solution
def m_taxi(s):
    b1, b2, b3 = [int(i) for i in s.split(' ')]
    if not (b1 + b2 + b3) % 3:
        even = (b1 + b2 + b3) / 3
        ans = 0
        if b1 > even:
            ans += b1 - even
        if b2 > even:
            ans += b2 - even
        if b3 > even:
            ans += b3 - even
        return int(ans)
    else:
        return 'IMPOSSIBLE'


if __name__ == '__main__':
    s = input()
    print(m_taxi(s))

# case_result_lst = [
#     [
#         [1, 2, 3],
#         1, 'test 1'],
#     [
#         [99, 100, 100],
#         'IMPOSSIBLE', 'test 2'],
#     [
#         [1, 1, 1],
#         0, 'test 3'],
# ]
