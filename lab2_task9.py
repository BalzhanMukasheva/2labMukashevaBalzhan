#вводим первый пароль
password_1 = input()
#вводим второй пароль
password_2 = input()
#задаем условие для того чтобы проверить совпадают ли первый пароль со вторым
if password_1 == password_2:
    print('Password accepted')
else:
    print('Password not accepted')