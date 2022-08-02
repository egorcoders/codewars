# print('x y z w')
# for x in range(0, 2):
#     for y in range(0, 2):
#         for w in range(0, 2):
#             for z in range(0, 2):
#                 if not(not(x == (not(y))) or ((x and w) == z):
#                     print(x, y, z, w)

# (w → z) ∧ ((y → x) ≡ (z → y))
# (not w or z) and ((not y or x) == (not z or y))

# (x ≡ ¬y) → ((x ∧ w) ≡ z)
# if not(not(x == (not y)) or ((x and w) == z)):

# a = 0
# b = 8

# # if (a and b) < 10:
# #     print(a, b)

# if a < 10 and b < 10:
#     print(a, b)

# # Отрицание ¬	not()
# if a:
#     print('Переменная есть')
# if not a:
#     print('Переменной нет')
# # if a не существует или пустая коробочка:
#     print('такой переменной нету')

# Отрицание ¬	not()
# Логическое умножение ∧	and
# Логическое сложение ∨	or
# Следование A ⟶ B	not(A) or B
# Равносильность ≡	==

# (w → z) ∧ ((y → x) ≡ (z → y))


print('x y z w')
for x in range(2):
    for y in range(0, 2):
        for w in range(0, 2):
            for z in range(0, 2):
                if (not(w) or z) and ((not(y) or x) == (not(z) or y)):
                    print(x, y, z, w)