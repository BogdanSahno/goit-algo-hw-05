import sys
def parse_log_line(line: str) -> dict:#для парсингу рядків логу.
    line = line.split()
    dict_of_lines = {}
    dict_of_lines['date'], dict_of_lines['time'], dict_of_lines['type'], dict_of_lines['information'] = line[0], line[1], line[2], ' '.join(line[3::])
    
    return dict_of_lines

def load_logs(file_path: str) -> list: #для завантаження логів з файлу.
    try:
        with open (file_path, 'r') as file:
            list_of_lines = []
            for line in file.readlines():
                list_of_lines.append(parse_log_line(line))
        return list_of_lines
    except Exception as e:
        print(f'There is an exception {e}')

def filter_logs_by_level(logs: list, level: str) -> list: #для фільтрації логів за рівнем.
    return list(filter(lambda log: log['type'].lower()==level.lower(),logs))

def count_logs_by_level(logs: list) -> dict: #для підрахунку записів за рівнем логування.
    count_dict = {}
    for log in logs:
        if log['type'] in count_dict:
            count_dict[(log['type'])] += 1
        else:
            count_dict[(log['type'])] = 1
    return count_dict

def display_log_counts(counts: dict):
    # Початок форматованого рядка з заголовком таблиці
    result = f'{"Рівень логування":<17} | Кількість\n'
    # Додавання роздільної лінії
    result += '-' * 35 + '\n'
    # Додавання рядків для кожного рівня логування у словнику
    for level, count in counts.items():
        # Формування рядка з рівнем логування та кількістю записів
        result += f'{level:<17} | {count}\n'
    return result


if __name__ == "__main__":
    try:
        # Отримуємо шлях до лог-файлу з аргументу командного рядка
        log_file = sys.argv[1]
        
        # Завантажуємо логи з вказаного файлу
        logs = load_logs(log_file)
        
        # Виводимо загальну кількість логів за кожним рівнем логування
        print(display_log_counts(count_logs_by_level(logs)))
        
        # Якщо вказаний додатковий аргумент командного рядка (тип логу), виводимо деталі для цього типу
        if len(sys.argv) == 3:
            log_type = sys.argv[2]
            print(f'Деталі логів для типу {log_type}:\n' + ''.join(map(lambda x: f"{x['date']} {x['time']} {x['information']}\n", filter_logs_by_level(logs, log_type))))
    
    # Виводимо повідомлення про помилку, якщо виникла
    except Exception as exc:
        print(f'There is an error: {exc}!')

