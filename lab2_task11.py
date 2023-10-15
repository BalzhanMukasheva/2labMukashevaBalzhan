try:
    #вводим два числа
    num_1 = int(input())
    num_2 = int(input())
    #задаем условие чтобы определить наименьшее среди двух введенных чисел
    if num_1 < num_2:
        print(num_1)
    else:
        print(num_2)
except ValueError:
    print('Input is not correct')