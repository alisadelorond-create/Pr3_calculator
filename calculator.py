def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль!"
    return a / b

# Этот код запустится ТОЛЬКО если файл запущен напрямую
if __name__ == "__main__":
    print("=== ПРОСТОЙ КАЛЬКУЛЯТОР ===")
    print("1. Сложение")
    print("2. Вычитание") 
    print("3. Умножение")
    print("4. Деление")

    choice = input("Выберите операцию (1-4): ")
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    if choice == '1':
        result = add(num1, num2)
        print(f"Результат: {num1} + {num2} = {result}")
    elif choice == '2':
        result = subtract(num1, num2)
        print(f"Результат: {num1} - {num2} = {result}")
    elif choice == '3':
        result = multiply(num1, num2)
        print(f"Результат: {num1} * {num2} = {result}")
    elif choice == '4':
        result = divide(num1, num2)
        print(f"Результат: {num1} / {num2} = {result}")
    else:
        print("Неверный выбор!")