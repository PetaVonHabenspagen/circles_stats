# print(bin(89))
# print(int('01011001', 2))

# age = 25
# price = 19.99
# is_student = True
# name = "Alice"
#
# print(type(is_student))
# print(isinstance(price, int))
# print(isinstance(name, str))


# age = int("25")
# next_year = age + 1
# print(next_year)

# text ="Hello你好 مرحبПривет 🐍"
# print(len(text))
#
# print(ord("z"))
#
# name = "alice"
# name = name.upper()
# print(name)
#
# patient_id = "P12345"
# patient_id = patient_id.replace("P", "ID")
# print(patient_id)
#
# original_name = "JAN NOVÁK"
# lowercase = original_name.lower()
# print(lowercase)

# value = "123"
# value = int(value)
# print(type(value))
# print(isinstance(value, str))
# print(isinstance(value, int))
# print(value + 1)
#
# age_text = "25"
# age = int(age_text)
# print(type(age_text))
# print(type(age))
# print(age + 5)
#
# price_text = "19.99"
# price = float(price_text)
# print(type(price_text))
# print(type(price))
# print(isinstance(price, int))
# print(isinstance(price_text, str))
# print(price * 2)
#
# score = 100
# print(type(score))
# message = "Skóre:" + str(score)
# print(type(message))
# print(message)
#
# jmeno = input("Zadejte své jméno: ")
# print(f"Ahoj, {jmeno}!")

# print("=== Registrace pacienta ===")
# name = input("Jméno: ")
# if name == "":
#     print("Nezadal jsi nic!")
# age = input("Věk: ")
# allergies = input("Alergie (oddělené čárkou): ")
# age = int(age)
# print(f"\nPacient: {name}")
# print(f"Věk: {age} let")
# print(f"Rok narození: {2026 - age}")
# print(f"Alergie: {allergies}")

# temperature = "98.5"
# temp = float(temperature)
# celsius = (temp - 32) * (5/9)
# print(f"Teplota {temperature} °F je {round(celsius*100)/100} °C")
#
# message = "Let's learn more about Python!"
# print(message)
# length = len(message)
# print(f"Text má {length} znaků")


# birth_num = "0508150830"
# if len(birth_num) == 10:
#     print("Délka rodného čísla je správná")
# else:
#     print(f"Chyba: očekáváno 10 číslic, nalezeno pouze {len(birth_num)}")
#
# heslo = input("Vaše heslo: ")
# delka = len(heslo)
# print(f"Tvoje heslo má {delka} znaků")
# if delka < 8:
#     print("Heslo je příliš krátké!")
#
# greeting = "Dobrý den"
# name = "Karle"
# message = greeting + ", " + name + "!"
# print(message)
#
# user_name = input("Zadej své jméno: ")
# message = "Vítej, " + user_name + "!"
# print(message)
# name = "Staropramen"
# detachment = "JIP"
# print("=" * 21)
# print(f"[{name}] - [{detachment}]")
# print("=" * 21)
#
# name = "Jan"
# age = 25
# message = f"Ahoj, jmenuji se {name} a je mi {age} let."
# print(message)
#
# a = 10
# b = 5
# print(f"Součet: {a + b}")
# print(f"Rozdíl: {a - b}")
# print(f"Je a větší než b?: {a > b}")
# print(f"Délka jména: {len('Python')} znaků")
#
# bmi_weight = 75
# bmi_height = 1.80
#
# print(f"BMI: {bmi_weight / (bmi_height ** 2):.1f}")

# name = input("Jméno: ")
# weight = float(input("Váha (kg): "))
# height = float(input("Výška (m): "))
# bmi = weight / (height ** 2)
# if bmi < 18.5:
#     category = "podváha"
# elif bmi < 25:
#     category = "optimální"
# elif bmi < 30:
#     category = "nadváha"
# else:
#     category = "obezita"
# print(f"Vaše kategorie: {category}")

# sys = float(input("Systolický tlak: "))
# dia = float(input("Diastolický tlak: "))
# MAP = (sys +2 * dia) / 3
# vysledek = f"MAP: {MAP:.1f} mmHg"
# print(vysledek)

# word = "Python"
#
# for i in [0, 2, 4]:
#     print(f"Znak na indexu {i}: {word[i]}")
# for i in range(len(word)):
#     print(f"Index {i}: {word[i]}")
#
# school = "Hogwarts"
# print(school[3])
# for i in [1, 3, 5, 7]:
#     print(f"Index {i}: {school[i]}")
#
# text = "Slytherin beats Gryffindor"
# team = text[0:9]
# team = text[:9]
# rest = text[9:]
# print(team)
# print(rest)
#
# text = "0123456789"
# print(text[::2])
# print(text[::-1])
# print(text[::-2])
#
# print(text[1:8:2])
# print(text[2:9:3])
#
# dna = "ACGTTAGCTA"
# first_codon = dna[0:3]
# reversed_dna = dna[::-1]
# print(f"První kodon: {first_codon}")
# print(f"Reverzní sekvence: {reversed_dna}")

# rod_cislo = input("Vaše rodné číslo: ")
# mesic = rod_cislo[3:4]
# rok = rod_cislo[:2]
# den = rod_cislo[4:6]
# print(f"Datum narození: {den}.{mesic}.{rok}")

# text = "Programming"
# for i in range(0, len(text), 2):
#     print(text[i])
#
# text1 = "Hello World"
# count = 0
# for char in text1:
#     if char.islower():
#         count += 1
# print(f"Počet malých písmen v textu: {count}")

# text2 = "Banana"
# counta = 0
# for charc in text2:
#     if charc == "a":
#         counta += 1
# print(f"Počet písmen 'a': {counta}")
# print(text2.count("a"))
#
#
# dna = "ACGTTAGCTA"
# GC = 0
# for i in dna:
#     if i == "G" or i == "C":
#         GC += 1
# print(f"GC Obsah: {GC} znaků")

# name = "severus snape"
# print(name.upper())
# print(name.lower())
# print(name.isupper())
# print(name.islower())
# print(name.upper().isupper())
#
# name = "alice"
# print(name.upper())

# text = "Python is amazing. Python is fun!"
# position = text.find("amazing")
# position1 = text.find("Java")
# print(position, position1)
# new_text = text.replace("Python", "Programming")
# print(new_text)
#
# count = text.count("Python")
# print(count)
#
# sentence = "Jablko,Hruška,Banán"
# fruits = sentence.split(",")
# print(fruits)
#
# words = ["Python", "je", "super"]
# sentence = " ".join(words)
# print(sentence)

# data_line = "Jan Novák,35,120/80,72,36.6"
# values = data_line.split(",")
# print(values)
#
# name = values[0]
# age = int(values[1])
# blood_pressure = values[2]
# heart_rate = int(values[3])
# temperature = float(values[4])
#
# print(f"Pacient: {name}, věk {age} let")
# print(f"TK: {blood_pressure} mmHg, TF: {heart_rate} BPM")
# print(f"Teplota: {temperature} °C")


# new_record = ["Marie Svobodová", "42", "115/75", "68", "36.8"]
# csv_line = ",".join(new_record)
# print(csv_line)
#
# text = "   Hello   "
# text2 = "."
# print(text.strip() + text2)
# print(text.lstrip() + text2)
# print(text.rstrip() + text2)

text = "Python"
vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count += 1
    print(f"Kontroluji: {char}, počet samohlásek: {count}")

print(f"Celkem samohlásek: {count}")