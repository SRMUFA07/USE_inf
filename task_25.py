# def f(x):
#     divs = set() # множество, без повторов
#     for d in range(1, int(x**0.5) + 1): # делители от 1 до корня из x
#         if x % d == 0: # если остаток от деления == 0
#             divs.add(d) # добавляю в множество число
#             divs.add(x // d) # добавляю в множество пару
#     return divs # возвращаю множество



# 10 дз Поляков
# def find_numbers_with_four_divisors(start, end):
#     # Проходим по всем числам в диапазоне
#     for num in range(start, end + 1):
#         divisors = []
#
#         # Ищем все делители числа
#         for i in range(1, int(num**0.5) + 1):
#             if num % i == 0:
#                 divisors.append(i)
#                 if i != num // i:
#                     divisors.append(num // i)
#
#         # Проверяем, есть ли у числа ровно 4 делителя
#         if len(divisors) == 4:
#             divisors.sort()
#             print(divisors)
#
# find_numbers_with_four_divisors(338472, 338494) # Значения по условию



# № 17642 Основная волна 19.06.24
def f(x):
    divs = set()
    for d in range(1, int(x**0.5) + 1):
        if x % d == 0:
            if (d % 10 == 9) and (d != x) and (d != 9):
                divs.add(d)
            if ((x//d) % 10 == 9) and ((x//d) != x) and ((x//d) != 9):
                divs.add(x//d)
    return divs

for x in range(800000, 800100):
    divs = f(x)
    if len(divs) > 0:
        print(x, min(divs))