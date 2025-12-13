import numpy as np

# R&D Logic Core: Инициализация переменных
number = np.random.randint(1, 101) # Машина загадывает число
count = 0 # Сброс счетчика попыток

while True:
    count += 1
    # Ввод данных Оператором
    predict_number = int(input("Угадай число от 1 до 100: "))
    
    # Логика сравнения
    if predict_number > number:
        print("Число должно быть меньше!")

    elif predict_number < number:
        print("Число должно быть больше!")
    
    else:
        # Победа
        print(f"Вы угадали число! Это число = {number}, за {count} попыток.")
        break # Выход из цикла