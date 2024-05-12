def caching_fibonacci():
    cache = {}
    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1 
        elif n in cache:
            return cache[n]
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]
    return fibonacci
fib = caching_fibonacci()
print(fib(10))
print(fib(15))

# _____________________________

import re
from typing import Generator, Callable

def generator_numbers(text: str) -> Generator[str, None, None]:
    pattern = r"\d+\.*\d*"
    numbers = re.findall(pattern, text)
    for number in numbers:
        yield number
def sum_profit(text: str, func: Callable[[str], Generator[str, None, None]]) -> float:
    number_sum = 0
    for number in func(text):
        number_sum += float(number)
    return number_sum
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

# ___________________________

import sys

def parse_log_line(line: str) -> dict:
    parts = line.split(' ', maxsplit=3)
    timestamp, level, message = parts[0], parts[2], parts[3]
    return {'timestamp': timestamp, 'level': level, 'message': message}

def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                logs.append(parse_log_line(line))
    except FileNotFoundError:
        print("Файл не знайдено. Перевірте правильність шляху до файлу.")
        sys.exit(1)
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        sys.exit(1)
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log['level'] == level]

def count_logs_by_level(logs: list) -> dict:
    counts = {'INFO': 0, 'DEBUG': 0, 'ERROR': 0, 'WARNING': 0}
    for log in logs:
        level = log['level']
        counts[level] += 1
    return counts

def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<17}| {count:>10}")

def display_error_logs(logs: list):
    print("\nДеталі логів для рівня 'ERROR':")
    for log in logs:
        if log['level'] == 'ERROR':
            print(f"{log['timestamp']} - {log['message']}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: main.py file_path [log_level]")
        sys.exit(1)
    
    file_path = sys.argv[1]
    logs = load_logs(file_path)
    
    counts = count_logs_by_level(logs)
    display_log_counts(counts)
    
    if len(sys.argv) == 3:
        log_level = sys.argv[2]
        filtered_logs = filter_logs_by_level(logs, log_level)
        display_error_logs(filtered_logs)

# __________________________

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Name not found in contacts."
        except IndexError:
            return "Not enough arguments"
    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return f"Phone number for {name} updated."
    else:
        return f"{name} not found in contacts."
    
@input_error
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return f"Phone number for {name}: {contacts[name]}"
    else:
        return f"{name} not found in contacts."
    
@input_error    
def show_all(args, contacts):
    contact_list = []
    if contacts:
        result = "All contacts with phone numbers:\n"
        for name, phone in contacts.items():
            contact_list.append(contacts)
            # result += f"{name}: {phone}\n"
            result += f"{contact_list}"
            return result
    else:
        return "No contacts details."
    

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()