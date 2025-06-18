import re
from datetime import datetime

def parse_datetime(date_string): # Ця функція перебирає кожний з варіантів запису часу вказаних нижче
    formats = [
        "%Y-%m-%d %H:%M:%S",  # 2024-01-15 14:30:00
        "%d/%m/%Y %H:%M:%S",  # 15/01/2024 14:30:00
        "%m-%d-%Y",  # 01-15-2024
        "%Y-%m-%d",  # 2024-01-15
        "%d %B %Y",  # 15 January 2024
        "%B %d, %Y",  # January 15, 2024
        "%Y/%m/%d %H:%M:%S", # 2024/02/31 13:32:34
    ]

    for fmt in formats: # Цей цикл робить саме перебирання
        try:
            return datetime.strptime(date_string.strip(), fmt)
        except ValueError:
            continue

    raise ValueError(f"Unable to parse date: {date_string}")

with open("LOG.txt", "r") as log:  # Тут відкривається сам лог-файл
    content = log.read()
    lines = content.split('\n')

def menu(): # Це меню для терміналу
    print("="*10)
    print("Log Sorter")
    print("="*10)
    print("\n")
    print("To start log sorting press 0")
    print("To end program press 1")
    print("To clear the main log press 2")
    user_input = int(input(":"))
    if  user_input == 0:
        sort_log_by_td()
        return menu()
    elif user_input == 1:
        return print("Shut down complete!")
    elif user_input == 2:
        print("\n")
        print("Do you really want to clear the log?")
        print("Press 1 to continue")
        print("Press 2 to call menu")
        user_input_f_c = int(input(":"))
        if user_input_f_c == 1:
            clear_log()
            print("Log cleared!")
            return menu()
        elif user_input_f_c == 2:
            return menu()
    else:
        print("incorrect input")
        return menu()


def bubble_sort_values(d): # bubble sort для сортування по значенню ключів словників які потім виводяться як список
    items = list(d.items())
    n = len(items)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if items[j][1] > items[j + 1][1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if not swapped:
            break

    return [item[1] for item in items]

def sorting_type(txt):  # Це регулярний вираз для добування типу данних
   pattern = r'\s*\[[\s!,?.@#$%^&*]?(?P<data>[A-z]+)[\s!,?.@#$%^&*]?]|(?P<data2>[A-z]+)[\s!,?.@#$%^&*]? [\s-]?'
   match = re.search(pattern, txt)
   if match:
       type_of_data = match.group('data') or match.group('data2')
       return type_of_data

def sorting_time(txt):   # Цей регулярний вираз добуває дату
   pattern = r'(?P<timestamp>\d{4}[\s\/.,:;-]?\d{2}[\s\/.,:;-]?\d{2} \d{2}[\s\/.,:;-]?\d{2}[\s\/.,:;-]?\d{2})[\s-]?'
   match = re.search(pattern, txt)
   if match:
       return match.group('timestamp')

def sort_log_by_t(): # Ця функція сортує лог по часу використовуючи timestamp
    time_key_value = {}
    for i in range(len(lines)):
        time_of_i = sorting_time(lines[i])
        dt = parse_datetime(time_of_i)
        dt_stp = int(dt.timestamp())
        dt_dict = {dt_stp : lines[i]}
        time_key_value.update(dt_dict)
    return bubble_sort_values(time_key_value)

lines_list = list(sort_log_by_t()) # Тут створюється список з логом посортованим по часу

def sort_log_by_td(): # Ця функція сортує лог у різні файли залежачи від типу інформації
    for i in range(len(lines_list)):
        type_of_output = str(sorting_type(lines_list[i]))
        l_type_of_output = type_of_output.lower()
        if l_type_of_output == 'info':
            with open("LOG_output_INFO.txt", "a", encoding="utf-8") as log_output: # Тут функція перевіряє чи є строка
                log_output.write(lines_list[i])                                    # інфо якщо так, то відносить до відповідного файлу
                log_output.write("\n")
        elif l_type_of_output == 'warning':
            with open("LOG_output_WARNINGS.txt", "a", encoding="utf-8") as log_output:  # Тут функція перевіряє чи є строка
                log_output.write(lines_list[i])                                         # попередження якщо так, то відносить до відповідного файлу
                log_output.write("\n")
        elif l_type_of_output == 'error':
            with open("LOG_output_ERRORS.txt", "a", encoding="utf-8") as log_output: # Тут функція перевіряє чи є строка
                log_output.write(lines_list[i])                                      # помилка якщо так, то відносить до відповідного файлу
                log_output.write("\n")
        else:
            print("Incorrect type of log")
    return print("Log sorting complete!", "\n")

def clear_log(): # Ця функція може очистити лог
    with open("LOG.txt", "w", encoding="utf-8")as log_clear:
        log_clear.write('')

menu() # Тут викликатися функція меню для початку роботи юзера.