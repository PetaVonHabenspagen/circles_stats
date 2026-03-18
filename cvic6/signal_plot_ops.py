def load_signal_from_txt(path):
    vratit = []
    with open(path, mode = "r", encoding = "utf-8") as file:
        content = file.read()
        vrat = content.split("\n")
    print(vrat)
def signal_min(values):
    return print(min(values))
def signal_max(values):
    return print(max(values))
def signal_avg(values):
    return print(sum(values) / len(values))
def plot_signal(values, values1):
    import matplotlib.pyplot as plt
    plt.plot(values, values1)
    return plt.show()

if __name__ == "__main__":
    signal_min([4, 5, 6])
    signal_max([7, 8, 9])
    signal_avg([1, 2, 3])
    plot_signal([7, 8, 9], [4, 5, 6])
    load_signal_from_txt("ekg_signal.txt")