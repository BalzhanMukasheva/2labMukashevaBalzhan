#код в котором может возникнуть исключение помещено в try
try:
    #ввод три целых числа
    num_1 = int(input())
    num_2 = int(input())
    num_3 = int(input())
    #задаем условие которое определяет среднее число
    if num_2 < num_1 < num_3 or num_3 < num_1 < num_2:
        print('Среднее:', num_1)
    elif num_1 < num_2 < num_3 or num_3 < num_2 < num_1:
        print('Среднее:', num_2)
    else:
        print('Среднее:', num_3)
except ValueError:
        print("Ввод данных неверный")