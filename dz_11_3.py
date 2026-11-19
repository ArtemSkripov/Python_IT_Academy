# Задание 3
# Дана директория:
# project/
# data.txt
# config.json
# image.png
# users.txt
# README.md
# Напишите программу, которая с помощью os.listdir():
# ●
# получает список содержимого директории;
# ●
# находит только файлы с расширением .txt;
# ●
# выводит их имена;
# ●
# считает их количество.

import os

try:
    os.chdir('project')
    
    items = os.listdir()
    print(items)

    txt_files = [f for f in items if f.endswith('.txt')]
    print(f'Текстовые файлы{txt_files}')
    print(f'Количество{len(txt_files)}')
    
except FileNotFoundError:
  print("Ошибка: директория 'project' не найдена.")