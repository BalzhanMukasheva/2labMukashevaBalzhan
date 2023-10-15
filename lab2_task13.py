def determine_triangle_type(a, b, c):
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Versatile"

# Получаем длины сторон от пользователя
try:
    a = float(input("Введите длину стороны a: "))
    b = float(input("Введите длину стороны b: "))
    c = float(input("Введите длину стороны c: "))
except ValueError:
    print("Некорректный ввод. Пожалуйста, введите числа.")
    exit(1)

# Проверяем, является ли возможным треугольник с данными сторонами
if a + b > c and a + c > b and b + c > a:
    # Определяем тип треугольника
    triangle_type = determine_triangle_type(a, b, c)
    # Выводим результат
    print("Треугольник является", triangle_type)
else:
    print("Треугольник с такими сторонами невозможен.")