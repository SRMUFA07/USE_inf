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
# Известно, что в исходной строке A было ровно два нуля — на первом и на последнем месте, а после выполнения
# данной программы получилась строка B, содержащая 13 единиц и 18 двоек. Какое наибольшее количество цифр могло быть в строке A?
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
#  ПОКА нашлось (111)
#  заменить (111, 22)
#  заменить (222, 11)
#  КОНЕЦ ПОКА
# КОНЕЦ
# Известно, что исходная строка содержала более 100 единиц и не содержала других цифр. Укажите минимально возможную длину исходной строки, при которой в результате работы 
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
# Какая строка получится в результате применения приведённой ниже программы к строке, состоящей из одной единицы и 75 стоящих справа от нее нулей?
# НАЧАЛО
# ПОКА нашлось (10) ИЛИ нашлось (1)
#  ЕСЛИ нашлось (10)
#  ТО заменить (10, 001)
#  ИНАЧЕ заменить (1, 00)
#  КОНЕЦ ЕСЛИ
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
#  ПОКА нашлось (01) ИЛИ нашлось (02) ИЛИ нашлось (03)
#  заменить (01, 30)
#  заменить (02, 101)
#  заменить (03, 202)
#  КОНЕЦ ПОКА
# КОНЕЦ
# Известно, что исходная строка начиналась с нуля, а далее содержала только единицы, двойки и тройки. 
# После выполнения данной программы получилась строка, содержащая 20 единиц, 0 двоек и 70 троек. Сколько единиц было в исходной строке?
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
#  заменить (111, 2)
#  заменить (222, 11)
# КОНЕЦ ПОКА
# КОНЕЦ
# К исходной строке, содержащей более 60 единиц 
# и не содержащей других символов, применили приведённую 
# выше программу. В результате получилась строка 221. Какое 
# наименьшее количество единиц могло быть в исходной строке?
# for a in range(61, 1000):
#     num = '1' * a
#     while '111' in num:
#         num = num.replace('111', '2', 1)
#         num = num.replace('222', '11', 1)
#     if num == '221':
#         print(a)
#         break



# ЦУ
# НАЧАЛО
# ПОКА нашлось (22)
# ⠀⠀ЕСЛИ нашлось (224)
# ⠀⠀⠀⠀ТО заменить (224, 9)
# ⠀⠀⠀⠀ИНАЧЕ заменить (22, 5)
# КОНЕЦ ПОКА
# КОНЕЦ
# В исходной строке содержится шесть четвёрок и четырнадцать двоек. При этом, точный порядок расположения двоек и четверок неизвестен. 
# Какую наибольшую сумму цифр может иметь строка, которая получится после выполнения программы?
# num = '4' * 6 + '2' * 14
# while '22' in num:
#     if ('224' in num):
#         num = num.replace('224', '9', 1)
#     else:
#         num = num.replace('22', '5', 1)
# print(sum(map(int, num)))



# №11
# НАЧАЛО
#  ПОКА нашлось (11111) ИЛИ нашлось (888)
#  ЕСЛИ нашлось (11111)
#  ТО заменить (11111, 88)
#  ИНАЧЕ заменить (888, 8)
#  КОНЕЦ ЕСЛИ
#  КОНЕЦ ПОКА
# КОНЕЦ
# Какая строка получится в результате применения приведённой ниже программы
# строке, состоящей из 81 идущей подряд цифре 1? 
# num = '1' * 81
# while '11111' in num or '888' in num:
#     if '11111' in num:
#         num = num.replace('11111', '88', 1)
#     else: 
#         num = num.replace('888', '8', 1)
# print(num)



# №12 Какая строка получится в результате применения приведённой ниже программы к строке, состоящей из 79 семёрок?
# НАЧАЛО
#  ПОКА нашлось (7777) ИЛИ нашлось (3333)
#  ЕСЛИ нашлось (3333)
#  ТО заменить (3333, 77)
#  ИНАЧЕ
#  заменить (7777, 33)
#  КОНЕЦ ЕСЛИ
#  КОНЕЦ ПОКА
# КОНЕЦ
# num = '7' * 79
# while '7777' in num or '3333' in num:
#     if '3333' in num:
#         num = num.replace('3333', '77', 1)
#     else:
#         num = num.replace('7777', '33', 1)
# print(num)



# №13 
# НАЧАЛО
#  ПОКА нашлось (111) ИЛИ нашлось (222)
#  заменить (111, 22)
#  заменить (222, 1)
#  КОНЕЦ ПОКА
# КОНЕЦ
# Известно, что исходная строка содержала больше 200 единиц и не содержала других цифр, а после выполнения программы получилась строка, 
# содержащая только двойки. Какое наименьшее количество единиц могло быть в исходной строке?
# for a in range(200, 1000):
#     num = '1' * a
#     while '111' in num or '222' in num:
#         num = num.replace('111', '22', 1)
#         num = num.replace('222', '1', 1)
#     if num.count('1') == 0:
#         print(a)
#         break



# №14
# НАЧАЛО
#  ПОКА НЕ нашлось (00)
#  заменить (033, 1302)
#  заменить (03, 120)
#  заменить (023, 203)
#  заменить (02, 20)
#  КОНЕЦ ПОКА
# КОНЕЦ
# Известно, что в исходной строке A было ровно два нуля — на первом и на последнем месте, а после выполнения данной программы получилась строка B,
# содержащая 340 единиц, 849 двоек и 151 тройку. Какое наибольшее количество двоек могло быть в строке A?
# result = []
# for a in range(1, 1000):
#     for b in range(1, 1000):
#         for c in range(1, 1000):
#             num = '0' + '1'*a + '2'*b + '3'*c + '0'
#             while '00' not in num:
#                 num = num.replace('033', '1302', 1)
#                 num = num.replace('03', '120', 1)
#                 num = num.replace('023', '203', 1)
#                 num = num.replace('02', '20', 1)
#             if (num.count('1') == 340) and (num.count('2') == 849) and (num.count('3') == 151):
#                 result.append(b)
# print(max(result))


# 2022_1
# num = '9' * 84
# while '33333' in num or '999' in num:
#     if '33333' in num:
#         num = num.replace('33333', '99', 1)
#     else:
#         num = num.replace('999', '3', 1)
# print(num)

# 2022_2
# num = '9' * 96
# while '22222' in num or '9999' in num:
#     if '22222' in num:
#         num = num.replace('22222', '99', 1)
#     else:
#         num = num.replace('9999', '2', 1)
# print(num)

# 2023_1
# maxi = 0
# for two in range(4, 10000):
#     num = '1' + '2' * two
#     while '12' in num or '322' in num or '222' in num:
#         if '12' in num:
#             num = num.replace('12', '2', 1)
#         if '322' in num:
#             num = num.replace('322', '21', 1)
#         if '222' in num:
#             num = num.replace('222', '3', 1)
#     summ = 0
#     for i in num:
#         summ += int(i)
#     maxi = max(maxi, summ)
# print(maxi)

# 2023_2
# for n in range(4, 10000):
#     num = '5' + '2' * n
#     while '72' in num or '522' in num or '2222' in num:
#         if '72' in num:
#             num = num.replace('72', '2', 1)
#         if '522' in num:
#             num = num.replace('522', '27', 1)
#         if '2222' in num:
#             num = num.replace('2222', '5', 1)
#
#     sum_digit = 0
#     for digit in num:
#         sum_digit += int(digit)
#     if sum_digit == 63:
#         print(n)
#         break

# 2023_3
# for n in range(4, 10000):
#     num = '1' + '8' * n
#     while '18' in num or '388' in num or '888' in num:
#         if '18' in num:
#             num = num.replace('18', '8', 1)
#         if '388' in num:
#             num = num.replace('388', '81', 1)
#         if '888' in num:
#             num = num.replace('888', '3', 1)
#
#     if num.count('1') == 3:
#         print(n)
#         break


# 2024_1
# num = '9' * 100
# while '33333' in num or '999' in num:
#     if '33333' in num:
#         num = num.replace('33333', '99', 1)
#     else:
#         num = num.replace('999', '3', 1)
# print(num)


# 2024_2
# num = '7' * 108
# while '33333' in num or '777' in num:
#     if '33333' in num:
#         num = num.replace('33333', '7', 1)
#     else:
#         num = num.replace('777', '3', 1)
# print(num)


# 2024_3
# num = '8' * 83
# while '111' in num or '88888' in num:
#     if '111' in num:
#         num = num.replace('111', '88', 1)
#     else:
#         num = num.replace('88888', '8', 1)
# print(num)


# 2024_4
# num = '9' * 136
# while '22222' in num or '9999' in num:
#     if '22222' in num:
#         num = num.replace('22222', '99', 1)
#     else:
#         num = num.replace('9999', '2', 1)
# print(num)


# 2024_5
# num = '9' * 81
# while '33333' in num or '999' in num:
#     if '33333' in num:
#         num = num.replace('33333', '99', 1)
#     else:
#         num = num.replace('999', '3', 1)
# print(num)



#
# n = 82 * '8'
# while '1111' in n or '8888' in n:
#     if '1111' in n:
#         n = n.replace('1111', '8', 1)
#     else:
#         n = n.replace('8888', '11', 1)
# print(n)



# 21411
def sum_d(num):
    res = 0
    for d in num:
        res += d
    return res

for n in range(4, 10000):
    num = '3' + '1' * n
    while '31' in num or '211' in num or '1111' in num:
        if '31' in num:
            num = num.replace('31', '1', 1)
        if '211' in num:
            num = num.replace('211', '13', 1)
        if '1111' in num:
            num = num.replace('1111', '2', 1)

    sum_d = 0
    for d in num:
        sum_d += int(d)
    if sum_d == 15:
        print(n)
        break