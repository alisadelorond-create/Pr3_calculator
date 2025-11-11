from calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    print("✓ Сложение работает")

def test_subtract():
    assert subtract(5, 3) == 2
    print("✓ Вычитание работает")

def test_multiply():
    assert multiply(3, 4) == 12
    print("✓ Умножение работает")

def test_divide():
    assert divide(10, 2) == 5
    print("✓ Деление работает")

def test_divide_by_zero():
    assert divide(5, 0) == "Ошибка: деление на ноль!"
    print("✓ Деление на ноль обрабатывается")

if __name__ == "__main__":
    test_add()
    test_subtract()
    test_multiply()
    test_divide()
    test_divide_by_zero()
    print("Все тесты прошли успешно! ✅")