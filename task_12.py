# В1
# num = '8' * 68
# while ('222' in num) or ('888' in num):
#     if ('222' in num):
#         num = num.replace('222', '8', 1)
#     else:
#         num = num.replace('888', '2', 1)
# print(num)



# №1
# num = '9' * 85
# while ('666' in num) or ('999' in num):
#     if ('666' in num):
#         num = num.replace('666', '9', 1)
#     else:
#         num = num.replace('999', '6', 1)
# print(num)



# №3
# num = '1' * 77
# while ('11' in num):
#     if ('222' in num):
#         num = num.replace('222', '1', 1)
#     else:
#         num = num.replace('11', '2', 1)
# print(num)



# №6
# num = '8' * 69
# while ('3333' in num) or ('8888' in num): 
#     if ('3333' in num):
#         num = num.replace('3333', '88', 1)
#     else:
#         num = num.replace('8888', '33', 1)
# print(num)



# №2 
# Известно, что в исходной строке A было ровно два нуля  
# — на первом и на последнем месте, а после выполнения 
# данной программы получилась строка B, содержащая 13 единиц и 18 двоек.
# Какое наибольшее количество цифр могло быть в строке A?
# for a in range(1, 20):
#     for b in range(1, 20):
#         for c in range(1, 20):
#             num = '0' + '1'*a + '2'*b + '3'*c + '0'
#             while '00' not in num:
#                 num = num.replace('01', '220', 1)
#                 num = num.replace('02', '1013', 1)
#                 num = num.replace('03', '120', 1)
#             if num.count('1') == 13 and num.count('2') == 18:
#                 print(a + b + c + 2) 



# №4
# НАЧАЛО
#     ПОКА нашлось (111)
#         заменить (111, 22)
#         заменить (222, 11)
#     КОНЕЦ ПОКА
# КОНЕЦ
# Известно, что исходная строка содержала более 100 единиц и не содержала других цифр.
# Укажите минимально возможную длину исходной строки, при которой в результате работы 
# этой программы получится строка, содержащая максимально возможное количество единиц.
# max_zero = 0
# max_digit = 0
# for a in range(101, 110):
#     num = '1' * a
#     while '111' in num:
#         num = num.replace('111', '22', 1)
#         num = num.replace('222', '11', 1)
#     if num.count('1') > max_zero:
#         max_zero = num.count('1')
#         max_digit = a
# print(max_digit)
    


# №5
# num = '1' * 85
# while '11111' in num:
#     num = num.replace('111', '2', 1)
#     num = num.replace('222', '1', 1)
# print(num)



# №7
# Какая строка получится в результате применения приведённой ниже программы 
# к строке, состоящей из одной единицы и 75 стоящих справа от нее нулей?
# НАЧАЛО
# ПОКА нашлось (10) ИЛИ нашлось (1)
#     ЕСЛИ нашлось (10)
#         ТО заменить (10, 001)
#         ИНАЧЕ заменить (1, 00)
#     КОНЕЦ ЕСЛИ
# КОНЕЦ ПОКА
# КОНЕЦ
# num = '1' + '0' * 75
# while ('10' in num) or ('1' in num):
#     if '10' in num:
#         num = num.replace('10', '001', 1)
#     else:
#         num = num.replace('1', '00', 1)
# print(num.count('0'))



# №8
# НАЧАЛО
#     ПОКА нашлось (01) ИЛИ нашлось (02) ИЛИ нашлось (03)
#         заменить (01, 30)
#         заменить (02, 101)
#         заменить (03, 202)
#     КОНЕЦ ПОКА
# КОНЕЦ
# Известно, что исходная строка начиналась с нуля, а далее 
# содержала только единицы, двойки и тройки. После выполнения 
# данной программы получилась строка, содержащая 20 единиц, 
# 10 двоек и 70 троек. Сколько единиц было в исходной строке?
# for a in range(60):
#     for b in range(60):
#         for c in range(60):
#             num = '0' + '1'*a + '2'*b + '3'*c
#             while ('01' in num) or ('02' in num) or ('03' in num):
#                 num = num.replace('01', '30', 1)
#                 num = num.replace('02', '101', 1)
#                 num = num.replace('03', '202', 1)
#             if (num.count('1') == 20) and (num.count('2') == 10) and (num.count('3') == 70):
#                 print(a)


# №9
# for a in range(60):
#     for b in range(60):
#         for c in range(60):
#             num = '0' + '1'*a + '2'*b + '3'*c
#             while ('01' in num) or ('02' in num) or ('03' in num):
#                 num = num.replace('01', '2302', 1)
#                 num = num.replace('02', '10', 1)
#                 num = num.replace('03', '201', 1)
#             if (num.count('1') == 50) and (num.count('2') == 12) and (num.count('3') == 7):
#                 print(a)



# №10
# НАЧАЛО
# ПОКА нашлось (111)
#     заменить (111, 2)
#     заменить (222, 11)
# КОНЕЦ ПОКА
# КОНЕЦ
# К исходной строке, содержащей более 60 единиц 
# и не содержащей других символов, применили приведённую 
# выше программу. В результате получилась строка 221. Какое 
# наименьшее количество единиц могло быть в исходной строке?
for a in range(61, 1000):
    num = '1' * a
    while '111' in num:
        num = num.replace('111', '2', 1)
        num = num.replace('222', '11', 1)
    if num == '221':
        print(a)
        break