try:
    #вводим возраст пользователя
    age=int(input("Введите ваш возраст: "))
    #с помощью условия проверяем если возраст больше равно 18
    if age>=18 :
        print("Access is allowed")
    else:
        print("Access denied")
except ValueError:
    print("Input is not correct")