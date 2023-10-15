def determine_age_group(age):
    if age <= 13:
        return "childhood"
    elif 14 <= age <= 24:
        return "youth"
    elif 25 <= age <= 59:
        return "maturity"
    else:
        return "old age"

# Получаем возраст от пользователя
try:
    age = int(input("Введите возраст: "))
except ValueError:
    print("Некорректный ввод. Пожалуйста, введите целое число.")
    exit(1)

# Определяем возрастную группу
age_group = determine_age_group(age)

# Выводим результат
print("Ваша возрастная группа: " + age_group)
