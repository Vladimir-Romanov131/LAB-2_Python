import re

# Запрос имени файла у пользователя
filename = input("Введите имя файла: ")

# Открываем файл и читаем его
with open(filename, 'r') as file:
    text = file.readlines()

# Инициализируем регулярное выражение для поиска дат
date_regex = r'\b\d{2}-\d{2}-\d{4}\b'

# Проходимся по каждой строке в тексте
for i, line in enumerate(text):
    # Ищем все вхождения регулярного выражения в строке
    matches = re.findall(date_regex, line)
    # Если вхождения найдены, выводим информацию о них
    if matches:
        for match in matches:
            pos = line.find(match)
            print(f"Строка {i+1}, позиция {pos+1} : найдено '{match}'")