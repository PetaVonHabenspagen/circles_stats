# name = "bagr"
# def greet():
#     """Vypíše text 'Dobrý den, pane/paní {name}!'."""
#     print(f"Dobrý den, pane/paní {name}!")
# greet()

# def calculate_bmi(weight, height):
#     bmi = weight / (height ** 2)
#     return bmi
# patient_bmi = calculate_bmi(80, 1.78)
# print(f"{patient_bmi:.1f}")

# def evaluate_pressure(systolic, diastolic):
#     """Vyhodnocení krevního tlaku"""
#     if systolic < 120 and diastolic < 80:
#         return "Normální"
#     elif systolic < 130 and diastolic < 85:
#         return "Vyšší normální"
#     elif systolic < 140 and diastolic < 90:
#         return "Mírná hypertenze"
#     else:
#         return "Vysoká hypertenze"
# result = evaluate_pressure(125, 81)
# print(f"Tlak 125/92: {result}")
#
# def calculate_bmi(height, weight):
#     bmi = weight / (height ** 2)
#     rounded_bmi = round(bmi, 1)
#     return rounded_bmi
#
# print(f"BMI: {calculate_bmi(1.74, 80)}")
# name = "Lakatoš"
# def greet_patient(name):
#     """
#     :param name: (str)
#     :return: none
#     """
# print(f"Dobrý den, pane/paní {name}")
#
# def fever(temperature):
#     """
#     :param temperature: (int | float) teplota °C
#     :return: (int) informace zda má pacient horečku
#     """
#     if temperature >= 38:
#         has_fever = True
#     else:
#         has_fever = False
#     return has_fever
#
# def celsius_to_fahrenheit(temperature_C):
#     temperature_F = (temperature_C * (9/5) +32)
#     return temperature_F
#
# temperature = 38
# greet_patient("Lakatoš")
# temperature_f = celsius_to_fahrenheit(temperature)
# horecka = fever(temperature)
# print(f"Tvoje tělesná teplota je {temperature_f:.1f} F")
# if horecka:
#     print("Máš horečku")
#
#
# numbers = [1, 2, 3, 4, 5]
# names = ["Alice", "Bob", "Charlie"]
# measurements = []
# measurements.append(36.5)
# measurements.append(37.0)
# measurements.append(38.2)
# print(measurements)
#
# temps = [36.5]
# temps.append(37.0)
# print(temps)
#
# text = "Ahoj"
# text = text.upper()
# print(text)
#
# word = "kocka"
# word1 = word.replace("k", "p")
# print(word1)
#
# a = [1, 2, 3]
# b = a.copy()
# b.append(4)
# print(a)
# print(b)
#
# dna = list("ACGTTAGC")
# print(dna)
#
# data = "Jan,25,Praha"
# parts = data.split(",")
# print(parts)
#
#
# patients = ["Jan", "Marie", "Petr", "Anna", "Tomáš"]
# print(patients[0])
# print(patients[-1])
# print(patients[1:4])
# print(patients[::-1])
#
# group_a = ["Jan", "Marie"]
# group_b = ["Petr", "Anna"]
# all_patients = group_a + group_b
# print(all_patients)
#
# baseline = [0]
# week_data = baseline * 7
# print(week_data)
#
# patients = ["Jan Novák", "Marie Svobodová", "Petr Dvořák"]
# if "Jan Novák" in patients:
#     print("Pacient je v databázi")
# if "Anna Černá" not in patients:
#     print("Pacient není v databázi")
#
# list1 = [1, 2, 3]
# list2 = [1, 2, 3]
# list3 = [3, 2, 1]
# print(list1 == list2)
# print(list2 == list3)
#
# for i in range(len(patients)):
#     print(f"{i+1}. {patients[i]}")
#
# for i, patient in enumerate(patients, start=1):
#     print(f"{i}. {patient}")
#
# names = ["Jan", "Marie", "Petr"]
# temperatures = [36.5, 37.2, 38.1]
# for name, temperature in zip(names, temperatures):
#     print(f"{name}: {temperature}°C")
#
# # Seznam měření systolického tlaku za týden
# blood_pressure = [120, 125, 118, 130, 135, 128, 122]
# max1 = max(blood_pressure)
# min1 = min(blood_pressure)
# counter = 0
# for blood_value in blood_pressure:
#     if blood_value >= 130:
#         counter += 1
# print(max1)
# print(min1)
# print(counter)
# days = ["Po", "Út", "St", "Čt", "Pá", "So", "Ne"]
# for day, blood in zip(days, blood_pressure):
#     print(f"{day}: {blood} mmHg")


# numbers = [3, 1, 4, 1, 5]
# length = len(numbers)
# maximum = max(numbers)
# numbers.append(9)
# numbers.sort()
# print(numbers)
#
# patients = ["jan", "marie"]
# patients.append("petr")
# print(patients)
# new_patients = ["petr", "anna"]
# patients.extend(new_patients)
# print(patients)
# patients.append(new_patients)
# print(patients)

# patients = ["Jan", "Marie", "Petr"]
# patients.insert(1, "anna")
# print(patients)
#
# waiting_room = []
# waiting_room.append("Jan Novák")
# waiting_room.append("Marie Svobodová")
# print("Fronta:", waiting_room)
# waiting_room.insert(0, "Anna Nová")
# print("Po urgenci:", waiting_room)

# patients = ["Jan", "Marie", "Petr", "Anna"]
# last = patients.pop()
# print(last)
# print(patients)
# first = patients.pop(0)
# print(first)
# print(patients)
#
# queue = ["Jan Novák", "Marie Svobodová", "Petr Dvořák", "Anna Černá"]
# print("Původní fronta", queue)
#
# current_patient = queue.pop(0)
# print(f"\nVoláme pacienta: {current_patient}")
# print(f"Ve frontě zbývá: {len(queue)} pacientů")

# Tabulka pacientů: [jméno, věk, temperature]
# patients_data = [
#     ["Jan Novák", 45, 36.5],
#     ["Marie Svobodová", 32, 37.2],
#     ["Petr Dvořák", 28, 38.1]
# ]
# print(patients_data[1][0])
# for patient in patients_data:
#     name = patient[0]
#     age = patient[1]
#     temperature = patient[2]
#     print(f"{name} ({age} let): {temperature} °C")
#
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# for row in matrix:
#     for item in row:
#         print(item, end=" ")
#     print()
#
# measurements = [
#     ["Pondělí", 36.5, 120, 80],
#     ["Úterý", 36.7, 125, 82],
#     ["Středa", 37.2, 128, 85]
# ]
#
# weekly_data = []
#
# weekly_data.append(["Pondělí", 36.5])
# weekly_data.append(["Úterý", 36.7])
# weekly_data.append(["Středa", 37.2])
# print(weekly_data)
#
# matrix = []
# for i in range(3):
#     matrix.append([0]*3)
# print(matrix),
#
# print([10, 20, 30, 40][-2])

# numbers = [3, 1, 2]
# result = numbers.sort()
# print(result)
# def calibrate(sample):
#     left = sample[0]
#     right = sample[-1]
#     return left + right
#
# print(calibrate([2, 4, 6]))

print(len("0508150830"))