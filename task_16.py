# №1
# def F(n):
#     if n <= 2:
#         return 2
#     if n > 2:
#         return F(n - 1) + 2 * F(n - 2)
# print(F(5))
import sys
from functools import lru_cache


# №2
# def F(n):
#     if n == 1:
#         return 2
#     if n >= 1:
#         return F(n - 1) * n
# print(F(5))



# №3
# def F(n):
#     if n == 0:
#         return 0
#     if n > 0 and n % 2 == 0:
#         return F(n // 2)
#     if n % 2 != 0:
#         return 1 + F(n - 1)
# print(len([n for n in range(1, 1001) if F(n) == 3]))



# №4
# import sys
# sys.setrecursionlimit(10**6) # повысил лимит на рекурсию, чтобы не возникало ошибки RecursionError
# def F(n):
#     if n < 11:
#         return 10
#     if n >= 11:
#         return n + F(n - 1)
# print(F(2022) - F(2019))



# №5
# def F(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return F(n - 1) + n
# print(F(30))



# №6
# def F(n):
#     if n == 1:
#         return 1
#     if n % 2 == 0:
#         return n + F(n - 1)
#     if n > 1 and n % 2 != 0:
#         return 2 * F(n - 2)
# print(F(26))




# №7
# def F(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 3
#     if n > 2:
#         return F(n - 1) * n + F(n - 2) * (n - 1)
# print(F(5))


# №8
# def F(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return F(n - 1) * (n + 2)
# print(F(5))


# №9
# import sys
# sys.setrecursionlimit(2024)
# def F(n):
#     if n < 7:
#         return 7
#     if n >= 7:
#         return 2 * n + F(n - 1)
# print(F(2024) - F(2022))


# №10
# def F(n):
#     if n == 1:  
#         return 1
#     if n == 2:  
#         return 2
#     if n > 2:
#         return 2 * F(n - 1) + (n - 2) * F(n - 2)
# print(F(6))



# №11
# def F(n):
#     if n==1: 
#         return 1
#     if n==2:
#         return 2
#     if n>2:
#         return 3 * F(n-1) - F(n-2)
# print(F(8))



# №12
# F(1)=1;
# F(2)=2;
# F(3)=3;
# F(n)=F(n − 3)·n при n > 3.
# Чему равно значение функции F(10)?
# def F(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     if n == 3:
#         return 3
#     if n > 3:
#         return F(n - 3) * n
# print(F(10))



# №13 
# F(n)=n при n ≤ 2;
# F(n)=F(n− 1)+3·F(n − 2) при n > 2.
# Чему равно значение функции F(6)?
# def F(n):
#     if n <= 2:
#         return n
#     if n > 2:
#         return F(n-1)+3 * F(n-2)
# print(F(6))



# №14
# F(n)=n, при n<11;
# F(n)=n+F(n−1), если n≥11.
# Чему равно значение выражения F(2024)−F(2021)?
# import sys
# sys.setrecursionlimit(2024)
# def F(n):
#     if n < 11:
#         return n
#     if n >= 11:
#         return n + F(n-1)
# print(F(2024) - F(2021))



# 224)	(Демо-2025) 
# import sys
# sys.setrecursionlimit(10**5)
# def F(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return (n-1)*F(n-1)
# print((F(2024) + 2*F(2023)) // F(2022))



# 213)	(ЕГЭ-2024) 
# import sys
# sys.setrecursionlimit(10**5)
# def F(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return 2 * n * F(n-1)
# print((F(2024) - 4 * F(2023)) // F(2022))



# 214)	(ЕГЭ-2024) 
# import sys
# sys.setrecursionlimit(10**5)
# def F(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return n * F(n-1)
# print((2*F(2024)+F(2023)) // F(2022))



# 215)	(ЕГЭ-2024) 
# import sys
# sys.setrecursionlimit(10**5)
# def F(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return 3 * n * F(n-1)
# print((F(2024)//6 + F(2023)) // F(2022))



# 216)	(ЕГЭ-2024) 
# import sys
# sys.setrecursionlimit(10**5)
# def F(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return 2 * n * F(n-1)
# print((F(2024)//16 - F(2023)) // F(2022))



# 217)	(ЕГЭ-2024) 
# import sys
# sys.setrecursionlimit(10**5)
# def F(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return (n+1)*F(n-1)
# print((F(2024) - 3*F(2023)) // F(2022))



# 218)	(ЕГЭ-2024) 
# import sys
# sys.setrecursionlimit(10**5)

# from functools import lru_cache
# @lru_cache(None)
# def F(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return (n+1)*F(n-1)
# for n in range(1, 2024): F(n)
# print((F(2024) + 3*F(2023)) // F(2022))



# Какой-то там Джобса
# import sys
# sys.setrecursionlimit(10**5)
# from functools import lru_cache
#
# @lru_cache(None)
# def F(n):
#     if n >= 3210: return 1
#     if n < 3210: return F(n + 3) + 7
#
# @lru_cache(None)
# def G(n):
#     if n < 10: return n
#     if n >= 10: return G(n - 3) + 5
#
# for n in range(3210, 15, -1): F(n)
# for n in range(1, 3000): G(n)
#
# print(F(15) - G(3000))



# №2247 КЕГЭ
# def F(n):
#     if n < 3: return n+1
#     if n >= 3 and n % 2 == 0: return F(n - 2) + n - 2
#     if n >= 3 and n % 2 != 0: return F(n + 2) + n + 2
#
# count = 0
# for n in range(1, 10000):
#     try:
#         if 10000 <= abs(F(n)) <= 99999: # abs() - модуль
#             count += 1
#     except:
#         pass
# print(count)



#
# import sys
# sys.setrecursionlimit(10**5)
# def F(n):
#     if n == 1: return 1
#     if n > 1: return n * F(n - 1)
#
# print((F(2024) - F(2023)) // F(2022))



# 21415.1
# import sys
# sys.setrecursionlimit(10**5)
# def F(n):
#     if n <= 5:
#         return 1
#     if n > 5:
#         return n + F(n-2)
# print(F(2126) - F(2122))

# 21415.2
# from functools import lru_cache
# @lru_cache(None)
# def F(n):
#     if n <= 5:
#         return 1
#     if n > 5:
#         return n + F(n - 2)
# for n in range(1, 2126): F(n)
# print(F(2126) - F(2122))



# 21902
# def F(n):
#     if n >= 2025:
#         return n
#     if n < 2025:
#         return n * 2 + F(n + 2)
# print(F(82) - F(81))



# 21711
# from functools import lru_cache
# @lru_cache(None)
# def F(n):
#     if n < 20:
#         return n
#     if n >= 20:
#         return (n - 6) * F(n - 7)
# for n in range(1, 47872): F(n)
# print((F(47872) - 290 * F(47865)) // F(47858))



# 16327
# from functools import lru_cache
# @lru_cache(None)
# def F(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return n * F(n - 1)
# for n in range(1, 2024): F(n)
# print((F(2024) - F(2023)) // F(2022))



# 16263
# from functools import lru_cache
# @lru_cache(None)
# def F(n):
#     if n < 7:
#         return 7
#     if n >= 7 and n % 3 != 0:
#         return 5 - F(n - 1)
#     if n >= 7 and n % 3 == 0:
#         return 3 + F(n - 1)
# for n in range(1, 3015): F(n)
# print(F(3015))



# 14339
from functools import lru_cache
@lru_cache(None)
def F(n):
    if n < 11:
        return n
    if n >= 11 and n % 2 == 0:
        return 2 * n - 3 + F(n - 2)
    if n >= 11 and n % 2 != 0:
        return 3 * n - 4 + F(n - 3)
for n in range(1, 5500): F(n)
print(F(5500) - F(5497))


































