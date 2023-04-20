from constants import *
import simplejson as json
import datetime
# from ui import ui

def clear_json(note): # Создаём новый файл .json.

    """
    Функция проверяет, существует ли файл *.json, если нет, то создаёт
    и располагает там список с тестовым json-объектом.
    """
    json_data = [note]
    with open(FILE_JSON, 'w') as file:
        file.write(json.dumps(json_data, indent=4, ensure_ascii=False, encoding = 'utf-8'))

# clear_json(TEST_NOTE)

def wellcome_note_name(): #Просит ввести имя заметки и возвращает его
    note_name = str(input('Введите краткое имя заметки: '))
    return note_name

def wellcome_note_text(): #Просит ввести текст заметки и возвращает его
    note_text = str(input('Введите полный текст заметки: '))
    return note_text

def wellcome_note_number(): #Просит ввести номер заметки для операций с ней
    note_number = int(input('Введите номер заметки: '))
    return note_number

def add_to_json(note): # Добавляет в список файла новую json-заметку
    """
    Функция принимает на вход json-объект и добавляет в список файла новый элемент
    Args:
        Создаём объект json, функция считывает 
        его под видом переменной note и добавляет в список в файле *.json
    """
    card = json.load(open(FILE_JSON, encoding = 'utf-8'))
    card.append(note)
    with open(FILE_JSON, "w", encoding = 'utf-8') as file:
        file.write(json.dumps(card, file, indent=4, ensure_ascii=False))

def create_json(note_name, note_text): #Принимает строку имя и текста заметки и возвращает заполненную json-заметку
    TEST_NOTE["note_name"] = note_name
    TEST_NOTE["note_text"] = note_text
    return TEST_NOTE

# print(create_json(wellcome_note_name(), wellcome_note_text()))

def read_file_list(): #Выводит все заметки и присваивает им №
    """
    Функция считывает из файла объекты json 
    и выводит их в виде списка.
    Returns:
        _type_: _description_
    """
    with open(FILE_JSON, "r", encoding = 'utf-8') as read:
        cards = json.load(read)
        for i in range(1, len(cards)):
            card = cards[i]
            note_name = card["note_name"]
            note_text = card["note_text"]
            note_date = card["note_date"]
            print(f"Заметка №{i}\nИмя заметки: {note_name}\nЗаметка: {note_text}\nВремя создания/изменения: {note_date}\n")
    
# read_file_list()

def change_note(i, new_note): # Принимает номер записи и новую заметку и заменяет запись под номером на новую заметку
    with open(FILE_JSON, "r", encoding = 'utf-8') as file:
        cards = json.load(file)
        cards[i] = new_note
    with open(FILE_JSON, "w", encoding = 'utf-8') as file:
        file.write(json.dumps(cards, file, indent=4, ensure_ascii=False))
        print(f"Заметка №{i-1} изменена")


def delete_note(i): #Удаляет заметку.
    """
    Удаляет заметку по введённому номеру. 

    Returns:
        _type_: _description_
    """
    with open(FILE_JSON, "r", encoding = 'utf-8') as file:
        cards = json.load(file)
        cards.pop(i)
    
    with open(FILE_JSON, "w", encoding = 'utf-8') as file:
        file.write(json.dumps(cards, file, indent=4, ensure_ascii=False))
        print(f"Заметка №{i} удалена")

# delete_note(2)