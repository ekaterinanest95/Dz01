# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
day_of_week = int(input('Введите число дня недели: '))

if (day_of_week == 6 or day_of_week == 7):
    print('Да')
else:
    print('Нет')   
