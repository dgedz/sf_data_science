"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

from unicodedata import name
import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: число попаток
    """
    count = 0
    
    while True:
        count+=1
        predict_number = np.random.randint(1, 100) # предполагаемое число
        if number == predict_number:
            break #выход из цикла
    return(count)

if __name__ == '__main__':
print(f'Количество попыток: {random_predict()}')

