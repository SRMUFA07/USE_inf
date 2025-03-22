# пример_____________________________________________________________________________________________________________________________________
# file_array = [int(x) for x in open('17_пример.txt')] # преобразовываю данные файла в массив
# max13 = max(x for x in file_array if x % 100 == 13) # нахожу максимальное число заканчивающиеся на 13
# result = [] # список для вывода результата

# for i in range(len(file_array) - 2): # прохожу по массиву. -2 чтобы не выйти за его пределы, т.к. он проверяет два числа идущие после него
#     three_digit = range(100, 1000) # диапазон с трёхзначными числами
#     if ((file_array[i] in three_digit) + (file_array[i + 1] in three_digit) + (file_array[i + 2] in three_digit)) == 2:
#         # сначала проверяю трехзначное ли первое число, затем второе, а потом третье. Нам чтобы только два из них были трехзначными поэтому == 2 
#         if sum(file_array[i : i+3]) < max13: # также по условию сумма этих чисел должна быть меньше максимального числа заканчивающегося на 13
#             result.append(sum(file_array[i : i+3])) # закидываю подходящие по условию "тройки" в список

# print(len(result), max(result)) # получаю количство "троек" и максимальную "троку"



# №1_____________________________________________________________________________________________________________________________________
# Определите количество троек, для которых выполняются следующие условия:
# —в тройке есть пятизначные числа, но не все числа в тройке пятизначные;
# —в тройке больше чисел, кратных 3, чем чисел, кратных 5;
# —сумма элементов тройки больше максимального элемента последовательности, запись которого заканчивается на 238.

# file_array = [int(x) for x in open('17_1.txt')]
# max_238 = max(x for x in file_array if x % 1000 == 238)
# result = []

# for i in range(len(file_array) - 2):
#     troika = [file_array[i] , file_array[i+1] , file_array[i+2]]
#     multiples_5 = [x for x in troika if x % 5 == 0]
#     multiples_3 = [x for x in troika if x % 3 == 0]
#     five_digit = [x for x in troika if len(str(x)) == 5]

#     if 0 < len(five_digit) < 3 and \
#         len(multiples_3) > len(multiples_5) and \
#         sum(troika) > max_238:
#         result.append(sum(troika))

# print(len(result), max(result))



# №2_____________________________________________________________________________________________________________________________________
# Определите количество четвёрок, для которых выполняются следующие условия:
# —в четвёрке есть хотя бы два пятизначных числа и хотя бы одно не пятизначное;
# —в четвёрке больше чисел, кратных 3, чем чисел, кратных 7;
# —сумма элементов четвёрки больше максимального элемента последовательности, запись которого заканчивается на 538, но меньше удвоенного значения этого элемента.

# file_array = [int(x) for x in open('17_2.txt')]
# max_538 = max(x for x in file_array if x % 1000 == 538)
# result = []

# for i in range(len(file_array) - 3):
#     chetverka = [file_array[i] , file_array[i+1] , file_array[i+2] , file_array[i+3]]
#     multiples_3 = [x for x in chetverka if x % 3 == 0]
#     multiples_7 = [x for x in chetverka if x % 7 == 0]
#     five_digit = [x for x in chetverka if len(str(x)) == 5]
#     not_five_digit = [x for x in chetverka if len(str(x)) != 5]

#     if len(five_digit) >= 2 and len(not_five_digit) >= 1 and \
#         len(multiples_3) > len(multiples_7) and \
#         sum(chetverka) > max_538 and sum(chetverka) < max_538 * 2:
#         result.append(sum(chetverka))

# print(len(result), max(result))



# №5_____________________________________________________________________________________________________________________________________
# Определите количество троек, для которых выполняются следующие условия:
# —  ровно два числа в тройке пятизначные;
# —  хотя бы одно число в тройке делится на 5;
# — сумма элементов тройки больше максимального элемента последовательности, запись которого заканчивается на 321.

# file_array = [int(x) for x in open('17_5.txt')]
# max_321 = max(x for x in file_array if x % 1000 == 321)
# result = []

# for i in range(len(file_array) - 2):
#     troika = [file_array[i] , file_array[i+1] , file_array[i+2]]
#     five_digit = [x for x in troika if len(str(x)) == 5]
#     multiples_5 = [x for x in troika if x % 5 == 0]

#     if (len(five_digit) == 2) and \
#         (len(multiples_5) > 0) and \
#         (sum(troika) > max_321):
#         result.append(sum(troika))

# print(len(result), max(result))
    


# №6_____________________________________________________________________________________________________________________________________
# Определите количество троек, для которых выполняются следующие условия:
# —  в тройке есть четырёхзначные числа, но не все числа в тройке четырёхзначные;
# —  в тройке больше чисел, кратных 5, чем чисел, кратных 3;
# — сумма элементов тройки больше максимального элемента последовательности, запись которого заканчивается на 832.

# file_array = [int(x) for x in open('17_6.txt')]
# max_832 = max(x for x in file_array if x % 1000 == 832)
# result = []

# for i in range(len(file_array) - 2):
#     troika = [file_array[i] , file_array[i+1] , file_array[i+2]]
#     multiples_5 = [x for x in troika if x % 5 == 0]
#     multiples_3 = [x for x in troika if x % 3 == 0]
#     four_digit = [x for x in troika if len(str(x)) == 4]

#     if 0 < len(four_digit) < 3 and \
#         len(multiples_5) > len(multiples_3) and \
#         sum(troika) > max_832:
#         result.append(sum(troika))

# print(len(result), max(result))



# №10_____________________________________________________________________________________________________________________________________
# Определите количество пар, для которых выполняются следующие условия:
# —ровно одно число в паре четырёхзначное;
# —сумма квадратов элементов пары без остатка делится на наименьшее в последовательности трёхзначное число, запись которого заканчивается цифрой 3.
# В ответе запишите два числа: сначала количество найденных пар, затем максимальную из сумм квадратов элементов таких пар.

# file_array = [int(x) for x in open('17_10.txt')]
# result = []
# min_ending3_three_digit = min(i for i in file_array if len(str(i)) == 3 and str(i)[-1] == '3') # i % 10 == 3 

# for i in range(len(file_array) - 1):
#     para = [file_array[i] , file_array[i+1]]
#     four_digit = [x for x in para if len(str(x)) == 4]
#     sum_squares = sum([x**2 for x in para])

#     if len(four_digit) == 1 and \
#         sum_squares % min_ending3_three_digit == 0:
#         result.append(sum_squares)

# print(len(result), max(result))




# №3_____________________________________________________________________________________________________________________________________
# В файле содержится последовательность из 10000 целых положительных чисел.
# Каждое число не превышает 10000. Определите и запишите в ответе сначала количество пар элементов последовательности,
# у которых сумма элементов кратна 10, затем максимальную из сумм элементов таких пар. 
# В данной задаче под парой подразумевается два различных элемента последовательности. Порядок элементов в паре не важен.

# file_array = [int(x) for x in open('17_3.txt')]
# result = []

# for i in range(len(file_array) - 1):
#     for j in range(i + 1, len(file_array)):
#         element_sum = file_array[i] + file_array[j]

#         if element_sum % 10 == 0:
#             result.append(element_sum)

# print(len(result), max(result))



# №4_____________________________________________________________________________________________________________________________________
# В файле содержится последовательность из 10000 целых положительных чисел. Каждое число не превышает 10000.
# Определите и запишите в ответе сначала количество пар элементов последовательности, 
# у которых сумма элементов кратна 126, затем максимальную из сумм элементов таких пар. 
# В данной задаче под парой подразумевается два различных элемента последовательности. Порядок элементов в паре не важен.

# file_array = [int(x) for x in open('17_4.txt')]
# result = []

# for i in range(len(file_array) - 1):
#     for j in range(i + 1, len(file_array)):
#         element_sum = file_array[i] + file_array[j]

#         if element_sum % 126 == 0:
#             result.append(element_sum)

# print(len(result), max(result))



# №7_____________________________________________________________________________________________________________________________________
# Определите количество пар элементов последовательности, в которых сумма остатков от деления обоих элементов на18 равна минимальному элементу последовательности.
# В ответе запишите количество найденных пар, затем максимальную из сумм элементов таких пар. 
# В данной задаче под парой подразумевается два идущих подряд элемента последовательности.

# file_array = [int(x) for x in open('17_7.txt')]
# result = []

# for i in range(len(file_array) - 1):
#     if file_array[i] % 18 + file_array[i + 1] % 18 == min(file_array):
#         result.append(file_array[i] + file_array[i + 1])
        
# print(len(result), max(result))



# №8_____________________________________________________________________________________________________________________________________
# В файле содержится последовательность из 10 000 целых положительных чисел. Каждое число не превышает 10 000.
# Определите и запишите в ответе сначала количество пар элементов последовательности, 
# у которых сумма элементов кратна 80 и хотя бы один элемент из пары делится на 50, затем максимальную из сумм элементов таких пар. 
# В данной задаче под парой подразумевается два различных элемента последовательности. Порядок элементов в паре не важен.

# file_array = [int(x) for x in open('17_8.txt')]
# result = []

# for i in range(len(file_array) - 1):
#     for j in range(i + 1, len(file_array)):
#         element_sum = file_array[i] + file_array[j]

#         if element_sum % 80 == 0 and \
#             (file_array[i] % 50 == 0 or file_array[j] % 50 == 0):
#             result.append(element_sum)

# print(len(result), max(result))




# №9_____________________________________________________________________________________________________________________________________
# В файле содержится последовательность из 10000 целых положительных чисел.
# Каждое число не превышает 10000. Определите и запишите в ответе сначала количество пар элементов последовательности,
# у которых разность элементов кратна 45 и хотя бы один из элементов кратен 18, затем максимальную из разностей элементов таких пар. 
# В данной задаче под парой подразумевается два различных элемента последовательности. Порядок элементов в паре не важен.

# file_array = [int(x) for x in open('17_9.txt')]
# result = []

# for i in range(len(file_array) - 1):
#     for j in range(i + 1, len(file_array)):
#         element_difference = file_array[i] - file_array[j]

#         if element_difference % 45 == 0 and \
#             (file_array[i] % 18 == 0 or file_array[j] % 18 == 0):
#             result.append(element_difference)

# print(len(result), max(result))



# ЦУ_____________________________________________________________________________________________________________________________________
# В файле содержится последовательность целых неотрицательных чисел, каждое из которых не превышает 10 000. Будем считать парой два идущих подряд числа последовательности. 
# Найдите количество пар, в которых хотя бы одно из двух чисел делится на 4, а их сумма делится на 7.
# В качестве ответа запишите два числа: количество найденных пар и максимальную сумму элементов таких пар.
# Например, в последовательности (2 3 7 8 9) есть две подходящие пары: (2 3) и (3 7), в ответе для этой последовательности надо записать числа 2 и 10 через пробел: 2 10.

# file_array = [int(x) for x in open('17-825afe25-70a9-4e81-9a88-458f938a934b.txt')]
# result = []
#
# for i in range(len(file_array) - 1):
#     first_element = file_array[i]
#     second_element = file_array[i + 1]
#
#     if first_element % 4 == 0 or second_element % 4 == 0:
#         if (first_element + second_element) % 7 == 0:
#             result.append(first_element + second_element)
#
# print(len(result), max(result))



# № 39246
# Файл содержит последовательность неотрицательных целых чисел, не превышающих 10000. Назовём парой два идущих подряд элемента последовательности.
# Определите количество пар, в которых хотя бы один из двух элементов делится на 5, а их сумма делится на 7.
# В ответе запишите два числа: сначала количество найденных пар, а затем — максимальную сумму элементов таких пар.

# file_array = [int(x) for x in open('17 (1).txt')]
# count = 0
# max_sum = 0
#
# for i in range(len(file_array) - 1):
#     if (file_array[i] % 5 == 0 or file_array[i + 1] % 5 == 0) and ((file_array[i] + file_array[i + 1]) % 7 == 0):
#         count += 1
#         max_sum = max(max_sum, file_array[i] + file_array[i + 1])
#
# print(count, max_sum)



# №16328 КЕГЭ
# file_array = [int(x) for x in open('task_17/17_16328.txt')]
# res = []
#
# min_19 = 0
# for i in sorted(file_array):
#     if i % 19 == 0:
#         min_19 = i
#         break
#
# for i in range(len(file_array) - 1):
#     if file_array[i] % min_19 == 0 or file_array[i + 1] % min_19 == 0:
#         res.append(file_array[i] + file_array[i + 1])
#
# print(len(res), max(res))


# 17636 КЕГЭ
# file = [int(x) for x in open('task_17/17_17636.txt')]
# res = []
#
# max_3 = max(x for x in file if str(x)[-1] == '3' and x in range(100, 1000))
#
# for i in range(len(file) - 2):
#     if str(file[i])[-1] == '3' and abs(file[i]) in range(100, 1000) or \
#         str(file[i + 1])[-1] == '3' and abs(file[i + 1]) in range(100, 1000) or \
#         str(file[i + 2])[-1] == '3' and abs(file[i + 2]) in range(100, 1000):
#         if (file[i] + file[i+1] + file[i+2]) < max_3:
#             res.append(file[i] + file[i+1] + file[i+2])
# print(len(res), max(res))



# 14653 КЕГЭ
file = [int(x) for x in open('task_17/17.16_14653.txt')]
res = []

file_usl = [x for x in file if x % 17 == 0 and x > 0]
min_1 = sorted(file_usl)[0]
min_2 = sorted(file_usl)[1]

max69 = max([x for x in file if abs(x) % 100 == 69])

for i in range(len(file) - 3):
    if (abs(file[i]) in range(100, 1000)) + (abs(file[i+1]) in range(100, 1000)) + \
        (abs(file[i+2]) in range(100, 1000)) + (abs(file[i+3]) in range(100, 1000)) == 2:
        if (file[i] % 18 == 0) + (file[i+1] % 18 == 0) + \
            (file[i+2] % 18 == 0) + (file[i+3] % 18 == 0) == 1:
            if (file[i] + file[i+1] + file[i+2] + file[i+3]) % (min_1 + min_2) == 0:
                if (file[i] * file[i+1] * file[i+2] * file[i+3]) <= max69**2:
                    res.append((file[i] + file[i+1] + file[i+2] + file[i+3])**2)
print(len(res), min(res))