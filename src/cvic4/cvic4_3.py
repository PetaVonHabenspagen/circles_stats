

# Ukol č. 1:
# try:
#     number_text = input("Zadej libovolné číslo:")
#     number = int(number_text)
#     print(number * 2)
# except ValueError:
#     print("Nezadal jsi číslo!")

# Úkol č. 2
#
# heart_rate = 120
# while heart_rate >= 60:
#     print(f"Tep: {heart_rate} bpm")
#     heart_rate -= 5
# print("Tep normalizován.")


# counter = 0
# while counter < 10:
#     print(counter)
#
#     if counter == 5:
#         print("Nalezeno číslo 5")
#         break
#     counter += 1
# print("konec")

# heart_rate = 70
# while True:
#     print(f"Tep: {heart_rate} bpm")
#
#     if heart_rate > 120:
#         print("Tachykardie!")
#         break
#     if heart_rate < 40:
#         print("Bradykardie!")
#         break
#     heart_rate_str = input("Vlož tep:")
#     try:
#         heart_rate = int(heart_rate_str)
#     except ValueError:
#         print("Neplatná hodnota tepu")
#         continue
# print("Stabilizováno lékařem")
#
# measurements = 0
# valid_count = 0
# while measurements < 10:
#     temp_str = input(f"Měření {measurements+1}/10 - Teplota: ")
#     measurements += 1
#     try:
#         temp = float(temp_str)
#     except ValueError:
#         print("Zadána neplatná hodnota")
#         continue
#     if temp < 35 or temp > 42:
#         print("Teplota mimo rozsah, ignoruji")
#         continue
#     valid_count += 1
#     print(f"Platné měření: {temp} °C")
# print(f"\nCelkem platných měření: {valid_count}/10")
# numbers = [4, 9, 5, 6, 8, 7, 2, 3]
# counter = len(numbers)
# while counter >= 0:
#     counter -= 1
#     try:
#         if numbers[counter] %3 == 0:
#             continue
#         if numbers[counter] == 7:
#             break
#         print(numbers[counter])
#         if numbers[counter] == 0:
#             print("koncim, došel seznam")
#     except ValueError:
#         print("Vložená hodnota v seznamu není číslo!")
# print("Konec, nalezeno 7")
# #
# mereni = ["EKG", "EEG", "EKG", "MRI", "EEG"]
# unikatni_mereni = set(mereni)
# print(unikatni_mereni)
# mereni_bez_duplikat = list(unikatni_mereni)
# print(mereni_bez_duplikat)


# #  Ukol  č. 5
# diagnozy = ["I10", "E11", "I10", "J45", "E11", "N39"]
# unikatni_diagnozy = set(diagnozy)
# print(unikatni_diagnozy)
# pocet = len(unikatni_diagnozy)
# print(pocet)
# if "J45" in diagnozy:
#     print("True")
#
#
# #  Ukol č. 6
# hashtagy_a = {"python", "programovani", "ai", "tips"}
# hashtagy_b = {"ai", "data", "python", "vizualizace"}
# sjednoceni = hashtagy_a | hashtagy_b
# print(sjednoceni)
# prunik = hashtagy_a & hashtagy_b
# print(prunik)
# rozdil = hashtagy_a - hashtagy_b
# print(rozdil)
# patient = {
#     "vitals": {
#         "temp": 37.2
#     }
# }
# print(patient["vitals"]["temp"])

#  Ukol č. 4
while True:
    rodne = input("Vlož své RČ:")
    soucet_sude = 0
    soucet_liche = 0
    rozdil = (soucet_liche)-(soucet_sude)
    rodne_str = str(rodne)
    for i in range(len(rodne_str)):
        if i %2 == 0:
            soucet_sude += int(i)
        if i == 0:
            soucet_liche += int(i)
        else:
            soucet_liche += int(i)
    if rodne == "Konec":
        break
    if len(rodne) != 10:
        print(f"RČ nemá 10 znaků.")
        continue
    if rodne.isdigit() == False:
        print(f"RČ obsahuje neplatný znak.")
        continue
    if rozdil %11 != 0:
        print(f"RČ není dělitelné 11.")
        continue
    print(f"Rodné číslo bylo přijato.")
print("Zadávání bylo ukončeno")