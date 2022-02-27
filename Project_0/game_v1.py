
import numpy as np


def game_core_v3(number):
    # Способ вычисления: Делить разницу границ на 2 и вычитать от максимального числа
    
    # Проверка number == 1, number == 50
    count = 2
    
    # Проверка 1
    if number == 1:
        return(count)
    
    # Границы, которые будут меняться в зависимости от проверок
    max_num = 100
    min_num = 1
    
    # Принимает значение между границами
    predict = (max_num + min_num) // 2
    
    while number != predict:
        count+=1
        
        if number < predict:
            # Устанавливаю новую максимальную границу
            max_num = predict
            predict = max_num - ((max_num-min_num)//2)
        
        elif number > predict:
            # Устанавливаю новую минимальную границу
            min_num = predict
            predict = max_num - ((max_num-min_num)//2)  
            print(f"Ваш алгоритм угадывает число в среднем за {count} попыток.")          
    return(count) # выход из цикла, если угадали

game_core_v3(1)


