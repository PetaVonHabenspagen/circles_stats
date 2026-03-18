import signal_plot_ops as spo

spo.load_signal_from_txt("ekg_signal.txt")
spo.signal_min([7, 5, 6, 7, 2])
spo.plot_signal([4, 7, 2, 3], [8, 6, 4, 2])