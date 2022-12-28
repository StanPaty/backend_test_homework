from math import sqrt


def calculate_square_root(Number):
    """Вычисляет квадратный корень."""
    return sqrt(Number)


def calc(your_number):
    """Печатает значение корня на экран."""
    if your_number <= 0:
        return
    root = calculate_square_root(your_number)
    print('Мы вычислили квадратный корень из введённого вами числа. '
          f'Это будет: {root}')


message = 'Добро пожаловать в самую лучшую программу для вычисления'
'квадратного корня из заданного числа'
print(message)
calc(25.5)
