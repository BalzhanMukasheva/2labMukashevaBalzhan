#код в котором может возникнуть исключение помещено в try
try:
    #вводим порядковый номер месяца
    num = int(input("Введите порядковый номер месяца: "))
    #массив месяцы в которых 31 дней
    serial_num = {1, 3, 5, 7, 8, 10, 12}
    #задаем условие для того чтобы определить кол-во дней в месяце
    if num in serial_num:
        print("31")
    elif num == 2:
        print("28")
    else:
        print("30")
except ValueError:
    print("Ввод данных неверный")