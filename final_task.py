import random
random.seed()
def guess_the_number_for_20_tries():
    """Игра которая загадывает случайное число
     и угадывает его максимум за 20 попыток. """

    secret_number = random.randint(1,100)
    attempts = 0
    found_range = None

# Находим в каком диапазоне находится число (пример: 1-5)
    for edge in range (5,100,5):
        attempts += 1
        if secret_number <= edge:
            found_range = (edge-4, edge)
            break
        
# Если усливие указанные выше не выполняются, тогда число находится в дапазоне (96-100)
    if found_range is None:
        found_range = (96,100)
    attempts += 1

# На последнем этапе 
    for num in range(found_range[0], found_range[1] + 1):
        if num == secret_number:
            return (f"Вы угадали число: {secret_number} за {attempts} попыток!")
print(guess_the_number_for_20_tries())
