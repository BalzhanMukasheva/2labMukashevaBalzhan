try:
    #вводим три числа
    num1=int(input())
    num2=int(input())
    num3=int(input())
    #условие арифметической прогрессии
    if num2-num1==num3-num2:
        print('YES')
    else:
        print('NO')
except ValueError:
    print("Input is not correct")