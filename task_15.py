# В1 числовая прямая
# A = set()
# def f(x, A):
#     return ((x in A) <= (x**2 <= 81)) and ((x**2 <= 36) <= (x in A))
#
# for x in range(-1000, 1000):
#     if not f(x, A):
#         A.add(x)
# print(len(A) - 1)
from sys import flags

# В2 ДЕЛ()
# def f(x, A):
#     # (A < 50) ∧ (¬ДЕЛ(x, А) → (ДЕЛ(x, 10) → ¬ДЕЛ(x, 18)))
#     return (A < 50) and ((x % A != 0) <= ((x % 10 == 0) <= (x % 18 != 0)))
    
#     # l1 = A < 50
#     # l2 = x % A != 0
#     # l3 = x % 10 == 0
#     # l4 = x % 18 != 0
#     # return l1 and (l2 <= (l3 <= l4))

# for A in range (1, 300): # диапазон можно менять 
#     flag = True
#     for x in range (1, 300): # диапазон можно менять 
#         if not f(x, A):
#             flag = False
#             break
#     if flag:
#         print(A)

# В2.1
# def f(x, A):
#     return (x % A != 0) <= ((x % 28 == 0) <= (x % 49 != 0))

# for A in range (1, 300):
#     flag = True
#     for x in range (1, 300):
#         if not f(x, A):
#             flag = False
#             break
#     if flag:
#         print(A)



# В3 с тремя аргументами
# def f(x, y, A):
#     return (x < A) or (y < A) or (x + 2*y > 50)

# for A in range (300):
#     flag = True
#     for x in range (300):
#         for y in range (300):
#             if not f(x, y, A):
#                 flag = False
#                 break
#     if flag:
#         print(A)
#         break



# В4
# def f(x, A):
#     return (x & 77 != 0) <= ((x & 12 == 0) <= (x & A != 0))

# for A in range (300):
#     flag = True
#     for x in range (300):
#         if not f(x, A):
#             flag = False
#             break
#     if flag:
#         print(A)
#         break


# №5
# def f(x, y, A):
#     return (x + 2*y > 16) or (x + y <= A)
# for A in range (300):
#     flag = True
#     for x in range (300):
#         for y in range (300):
#             if not f(x, y, A):
#                 flag = False
#                 break
#     if flag:
#         print(A)
#         break



# №6 Для какого наибольшего целого неотрицательного числа A выражение
# (x > A) ∨ (y > x) ∨ (2y + x < 110)
# тождественно истинно, то есть принимает значение 1 при любых целых неотрицательных x и y?
# def f(x, y, A):
#     return (x > A) or (y > x) or (2 * y + x < 110)
#
# res = []
# for A in range(1, 300):
#     flag = True
#     for x in range(300):
#         for y in range(300):
#             if not f(x, y, A):
#                 flag = False
#                 break
#     if flag:
#         res.append(A)
# print(max(res))



# №7 На числовой прямой задан отрезок A. Известно, что формула
# ((x ∈ A) → (x2 ≤ 100)) ∧ ((x2 ≤ 64) → (x ∈ A))
# тождественно истинна при любом вещественном x. Какую наибольшую длину может иметь отрезок A?
# def f(x, A):
#     return ((x in A) <= (x**2 <= 100)) and ((x**2 <= 64) <= (x in A))
#
# A = list(range(-500, 500))
# for x in range(-500, 500):
#     if not f(x, A):
#         A.remove(x)
# print(len(A) - 1)



# №8 На числовой прямой даны два отрезка: P=[3, 13] и Q=[12, 22]. Какова наибольшая возможная длина интервала A, что формула
# ((х ∈ A) → (х ∈ Р)) ∨ (х ∈ Q)
# тождественно истинна, то есть принимает значение 1 при любом значении переменной х.
# P = list(range(3, 13))
# Q = list(range(12, 22))
# A = list(range(1, 300))
#
# def f(x, P, Q, A):
#     return ((x in A) <= (x in P)) or (x in Q)
#
# for x in range(1, 300):
#     if not(f(x, P, Q, A)):
#         A.remove(x)
# print(len(A))



# №9
# def f(x, A):
#     return ((x & 35 != 0) or (x & 22 != 0)) <= ((x & 15 == 0) <= (x & A != 0))

# for A in range(300):
#     flag = True
#     for x in range(300):
#         if not f(x, A):
#             flag = False
#             break
#     if flag:
#         print(A)
#         break



# 506)	(ЕГЭ-2022) 
# def f(x, y, A):
#     return (x + y <= 22) or (y <= x - 6) or (y >= A)

# res = []
# for A in range(300): 
#     flag = True
#     for x in range(300):
#         for y in range(300):
#             if not f(x, y, A):
#                 flag = False
#                 break
#     if flag:
#         res.append(A)
# print(max(res))



# 507)	(ЕГЭ-2022) 
# def f(x, A):
#     return ((x % 2 == 0) <= (x % 3 != 0)) or (x + A >= 80)

# for A in range(1, 300):
#     flag = True
#     for x in range(1, 300):
#         if not f(x, A):
#             flag = False
#             break
#     if flag: 
#         print(A)
#         break



# 542)	(ЕГЭ-2023) 
# def f(x, y, A):
#     return (x < A) or (y < A) or (x + 2*y > 50)

# for A in range(300):
#     flag = True
#     for x in range(300):
#         for y in range(300):
#             if not f(x, y, A):
#                 flag = False
#                 break
#     if flag:
#         print(A)
#         break



# 543)	(ЕГЭ-2023) 
# def f(x, y, A):
#     return (x*y < A) or (x < y) or (9 < x)

# for A in range(300):
#     flag = True
#     for x in range(300):
#         for y in range(300):
#             if not f(x, y, A):
#                 flag = False
#                 break
#     if flag:
#         print(A)
#         break



# 544)	(ЕГЭ-2023) 
# def f(x, y, A):
#     return (x + 2*y > A) or (y < x) or (x < 30)

# res = []
# for A in range(300):
#     flag = True
#     for x in range(300):
#         for y in range(300): 
#             if not f(x, y, A):
#                 flag = False
#                 break
#     if flag:
#         res.append(A)
# print(max(res))



# 564)	(ЕГЭ-2024) 
# P = list(range(15, 41))
# Q = list(range(21, 64))
# A = []
#
# for x in range(1, 300):
#     if ((x in P) <= (((x in Q) and (x not in A)) <= (x not in P))) == False:
#         A.append(x)
# print(A[-1]-A[0])



# 565)	 (ЕГЭ-2024) 
# def f(x, A):
#     return ((x % 2 == 0) <= (x % 5 != 0)) or (x + A >= 70)

# for A in range(1, 300):
#     flag = True
#     for x in range(1, 300):
#         if not f(x, A):
#             flag = False
#             break
#     if flag:
#         print(A)
#         break



# 566)	(ЕГЭ-2024) 
# def f(x, A):
#     return (x % A == 0) or ((x in range(70, 91)) <= (x % 22 != 0))

# res = []
# for A in range(1, 300):
#     flag = True
#     for x in range(1, 300):
#         if not f(x, A):
#             flag = False
#             break
#     if flag:
#         res.append(A)
# print(max(res))



# 567)	(ЕГЭ-2024) 
# def f(x, y, A):
#     return (x + y <= 30) or (y <= x + 2) or (y >= A)

# res = []
# for A in range(300):
#     flag = True
#     for x in range(300):
#         for y in range(300):
#             if not f(x, y, A): 
#                 flag = False
#                 break
#     if flag:
#         res.append(A)
# print(max(res))



# 568)	(ЕГЭ-2024) 
# def f(x, A):
#     return (x % 33 == 0) <= ((x % A != 0) <= (x % 242 != 0))
#
# res = []
# for A in range(1, 900):
#     flag = True
#     for x in range(1, 900):
#         if not f(x, A):
#             flag = False
#             break
#     if flag:
#         res.append(A)
# print(max(res))



#
# def f(x, A):
#     return (x % A != 0) <= ((x % 14 == 0) <= (x % 4 != 0))
#
# res = []
# for A in range(1, 500):
#     flag = True
#     for x in range(1, 500):
#         if not f(x, A):
#             flag = False
#             break
#     if flag:
#         res.append(A)
# print(max(res))



# № 21414 Досрочная волна 2025
# def f(x, y, A):
#     return (5 < y) or (x > 32) or (x + 2*y < A)
#
# for A in range(1, 500):
#     flag = True
#     for x in range(1, 500):
#         for y in range(1, 500):
#             if not f(x, y, A):
#                 flag = False
#                 break
#     if flag:
#         print(A)
#         break



# № 20905 Апробация 05.03.25
# def f(x, P, Q, A):
#     return (x in P) <= (((x in Q) and (x not in A)) <= (x not in P))
#
# P = list(range(17, 58))
# Q = list(range(29, 80))
# A = list()
#
# for x in range(1, 500):
#     if not f(x, P, Q, A):
#         A.append(x)
# print(min(A))



# № 14659
# def f(x, P, Q, A):
#     return ((x in A) <= (x in P)) or (x in Q)
#
# P = list(range(6, 17))
# Q = list(range(13, 28))
# A = list(range(1, 500))
#
# for x in range(1, 500):
#     if not f(x, P, Q, A):
#         A.remove(x)
# print(len(A))



# № 9370
# P = list(range(5, 55))
# Q = list(range(50, 94))
#
# def f(x, P, Q, A):
#     return (x not in P) and (x in Q) and (x <= A)
#
# for A in range(1, 500):
#     count = 0
#     for x in range(1, 500):
#         if f(x, P, Q, A):
#             count += 1
#     if count == 20:
#         print(A)
#         break



# № 16833
# P = list(range(25, 74))
# Q = list(range(75, 119))
#
# def f(x, P, Q, A):
#     return ((x in A) and (x not in Q)) <= ((x in P) or (x in Q))
#
# res = []
# for A_start in range(1, 100):
#     for A_end in range(A_start+1, 200):
#         flag = True
#         A = list(range(A_start, A_end))
#         for x in range(1, 500):
#             if not f(x, P, Q, A):
#                 flag = False
#                 break
#         if flag:
#             res.append(len(A)-1)
# print(max(res))



# № 15330
# B = list(range(24, 91))
# C = list(range(47, 116))
#
# def f(x, B, C, A):
#     return (x in C) <= (((x not in A) and (x in B)) <= (x not in C))
#
# res = []
# for A_s in range(1, 200):
#     for A_e in range(A_s+1, 300):
#         flag = True
#         A = list(range(A_s, A_e))
#         for x in range(1, 500):
#             if not f(x, B, C, A):
#                 flag = False
#                 break
#         if flag:
#             res.append(len(A)-1)
# print(min(res))



# 21414
def f(x, y, A):
    return (5 < y) or (x > 32) or (x + 2*y < A)

res = []
for A in range(1, 500):
    flag = True
    for x in range(1, 500):
        for y in range(1, 500):
            if not f(x, y, A):
                flag = False
                break
    if flag:
        res.append(A)
print(min(res))