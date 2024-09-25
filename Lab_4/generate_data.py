import csv
import random
from faker import Faker # type: ignore
from datetime import datetime

fake = Faker(locale='uk_UA')

# Словники для по батькові
male_patronymics = [
    "Іванович", "Петрович", "Сергійович", "Олександрович", "Андрійович",
    "Володимирович", "Богданович", "Миколайович", "Юрійович", "Олегович",
    "Дмитрович", "Євгенович", "Леонідович", "Григорович", "Васильович",
    "Романович", "Федорович", "Макарович", "Степанович", "Михайлович"
]

female_patronymics = [
    "Іванівна", "Петрівна", "Сергіївна", "Олександрівна", "Андріївна",
    "Володимирівна", "Богданівна", "Миколаївна", "Юріївна", "Олегівна",
    "Дмитрівна", "Євгенівна", "Леонідівна", "Григорівна", "Василівна",
    "Романівна", "Федорівна", "Макарівна", "Степанівна", "Михайлівна"
]

# Функція для генерування випадкових даних
def generate_employee_data(num_records=2000):
    with open('employees.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([
            "Прізвище", "Ім'я", "По батькові", "Стать", "Дата народження",
            "Посада", "Місто проживання", "Адреса проживання", "Телефон", "Email"
        ])

        for _ in range(num_records):
            gender = random.choices(['Чоловіча', 'Жіноча'], weights=[60, 40])[0]
            
            if gender == 'Чоловіча':
                first_name = fake.first_name_male()
                patronymic = random.choice(male_patronymics)
                last_name = fake.last_name_male()
            else:
                first_name = fake.first_name_female()
                patronymic = random.choice(female_patronymics)
                last_name = fake.last_name_female()

            birth_date = fake.date_of_birth(minimum_age=16, maximum_age=85)
            position = fake.job()
            city = fake.city()
            address = fake.address()
            phone = fake.phone_number()
            email = fake.email()

            writer.writerow([last_name, first_name, patronymic, gender, birth_date,
                             position, city, address, phone, email])

if __name__ == '__main__':
    generate_employee_data()
    print("Згенеровані дані в файлі employees.csv")
