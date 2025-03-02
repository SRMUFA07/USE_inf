# 105)	 (ЕГЭ-2022) Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежат две кучи камней. Игроки ходят по очереди, первый ход делает Петя. 
# За один ход игрок может добавить в одну из куч (по своему выбору) один камень или увеличить количество камней в куче в два раза. 
# Для того чтобы делать ходы, у каждого игрока есть неограниченное количество камней. 
# Игра завершается в тот момент, когда суммарное количество камней в кучах становится не менее 259. Победителем считается игрок, сделавший последний ход, 
# т.е. первым получивший такую позицию, при которой в кучах будет 259 или больше камней. В начальный момент в первой куче было 17 камней, во второй куче – S камней; 1 ≤ S ≤ 241.
#       Задание 19. Ответ - 61
# Известно, что Ваня выиграл своим первым ходом после неудачного первого хода Пети. Укажите минимальное значение S, когда такая ситуация возможна.
#       Задание 20. Ответ - 112, 120
# Найдите два наименьших значения S, при которых у Пети есть выигрышная стратегия, причём одновременно выполняются два условия:
# − Петя не может выиграть за один ход;
# − Петя может выиграть своим вторым ходом независимо от того, как будет ходить Ваня.
# Найденные значения запишите в ответе в порядке возрастания.
#       Задание 21 Ответ - 111
# Найдите минимальное значение S, при котором одновременно выполняются два условия:
# – у Вани есть выигрышная стратегия, позволяющая ему выиграть первым или вторым ходом при любой игре Пети;
# – у Вани нет стратегии, которая позволит ему гарантированно выиграть первым ходом.    

# def f(a, b, m): # a - первая куча   b - вторая куча   m - ходы
#     if a+b >= 259: # условие победы, игра закончена
#         return m % 2 == 0 # эта строчка всегда есть
#     if m == 0: # если m==0 и мы не выполнили условие, возвращаю 0, игра не результативная 
#         return 0
#     h = [f(a+1, b, m-1), f(a, b+1, m-1), f(a*2, b, m-1), f(a, b*2, m-1)] # все возможные ходы. m-1 потому-что -1 ход
#     return any(h) if m % 2 != 0 else all(h) # чтобы получить ответ на 19, меняем all на any
# # all на any меняем только если такое условие: после неудачного первого хода

# print('19)', [s for s in range(1, 242) if f(17, s, 2)]) # тут по условию 19
# print('20)', [s for s in range(1, 242) if not f(17, s, 1) and f(17, s, 3)]) # условие 20
# print('21)', [s for s in range(1, 242) if not f(17, s, 2) and f(17, s, 4)]) # условие 21




# 106)	(ЕГЭ-2022) 
# def f(s, m):
#     if s >= 165: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(s+1, m-1), f(s*2, m-1)]
#     return any(h) if m % 2 != 0 else all(h)

# print('19)', [s for s in range(1, 165) if not f(s, 1) and f(s, 2)])
# print('20)', [s for s in range(1, 165) if not f(s, 1) and f(s, 3)])
# print('21)', [s for s in range(1, 165) if not f(s, 2) and f(s, 4)])


# 125)	(ЕГЭ-2023)
# def f(s, m):
#     if s >= 88: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(s+1, m-1), f(s+4, m-1), f(s*3, m-1)]
#     return any(h) if m % 2 != 0 else all(h)

# print('19)', [s for s in range(1, 88) if not f(s, 1) and f(s, 2)])
# print('20)', [s for s in range(1, 88) if not f(s, 1) and f(s, 3)])
# print('21)', [s for s in range(1, 88) if not f(s, 2) and f(s, 4)])



# 126)	(ЕГЭ-2023) 
# def f(s, m):
#     if s >= 59: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(s+1, m-1), f(s+3, m-1), f(s*4, m-1)]
#     return any(h) if m % 2 != 0 else all(h)

# print('19)', [s for s in range(1, 59) if not f(s, 1) and f(s, 2)])
# print('20)', [s for s in range(1, 59) if not f(s, 1) and f(s, 3)])
# print('21)', [s for s in range(1, 59) if not f(s, 2) and f(s, 4)])



# 127)	(ЕГЭ-2023) 
# def f(s, m):
#     if s >= 111: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(s+1, m-1), f(s+3, m-1), f(s*4, m-1)]
#     return any(h) if m % 2 != 0 else all(h)

# print('19)', [s for s in range(1, 111) if not f(s, 1) and f(s, 2)])
# print('20)', [s for s in range(1, 111) if not f(s, 1) and f(s, 3)])
# print('21)', [s for s in range(1, 111) if not f(s, 2) and f(s, 4)])



# 136)	(ЕГЭ-2024) 
# def f(a, b, m):
#     if a + b >= 65: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(a+1, b, m-1), f(a*3, b, m-1), f(a, b+1, m-1), f(a, b*3, m-1)]
#     return any(h) if m % 2 != 0 else all(h) # any в 19 ответ 7

# print('19)', [s for s in range(1, 59) if f(6, s, 2)])
# print('20)', [s for s in range(1, 59) if not f(6, s, 1) and f(6, s, 3)])
# print('21)', [s for s in range(1, 59) if not f(6, s, 2) and f(6, s, 4)])



# 137)	(ЕГЭ-2024) 
# def f(s, m):
#     if s >= 58: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(s+1, m-1), f(s+4, m-1), f(s*2, m-1)]
#     return any(h) if m % 2 != 0 else all(h)

# print('19)', [s for s in range(1, 58) if not f(s, 1) and f(s, 2)])
# print('20)', [s for s in range(1, 58) if not f(s, 1) and f(s, 3)])
# print('21)', [s for s in range(1, 58) if not f(s, 2) and f(s, 4)])



# 138)	(ЕГЭ-2024) 
# def f(s, m):
#     if s >= 39: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(s+1, m-1), f(s+3, m-1), f(s*2, m-1)]
#     return any(h) if m % 2 != 0 else all(h)

# print('19)', [s for s in range(1, 39) if not f(s, 1) and f(s, 2)])
# print('20)', [s for s in range(1, 39) if not f(s, 1) and f(s, 3)])
# print('21)', [s for s in range(1, 39) if not f(s, 2) and f(s, 4)])



# 139)	(ЕГЭ-2024) 
def f(a, b, m):
    if a + b >= 227: return m % 2 == 0
    if m == 0: return 0
    h = [f(a+1, b, m-1), f(a*2, b, m-1), f(a, b+1, m-1), f(a, b*2, m-1)]
    return any(h) if m % 2 != 0 else all(h) # any в 19 ответ 53

print('19', [s for s in range(1, 210) if f(17, s, 2)])
print('20', [s for s in range(1, 210) if not f(17, s, 1) and f(17, s, 3)])
print('21', [s for s in range(1, 210) if not f(17, s, 2) and f(17, s, 4)])