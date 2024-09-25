import csv
from datetime import datetime
import matplotlib.pyplot as plt

# Функція для обчислення віку
def calculate_age(birthdate):
    today = datetime.today()
    return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

# Функція для аналізу даних
def analyze_data():
    try:
        with open('employees.csv', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            data = list(reader)[1:]  # Пропускаємо заголовок

            male_count = 0
            female_count = 0

            age_categories = {
                "younger_18": 0,
                "18-45": 0,
                "45-70": 0,
                "older_70": 0
            }

            male_in_categories = {
                "younger_18": 0,
                "18-45": 0,
                "45-70": 0,
                "older_70": 0
            }

            female_in_categories = {
                "younger_18": 0,
                "18-45": 0,
                "45-70": 0,
                "older_70": 0
            }

            for row in data:
                birthdate = datetime.strptime(row[4], '%Y-%m-%d')
                age = calculate_age(birthdate)

                gender = row[3]
                if gender == 'Чоловіча':
                    male_count += 1
                else:
                    female_count += 1

                if age < 18:
                    age_categories["younger_18"] += 1
                    if gender == 'Чоловіча':
                        male_in_categories["younger_18"] += 1
                    else:
                        female_in_categories["younger_18"] += 1
                elif 18 <= age <= 45:
                    age_categories["18-45"] += 1
                    if gender == 'Чоловіча':
                        male_in_categories["18-45"] += 1
                    else:
                        female_in_categories["18-45"] += 1
                elif 45 < age <= 70:
                    age_categories["45-70"] += 1
                    if gender == 'Чоловіча':
                        male_in_categories["45-70"] += 1
                    else:
                        female_in_categories["45-70"] += 1
                else:
                    age_categories["older_70"] += 1
                    if gender == 'Чоловіча':
                        male_in_categories["older_70"] += 1
                    else:
                        female_in_categories["older_70"] += 1

            print(f"Чоловіків: {male_count}, Жінок: {female_count}")
            plt.bar(["Чоловіки", "Жінки"], [male_count, female_count])
            plt.title("Розподіл за статтю")
            plt.show()

            print("Розподіл за віковими категоріями:")
            print(age_categories)
            plt.bar(age_categories.keys(), age_categories.values())
            plt.title("Розподіл за віком")
            plt.show()

            print("Розподіл чоловіків за віковими категоріями:")
            print(male_in_categories)
            plt.bar(male_in_categories.keys(), male_in_categories.values())
            plt.title("Чоловіки за віковими категоріями")
            plt.show()

            print("Розподіл жінок за віковими категоріями:")
            print(female_in_categories)
            plt.bar(female_in_categories.keys(), female_in_categories.values())
            plt.title("Жінки за віковими категоріями")
            plt.show()

    except FileNotFoundError:
        print("Помилка: файл employees.csv не знайдено.")
    except Exception as e:
        print(f"Помилка: {e}")

if __name__ == '__main__':
    analyze_data()
