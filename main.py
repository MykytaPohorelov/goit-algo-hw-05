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
    with open(file_path, 'r') as file:
        for line in file:
            logs.append(parse_log_line(line))
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