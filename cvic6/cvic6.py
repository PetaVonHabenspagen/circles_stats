# def convert_coins(value, from_currency, to_currency):
#     if from_currency == "gold" and to_currency == "gems":
#         return value / 100
#     if from_currency == "gems" and to_currency == "gold":
#         return value * 100
#     return value
# print(convert_coins(value=6000, from_currency="gold", to_currency="gems"))
#
# def compute_score_delta(score, baseline, multiplier=1.0, round_to=2):
#     return round((score - baseline) * multiplier, round_to)
# print(compute_score_delta(1574, 1400, 1.4, 0))
#
# def normalize_signal(values, min_value = 0, max_value = 1):
#     low = min(values)
#     high = max(values)
#     scale = high - low
#     return [min_value + (v - low) * (max_value - min_value) / scale for v in values]
# print(normalize_signal([2, 4, 6], max_value=100))
# # print(normalize_signal([2, 4, 6], 0, 100))
#
#
# def basic_stats(values):
#     return min(values), max(values), round(sum(values) / len(values), 2)
# min_v, max_v, avg_v, = basic_stats([1200, 980, 1430, 1600, 890])
# print(min_v, max_v, avg_v)
#
# stats = basic_stats([1200, 980, 1430, 1600, 890])
# print(stats)
# print(stats[0])
# print(stats[1])
# print(stats[2])
#
# avg_only = basic_stats([1200, 980, 1430, 1600, 890])[2]
# print(avg_only)
#
#
# default_round = 2
# def round_value(value):
#     return round(value, default_round)
#
# print(round(14.7894))
#
# player_name = "GlobalPlayer"
# def show_player():
#     player_name = "LocalPlayer"
#     print("Ve funkci:", player_name)
#
# show_player()
# print("mimo_funkci:", player_name)
#
# counter = 10
# def increment_bad():
#     global counter
#     counter += 1
#     return counter
# print(increment_bad())

