import re

def generator_numbers(text):
    numbers = re.findall(r"\d+\.\d+", text)  # Знаходження всіх дійсних чисел у тексті
    if not numbers:                   # Перевірка наявності чисел у тексті
        print("Числа відсутні в данному тексті.")
    for number in numbers:   
        yield float(number)      # Перетворення в дійсне число і повернення генератора

def sum_profit(text, func):
    all_numbers = func(text)      # Отримання всіх чисел та їхній суми за допомогою функції-генератора
    return sum(all_numbers)

if __name__ == '__main__':
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_zarplata = sum_profit(text, generator_numbers)
    print(f"Загальний дохід {total_zarplata}")

