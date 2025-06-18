🗂️ Log Sorter
This script automatically sorts log entries from the main file LOG.txt by timestamp and message type: INFO, WARNING, or ERROR.
It includes a simple terminal menu for user interaction.

📦 Contents
LOG.txt — input log file

LOG_output_INFO.txt — file containing INFO messages

LOG_output_WARNINGS.txt — file containing WARNING messages

LOG_output_ERRORS.txt — file containing ERROR messages

🚀 How to Use
Add your logs to the LOG.txt file.

Run the script:

bash
Копіювати
Редагувати
python your_script_name.py
A menu will appear in the terminal:

==========
Log Sorter
==========

To start log sorting press 0  
To end program press 1  
To clear the main log press 2
Press 0 to start sorting

Press 1 to exit the program

Press 2 to clear the log file

🧠 Features
✅ parse_datetime(date_string)
Supports multiple datetime formats

Returns a datetime object

🔎 sorting_time(txt)
Extracts the timestamp from a log entry using regular expressions

🔎 sorting_type(txt)
Extracts the log message type (INFO, WARNING, ERROR) using regular expressions

🔃 sort_log_by_t()
Sorts log entries chronologically

🧩 sort_log_by_td()
Distributes log entries into corresponding files based on type

🧹 clear_log()
Clears the contents of LOG.txt

🛠 Sample Log Format
2024-01-15 14:30:00 [INFO] System started
2024-01-15 14:45:00 [WARNING] Memory threshold exceeded
2024-01-15 15:00:00 [ERROR] Database connection failed
⚠️ Notes
Supported datetime formats include:

2024-01-15 14:30:00

15/01/2024 14:30:00

01-15-2024

2024-01-15

15 January 2024

January 15, 2024

2024/02/31 13:32:34

If the timestamp or log type cannot be parsed, the entry will be skipped and a message will be printed to the terminal.

📄 License
This script may be used, modified, and distributed for educational or internal purposes. For commercial use, permission from the author is recommended.
====
The code commentary is written in Ukranian, so translate it if you need.
Happy Coding!
