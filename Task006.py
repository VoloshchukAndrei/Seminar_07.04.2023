#Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд 
#и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, 
#где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, 
#т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
#*Пример:*
#385916 -> yes
#123456 -> no

a = int(input("Введите номер билета: "))
b = a // 1000
d = a % 1000
sum1 = 0
sum2 = 0
while b > 0:
    sum1 = sum1 + b % 10
    b = b // 10
while d > 0:
    sum2 = sum2 + d % 10
    d = d // 10
#happiness = sum1 == sum2
#print(happiness)
if sum1 == sum2:
    print("yes")
else:
    print("no")