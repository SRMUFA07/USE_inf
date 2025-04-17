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
# def f(x):
#     divs = set()
#     for d in range(1, int(x**0.5) + 1):
#         if x % d == 0:
#             if (d % 10 == 9) and (d != x) and (d != 9):
#                 divs.add(d)
#             if ((x//d) % 10 == 9) and ((x//d) != x) and ((x//d) != 9):
#                 divs.add(x//d)
#     return divs
#
# for x in range(800000, 800100):
#     divs = f(x)
#     if len(divs) > 0:
#         print(x, min(divs))



# № 18192
# def p(d):
#     if d <= 1: return False # ни 1, ни числа < 1 - не простые
#     if d == 2: return True # число 2 - простое
#     if d % 2 == 0: return False # все четные числа кроме 2 - не простые
#     for i in range(3, int(d**0.5) + 1):
#         if d % i == 0: return False # если у d есть делитель отличный от 1 и от d - не простое
#     return True
#
# def f(x):
#     divs = set()
#     for d in range(1, int(x**0.5) + 1):
#         if x % d == 0:
#             if p(d):
#                 divs.add(d)
#             if p(x//d):
#                 divs.add(x//d)
#     return divs
#
# for x in range(1000001, 1000500):
#     divs = f(x)
#     if len(divs) == 3:
#         print(x, max(divs))



# № 17880 Демоверсия 2025
# from fnmatch import fnmatch
# for n in range(1917, 10**10 + 1, 1917):
#     if fnmatch(str(n), '3?12?14*5'):
#         print(n, n//1917)



# № 5642
# from fnmatch import fnmatch
# def f_mask(x):
#     divs = set()
#     for d in range(1, int(x**0.5) + 1):
#         if x % d == 0:
#             if fnmatch(str(d), '*1?3'):
#                 divs.add(d)
#             if fnmatch(str(x//d), '*1?3'):
#                 divs.add(x//d)
#     return divs
#
# def f_all(x):
#     divs = set()
#     for d in range(1, int(x**0.5) + 1):
#         if x % d == 0:
#             divs.add(d)
#             divs.add(x//d)
#     return sorted(divs)
#
# for x in range(500000, 600000):
#     divs_mask = f_mask(x)
#     divs_all = f_all(x)
#     if len(divs_mask) == 3:
#         print(x, divs_all[-2])



# №5226
# from fnmatch import fnmatch
#
# def f(x):
#     divs = set()
#     for d in range(1, int(x**0.5) + 1):
#         if x % d == 0:
#             divs.add(d)
#             divs.add(x//d)
#     return sorted(divs)
#
# for koren_iz_x in range(int((10**9 + 1)**0.5), int((10**10)**0.5)): # прохожу только ко корням
#     x = koren_iz_x**2
#     divs = f(x)
#     if fnmatch(str(x), '1*2*7*04'):
#         if len(divs) == 45: # 45 делителей, если у числа неполное количество делителей, то число является полным квадратом, то есть из него извлекается квадратный корень
#             print(x, divs[-2])



# 9846
# from fnmatch import fnmatch
# for x in range(2025, 10**8, 2025):
#     if fnmatch(str(x), '12*34?5'):
#         print(x, x//2025)



# 9792
# from fnmatch import fnmatch
# for x in range(1923, 10**8, 1923):
#     if fnmatch(str(x), '1*2??76'):
#         print(x, x//1923)



# 9754
# from fnmatch import fnmatch
# for x in range(2023, 10**8, 2023):
#     if fnmatch(str(x), '3?1*57'):
#         print(x, x//2023)



# из пробника
# from fnmatch import fnmatch
# for x in range(2031, 10**10, 2031):
#     if fnmatch(str(x), '21?478*7'):
#         print(x, x//2031)



# 21422
def f(x):
    divs = set()
    for d in range(1, int(x**0.5) + 1):
        if x % d == 0:
            if (str(d)[-1] == '7') and d != x and d != 7:
                divs.add(d)
            if (str(x//d)[-1] == '7') and x//d != x and x//d != 7:
                divs.add(x // d)
    return divs

for x in range(1125000, 1150000):
    divs = f(x)
    if len(divs) > 0:
        print(x, min(divs))