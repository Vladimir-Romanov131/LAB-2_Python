import re

# Запросить текст у пользователя
text = input("Введите текст: ")

# Искать слова, соответствующие шаблону
pattern = r'\b[A-Z][a-z]*\d{2,4}\b'
matches = re.findall(pattern, text)

# Вывести найденные слова
print("Найденные слова:")
for word in matches:
    print(word)