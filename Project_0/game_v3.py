
import numpy as np
def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает программа
    число от 1 до 100

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    
    random_array = np.random.randint(1,101, size=(1000)) # загадали список чисел
    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls)) # находим среднее количество попыток
    print(f"Программа угадывает число в среднем за {score} попыток.")
    return(score)

def random_num(number) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
         
    count = 2 # Проверка number == 1
       
    if number == 1: # Проверка 1
        return(count)
    
    # Начальные максимальная и минимальная границы
    max_num = 100
    min_num = 1
    
    predict = (max_num + min_num) // 2 # Принимает среднее значение между границами
    
    while number != predict:
        count+=1
        
        if number < predict:
            # Новая максимальная граница 
            max_num = predict
            predict = max_num - ((max_num-min_num)//2)
        
        elif number > predict:
            # Новая минимальная граница
            min_num = predict
            predict = max_num - ((max_num-min_num)//2)
        
    return(count) # выход из цикла, если число угадано
if __name__ == '__main__':
    score_game(random_num)