# В1 числовая прямая
# A = set()
# def f(x, A):
#     return ((x in A) <= (x**2 <= 81)) and ((x**2 <= 36) <= (x in A))

# for x in range(-1000,1000):
#     if not f(x,A):
#         A.add(x)
# print(len(A) - 1)



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
# for A in range(300, -1, -1):
#     k = 0 
#     for x in range(300):
#         for y in range(300):
#             if (x > A) or (y > x) or (2 * y + x < 110):
#                 k += 1
#     if k == 300**2:
#         print(A)
#         break



# №7 На числовой прямой задан отрезок A. Известно, что формула
# ((x ∈ A) → (x2 ≤ 100)) ∧ ((x2 ≤ 64) → (x ∈ A))
# тождественно истинна при любом вещественном x. Какую наибольшую длину может иметь отрезок A?
# def f(x, A):
#     return ((x in A) <= (x**2 <= 100)) and ((x**2 <= 64) <= (x in A))

# A = set([i for i in range(-300, 300)])
# for x in range(-300, 300):
#     if not f(x, A):
#         A.remove(x)
# print(len(A) - 1)



# №8 На числовой прямой даны два отрезка: P=[3, 13] и Q=[12, 22]. Какова наибольшая возможная длина интервала A, что формула
# ((х ∈ A) → (х ∈ Р)) ∨ (х ∈ Q)
# тождественно истинна, то есть принимает значение 1 при любом значении переменной х.
# m = 0
# P = [i for i in range(3, 13)]
# Q = [i for i in range(12, 22)]
# for Amin in range(1, 101):
#     for Amax in range(Amin + 1, 101):
#         check = 1
#         A = [i for i in range(Amin, Amax)]
#         for x in range(1, 101):
#             f = ((x in A) <= (x in P)) or (x in Q)
#             if not f:
#                 check = 0
#                 break
#         if check == 1:
#             m = max(m, Amax - Amin)
# print(m)



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
def f(x, A):
    return (x % A != 0) <= ((x % 14 == 0) <= (x % 4 != 0))

res = []
for A in range(1, 500):
    flag = True
    for x in range(1, 500):
        if not f(x, A):
            flag = False
            break
    if flag:
        res.append(A)
print(max(res))