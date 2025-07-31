import os
import json

def scan_folder(folder_path):
    result = {}
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path) and not os.path.islink(item_path):
            result[item] = scan_folder(item_path)
        else:
            # Файл как элемент списка значений
            if folder_path not in result:
                result[folder_path] = []
            # Но нам нужно, чтобы ключ был папкой, а значение - список файлов внутри нее
            # Для этого добавим файл в список под ключом текущей папки
            # Переделать: нужно для каждого уровня делать словарь {папка: [файлы или вложенные словари]}
            # Поэтому лучше сделать так:
            # Вместо списка - значения это список имён файлов
            if item not in result:
                result.setdefault('__files__', []).append(item)

    # Если есть файлы в текущей папке - вернуть словарь с ключом папки и значениями
    # Чтобы ключом была именно папка (basename), а значения - список файлов и вложенных папок
    # Отредактируем логику: сделаем словарь с именем папки, в котором лежит dict с вложенными папками и список файлов

    # Поправим функцию

def scan_folder(folder_path):
    folder_name = os.path.basename(folder_path)
    contents = {}
    files = []

    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path) and not os.path.islink(item_path):
            contents.update(scan_folder(item_path))
        else:
            files.append(item)
    if files:
        contents["__files__"] = files
    return {folder_name: contents}

folder_path = "C:/code/GPT"
folder_structure = scan_folder(folder_path)

with open("C:/code/GPT/skeleton/structure.json", "w") as json_file:
    json.dump(folder_structure, json_file, indent=4)
