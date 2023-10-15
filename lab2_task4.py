try:
    #вводим четыре числа задающие номер столбца и номер строки
    column_1=int(input())
    row_1=int(input())
    column_2=int(input())
    row_2=int(input())
    #задаем условие если столбцы или строки равны
    if column_1==column_2 or row_1==row_2:
        print('YES')
    else:
        print('NO')
except ValueError:
    print("Input is not correct")