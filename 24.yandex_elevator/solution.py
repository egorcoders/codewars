# my solution
m = 20  # этажи
n = 7  # целевой этаж
k = 2  # шаг лифта
up = 200  # стоимость подъема вверх
down = 100  # стоимость подъема вниз

k_floors = range(1, m, k)

ans = min([
    up * (n - i) if n > i
    else down * (i - n)
    for i in k_floors
])

print(ans)
