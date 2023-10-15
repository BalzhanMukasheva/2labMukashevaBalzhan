


#код в котором может возникнуть исключение помещено в try
try:
    #вводим вес
    weight = int(input())
    #задаем условие чтобы понять к какой весовой категории относится введенное значение
    if weight<=60:
        print('Light weight')
    elif weight>60 and weight<=64:
        print('First welterweight')
    elif weight>64 and weight<=69:
        print('Welterweight')
    else:
        print('Boxer does not fit weight')
except ValueError:
        print('Input is not correct')