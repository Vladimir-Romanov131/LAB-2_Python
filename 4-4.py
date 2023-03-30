import random

# Генерируем список из 100 дат в формате DD-MM-YYYY
dates = [f"{random.randint(1, 31):02d}-{random.randint(1, 12):02d}-{random.randint(2000, 2022)}" for _ in range(10)]

# Записываем список дат в файл
with open("task4.txt", "w") as f:
    f.write("\n".join(dates))