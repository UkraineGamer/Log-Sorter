This script can sort main log into other log, also sorting them by time.
To modificate log sorter for specific files you will need to change the names of files in:
====
with open("LOG.txt", "r") as log:
    content = log.read()
    lines = content.split('\n')
====
and
====
def sort_log_by_td(): # Ця функція сортує лог у різні файли залежачи від типу інформації
    for i in range(len(lines_list)):
        type_of_output = str(sorting_type(lines_list[i]))
        l_type_of_output = type_of_output.lower()
        if l_type_of_output == 'info':
            with open("LOG_output_INFO.txt", "a", encoding="utf-8") as log_output:
                log_output.write(lines_list[i])                                    
                log_output.write("\n")
        elif l_type_of_output == 'warning':
            with open("LOG_output_WARNINGS.txt", "a", encoding="utf-8") as log_output:  
                log_output.write(lines_list[i])                                         
                log_output.write("\n")
        elif l_type_of_output == 'error':
            with open("LOG_output_ERRORS.txt", "a", encoding="utf-8") as log_output: 
                log_output.write(lines_list[i])                                     
                log_output.write("\n")
        else:
            print("Incorrect type of log")
    return print("Log sorting complete!", "\n")
====
the commentary is written in Ukranian, so translate it if you need.
Happy Coding!
