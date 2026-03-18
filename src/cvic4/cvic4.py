# patient_id, heart_rate, spo2 = ("P001", 58, 96)
# print(patient_id)
# print(heart_rate)
# print(spo2)
#
# ids = ["P001", "P002", "P003"]
# bmi = [22.7, 25.6, 31.1]
#
# pairs = list(zip(ids, bmi))
# print(pairs[1])
#
# heart_rates = [58, 64, 72, 102]
# rates_plus_one = []
# for rate in heart_rates:
#     rates_plus_one.append(rate + 1)
# print(rates_plus_one)
#
# heart_rates = [58, 64, 72, 102]
# rates_plus_one = [rate + 1 for rate in heart_rates]
# print(rates_plus_one)
#
# heart_rates1 = [58, 64, 72, 102, 98, 110, 76, 59]
# warning_rates = []
# for rate in heart_rates1:
#     if rate < 60 or rate > 100:
#         warning_rates.append(rate)
# print(warning_rates)
#
# heart_rates1 = [58, 64, 72, 102, 98, 110, 76, 59]
# warning_rates1 = [rate for rate in heart_rates1 if rate < 60 or rate > 100]
# print(warning_rates1)

# temperatures_c = [36.5, 37.0, 38.2]
# def celsius_to_fahrenheit(value):
#     return round(value * 9 / 5 + 32.1)
# temperatures_f = [celsius_to_fahrenheit(value) for value in temperatures_c]
# print(temperatures_f)
#
# patient_ids = ["P001", "P002", "P003"]
# bmi_values = [22.7, 25.6, 31.1]
#
# def format_bmi_line(patient_id, bmi):
#     return f"{patient_id}: BMI {bmi:.1f}"
# report_lines = [format_bmi_line(patient_id, bmi) for patient_id, bmi in zip(patient_ids, bmi_values)]
# print(report_lines)

# raw_values = ["58", "64", "72", "102"]
# heart_rates = [int(value)+1 for value in raw_values]
# print(heart_rates)

# """Ukol 1:"""
# records = [
#     ("ORD-001", 2, 499),
#     ("ORD-002", 8, 149),
#     ("ORD-003", 1, 1299),
#     ("ORD-004", 5, 89),
#     ("ORD-005", 10, 59)
# ]
# vra = [order for order in records if order[1] >= 5 or order[2] >= 1000]
#
# with open("data/lab_notes.txt", mode = "r", encoding = "utf-8") as file:
#     content = file.read()
# print(content)
# #
# # with open("data/report.txt", mode = "w") as file:
# #     file.write("Pacient: P001\n")
# #     file.write("Tep: 78\n")
#
# with open("data/report.txt", mode = "a") as file:
#     file.write("SpO2: 97\n")
# with open("data/report.txt", mode = "r", encoding = "utf-8") as file:
#     content1 = file.read()
# print(content1)
#
# with open("data/lab_notes.txt", mode = "r", encoding = "utf-8") as file:
#     text = file.read()
# print(text)
#
# with open("data/lab_notes.txt", mode = "r", encoding = "utf-8") as file:
#     first_line = file.readline()
#     second_line = file.readline()
# print(first_line)
# print(second_line)
#
# with open("data/lab_notes.txt", mode = "r", encoding = "utf-8") as file:
#     lines = file.readlines()
# print(lines)
#
# with open("data/lab_notes.txt", mode = "r", encoding = "utf-8") as file:
#     for line in file:
#         print(line)

# with open("data/lab_notes.txt", mode = "r", encoding = "utf-8") as file:
#     content = file.read()
# with open(r"C:\Users\283151\Desktop\python\data\lab_notes.txt", mode = "r", encoding = "utf-8") as file:
#     content1 = file.read()
# print(content1)
#
# with open("data/products_comma.csv", mode = "r", encoding = "utf-8") as file:
#     lines = file.readlines()
#     header = lines[0].strip().split(",")
#     rows = [line.strip().split(",") for line in lines[1:]]
# print(header)
# print(rows)

# risk_rows = [
#     ["id", "heart_rate", "spo2"],
#     ["P003", "105", "92"],
#     ["P005", "112", "91"],
# ]
# with open("data/risk_patients.csv", mode = "w", encoding = "utf-8") as file:
#     for row in risk_rows:
#         file.write((",").join(row) + "\n")
# with open("data/risk_patients.csv", mode = "r", encoding = "utf-8") as file:
#     text = file.read()
# print(text)


# import json
# with open("data/limits.json", mode = "r", encoding = "utf-8") as file:
#     limits = json.load(file)
# print(limits)
# print(type(limits))
#
# import json
# uzivatel = {
#     "jmeno": "Anna",
#     "vek": 21,
#     "obor": "Biomedicinske inzenyrstvi",
# }
# with open("data/uzivatel.json", mode = "w", encoding = "utf-8") as file:
#     json.dump(uzivatel, file, indent = 4)
# with open("data/uzivatel.json", mode = "r", encoding = "utf-8") as file:
#     ner = json.load(file)
# print(ner)


with open("data/measurements.csv", mode = "r", encoding = "utf-8") as file:
    text = file.readlines()
    for row in text:
        divided_rows = row.split(";")
print(row)
import json
with open("data/limits.json", mode = "r", encoding = "utf-8") as file:
    limits = json.load(file)
print(limits)
with open("data/risk_patients.csv", mode = "w", encoding = "utf-8") as file:
