#код в котором может возникнуть исключение помещено в try
try:
    #ввод номера столбцов и строк
    column_1=int(input())
    row_1=int(input())
    column_2=int(input())
    row_2=int(input())
    #условие определяющее может ли король за один ход перейти с первого поля на второе
    if column_1==column_2-1 and row_1==row_2-1 :
        print ("YES")
    else:
        print ("NO")
except ValueError:
    print("Ввод данных неверный")