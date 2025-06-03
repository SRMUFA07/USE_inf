# №1
# print('xyz')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             if ((x == y) or ((z or y) <= x)) == 0:
#                 print(x, y, z)



# №2
# print('xyzw')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if (((w <= y) <= x) or not z) == 0:
#                     print(x, y, z, w)



# 278)	(ЕГЭ-2024) 
# print('y x w z')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if (not(x <= w) or (y <= z) or (not y)) == 0:
#                     print(y, x, w, z)



# 279)	(ЕГЭ-2024) 
# print('xyzw')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if (((x <= y) <= z) or (not w)) == 0:
#                     print(x, y, w, z)



# 280)	(ЕГЭ-2024) 
# print('x z y w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if ((y <= (not(x <= z)) or w)) == 0:
#                     print(x, z, y, w)



# 281)	(ЕГЭ-2024) 
# print('z x y w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if (not(x <= z) or (y == w) or y) == 0:
#                     print(z, x, y, w)



# 282)	(ЕГЭ-2024) 
# print('x w z y')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if ((not(x) and y and z and not(w)) or (not(x) and y and not(z) and not(w)) or (x and y and z and not(w))) == 1:
#                     print(x, w, z, y)



# 283)	(Демо-2025) 
# print('z y w x')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if ((w <= y) <= x or not(z)) == 0:
#                     print(z, y, w, x)


# 21401
# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if (x and (z <= w) and not y) == 1:
#                     print(x, y, z, w) # xwzy



# 21888
# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if ((x and not y) or (y == z) or w) == 0:
#                     print(x, y, z, w) # xwzy



# 21697
# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if (not(x <= y) or (z == w) or z) == 0:
#                     print(x, y, z, w) # zyxw



# 21401
# print('x w z y')
# for x in range(2):
#     for w in range(2):
#         for z in range(2):
#             for y in range(2):
#                 if (x and (z <= w) and not(y)) == 1:
#                     print(x, w, z, y) # xwzy



# 20894
# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if (not(x <= y) or (z <= w) or not(z)) == 0:
#                     print(x, y, z, w) # xyzw



# 20802
print('z x y w')
for z in range(2):
    for x in range(2):
        for y in range(2):
            for w in range(2):
                if ((w <= (not(z <= x))) or y) == 0:
                    print(z, x, y, w) # zxyw













