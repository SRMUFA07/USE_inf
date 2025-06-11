# В1 какой набор букв будет под номером 376?
# from itertools import *
# print([i for i in permutations(sorted('модест'))][376])



# В2 под каким номером стоит набор букв подходящий по условию задания?
# from itertools import *
# for i, w in enumerate(product(sorted('компьютер'), repeat=5), 1): # единица нужна чтобы список шел с одного, как в задании
#     if i % 2 != 0 and w[0] != 'ь' and w.count('к') == 2:
#         print(i)



# В3 какое количество наборов букв будет подходящими по условию задания?
# from itertools import *
# k = 0
# for i, w in enumerate(product(sorted('дощгхимтэ'), repeat=5), 1):
#     if i % 2 == 0 and w[0] not in 'ми':
#         k += 1
# print(k)



# В4 какое количество наборов цифр будет подходящими по условию задания (девятеричная система счисления)?
# from itertools import *
# k = 0
# for x in product('012345678', repeat=7):
#     if x[0] not in '026' and x[-2] != x[-1]:
#         k += 1
# print(k)



# В5 под каким номером стоит набор букв подходящий по условию задания?
# from itertools import *
# for i, w in enumerate(product(sorted('парус'), repeat = 3), 1):
#     if w[0] == 'с':
#         print(i)



# В6 сколько различных кодов можно составить с неким условием, нет ограничения на использование букв.
# from itertools import *
# k = 0
# for w in product('ваяющий', repeat = 4):
#     if w[0] != 'й' and ('а' in w or 'я' in w or 'ю' in w or 'и' in w):
#         k += 1
# print(k)



# В7 сколько различных кодов можно составить с неким условием, каждую букву можно использовать единожды.
# from itertools import *
# k = 0
# for w in permutations('пайщик'):
#     word = ''.join(w) # объединил строку чтобы проверить по условию задания
#     if w[0] != 'й' and 'иа' not in word:
#         k += 1
# print(k)



# В8 сколько различных кодов можно составить с условием, что в коде не должны стоять рядом две гласные и две согласные буквы.
# from itertools import *
# k = set() # создал множество чтобы исключить повторения
# for w in permutations('акарида'):
#     res = '' 
#     for i in w:
#         if i in 'аи':
#             res += 'г' # гласная
#         else:
#             res += 'с' # согласная
#     if 'гг' not in res and 'сс' not in res:
#         k.add(w)
# print(len(k))



# Из букв А, Д, М, Т составили всевозможные 5-буквенные слова. Полученные слова записали в алфавитном порядке. Запишите слово, которое стоит на 330-м месте от начала списка.
# from itertools import *
# print([i for i in product(sorted('адмт'), repeat=5)][329])



# Определите количество 12-ричных пятизначных чисел, в записи которых ровно одна цифра 7
# и не более трёх цифр с числовым значением, превышающим 8.
# alph = '0123456789ab'
# count = 0
# for a in alph[1:]: # чтобы не начиналось с 0
#     for b in alph:
#         for c in alph:
#             for d in alph:
#                 for e in alph:
#                     num = a+b+c+d+e
#                     more_8 = num.count('9') + num.count('a') + num.count('b')
#                     if num.count('7') == 1 and more_8 <= 3:
#                         count += 1
# print(count)



# Составляют 5-буквенные слова из букв слова ПЯТНИЦА. Найти количество слов, которые не начинаются с Н и в которых есть только одна буква Я. Буквы в слове могут повторяться.
# from itertools import*
# count = 0
# for i in product('ПЯТНИЦА', repeat=5):
#     if i[0] != 'Н' and i.count('Я') == 1:
#         count += 1
# print(count)

# count = 0
# for a in 'ПЯТНИЦА':
#     for b in 'ПЯТНИЦА':
#         for c in 'ПЯТНИЦА':
#             for d in 'ПЯТНИЦА':
#                 for e in 'ПЯТНИЦА':
#                     word = a+b+c+d+e
#                     if word[0] != 'Н' and word.count('Я') == 1:
#                         count += 1
# print(count)



# Все 5-буквенные слова, составленные из букв А, К, Р, У, записаны в алфавитном порядке. Запишите слово, которое стоит на 150-м месте от начала списка.
# from itertools import*
# print([i for i in product(sorted("АКРУ"), repeat=5)][149])
#
# res = []
# for a in sorted('АКРУ'):
#     for b in sorted('АКРУ'):
#         for c in sorted('АКРУ'):
#             for d in sorted('АКРУ'):
#                 for e in sorted('АКРУ'):
#                     word = a+b+c+d+e
#                     res.append(word)
# print(res[149])



# Олег составляет таблицу кодовых слов для передачи сообщений, каждому сообщению соответствует своё кодовое слово. 
# В качестве кодовых слов Олег использует 4-буквенные слова, в которых есть только буквы A, B, C, D, E, X, Z, причём буквы X и Z встречаются только на двух первых позициях,
# а буквы A, B, C, D, E — только на двух последних. Сколько различных кодовых слов может использовать Олег?
# from itertools import*
# count = 0
# for i in product('ABCDEXZ', repeat=4):
#     if (i[0] in 'XZ' and i[1] in 'XZ') and (i[2] in 'ABCDE' and i[3] in 'ABCDE'):
#         count += 1
# print(count)
#
# count = 0
# for a in 'ABCDEXZ':
#     for b in 'ABCDEXZ':
#         for c in 'ABCDEXZ':
#             for d in 'ABCDEXZ':
#                 word = a+b+c+d
#                 if (word[0] in 'XZ' and word[1] in 'XZ') and (word[2] in 'ABCDE' and word[3] in 'ABCDE'):
#                     count += 1
# print(count)



# words = []
# for a in sorted('ПАРУС'):
#     for b in sorted('ПАРУС'):
#         for c in sorted('ПАРУС'):
#             for d in sorted('ПАРУС'):
#                 for e in sorted('ПАРУС'):
#                     word = a + b + c + d + e
#                     words.append(word)
#
# for word in words:
#     if word.count('У') <= 1 and 'АА' not in word:
#         print(words.index(word) + 1)



# 21407
# count = 0
# for a in 'ДГИАШЭ':
#     for b in 'ДГИАШЭ':
#         for c in 'ДГИАШЭ':
#             for d in 'ДГИАШЭ':
#                 for e in 'ДГИАШЭ':
#                     word = a + b + c + d + e
#                     if word[0] == 'И' or word[0] == 'А' or word[0] == 'Э':
#                         if word[-1] == 'Д' or word[-1] == 'Г' or word[-1] == 'Ш':
#                             count += 1
# print(count)



# 21703
# count = 0
# for a in sorted('ПОБЕДА'):
#     for b in sorted('ПОБЕДА'):
#         for c in sorted('ПОБЕДА'):
#             for d in sorted('ПОБЕДА'):
#                 for e in sorted('ПОБЕДА'):
#                     for f in sorted('ПОБЕДА'):
#                         count += 1
#                         word = a + b + c + d + e + f
#                         if count % 2 ==0 and word[0] == 'О' and len(set(word)) == 6:
#                             print(count, word)



# 21894
# count = 0
# for a in '0123456789':
#     for b in '0123456789':
#         for c in '0123456789':
#             for d in '0123456789':
#                 word = a + b + c + d
#                 if len(set(word)) == 4:
#                     word = word.replace('1', '0', 1).replace('3', '0').replace('5', '0').replace('7', '0').replace('9', '0')
#                     word = word.replace('0', '1', 1).replace('2', '1').replace('4', '1').replace('6', '1').replace('8', '0')
#                     if '00' not in word and '11' not in word:
#                         count += 1
# print(count)



# 20898
# count = 0
# for a in '012345678':
#     for b in '012345678':
#         for c in '012345678':
#             for d in '012345678':
#                 for e in '012345678':
#                     word = a + b + c + d + e
#                     if word[0] != '0' and word.count('0') == 1:
#                         word = word.replace('3' , '1').replace('5' , '1').replace('7' , '1')
#                         if '10' not in word and '01' not in word:
#                             count += 1
# print(count)



# 19240
k = 0
res = []
for a in sorted('январь'):
    for b in sorted('январь'):
        for c in sorted('январь'):
            for d in sorted('январь'):
                for e in sorted('январь'):
                    k += 1
                    word = a+b+c+d+e
                    if word[0] != 'я' and word.count('ь') <= 1 and 'яя' not in word:
                        res.append(k)
print(max(res))






























