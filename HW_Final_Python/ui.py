from constants import *
import simplejson as json
from functions import *

def ui():
    # clear_json(TEST_NOTE)
    print("\n Добро пожаловать в программу 'ЗАМЕТКА_2.0'\
          \nЯ умею:\n\
          1. Создать и сохранить заметку в формате (Имя заметки, Текст заметки)\n\
          2. Выводить на экран все сохранённые заметки.\n\
          3. Удалять выбранную заметку.\n\
          4. Редактировать выбранную заметку\n\
          0. Сбросить (удалить) все заметки\n\
          Ctrl+C Выход из программы")
    number_function = int(input('\nВведите в терминал номер необходимой функции: '))
    print('\n')
    if number_function == 1:
        add_to_json(create_json(wellcome_note_name(), wellcome_note_text()))
        print("\nЗаметка добавлена.")
        return ui()
    elif number_function == 2:
        read_file_list()
        return ui()
    elif number_function == 3:
        delete_note(wellcome_note_number())
        return ui()
    elif number_function == 4:
        change_note(wellcome_note_number(), create_json(wellcome_note_name(), wellcome_note_text()))
        return ui()

    elif number_function == 0:
        clear_json(TEST_NOTE)
        print("Все заметки удалены.")
        return ui()
    else: 
        print("Нет такой цифры в этом списке. Попробуй ещё раз.\n") 
        return ui()
