# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет
# с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых
# трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

#n = input()
#s1 = int(n[0]) + int(n[1]) + int(n[2])
#s2 = int(n[3]) + int(n[4]) + int(n[5])
#if s1 == s2:
#    print('Счастливый')
#else:
#    print('Обычный')

# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали
# одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
#6 -> 1 4 1
#24 -> 4 16 4
#60 -> 10 40 10

#a = int(input())
#k = int((a/3)*2)
#p = int((k/2)/2)
#s = int(p)
#print(p, k, s)

# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).

#n,m,k = int(input()),int(input()),int(input())
#if n*m>k:
#    if k%n==0 or k%m==0:
#        print('YES')
#    else:
#        print('NO')
#else:
#    print('NO')

# Найдите сумму цифр трехзначного числа.

#i = input()
#print(int(i[0])+int(i[1])+int(i[2]))