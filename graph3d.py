from matplotlib import pyplot as plt
import numpy as np
import csv
from scipy.fft import fft, fftfreq
from scipy.interpolate import interp1d
from mpl_toolkits import mplot3d

vepp4_bpms = ["STP0", "STP2", "STP4",
              "SRP1", "SRP2", "SRP3", "SRP4", "SRP5", "SRP6", "SRP7", "SRP8", "SRP9",
              "SIP1", "SIP2",
              "SRP10", "SRP11", "SRP12", "SRP13", "SRP14", "SRP15", "SRP16", "SRP17",
              "SEP5", "SEP4", "SEP3", "SEP1", "SEP0",
              "NEP0", "NEP1", "NEP3", "NEP4", "NEP5",
              "NRP17", "NRP16", "NRP15", "NRP14", "NRP13", "NRP12", "NRP11", "NRP10",
              "NIP3", "NIP1",
              "NRP9", "NRP8", "NRP7", "NRP6", "NRP5", "NRP4", "NRP3", "NRP2", "NRP1",
              "NTP4", "NTP2", "NTP0"]


def read_data(bpm, channel):
    with open("data_recs/graph3d/"+bpm+"_"+channel+".log") as f:
        reader = csv.reader(f, delimiter=',')
        data_read = np.array([[float((row[0])), float(row[1])] for row in reader])
        return data_read.transpose()


def calc_step(x):
    steps = x[1:] - x[:-1]
    return np.percentile(steps, 50)


def calc_fft(t, x, spline_kind='linear'):
    # t, x - input data
    # N - number of sample points
    step = calc_step(np.array(t))
    N = int((t[-1] - t[0]) // step)
    x_sample, step = np.linspace(t[0], t[-1], N, retstep=True)

    if spline_kind is None:
        y_sample = x
    else:
        f = interp1d(t, x, kind=spline_kind)
        y_sample = f(x_sample)

    yf = 2.0 * np.abs(fft(y_sample, norm="forward"))[:N // 2]
    xf = fftfreq(N, step)[:N // 2]
    return xf, yf


channel = "x"
num_interp = 500
length = len(vepp4_bpms)
num_cut = 2

if __name__ == "__main__":
    X = np.linspace(0, 240, num_interp)[num_cut:]
    Y = np.linspace(1, length, length, endpoint=True)
    X, Y = np.meshgrid(X, Y)
    Z = np.zeros((length, num_interp - num_cut))
    i: int = 0
    for bpm in vepp4_bpms:
        x, y = read_data(bpm, channel)
        xf, yf = calc_fft(x, y)
        f = interp1d(xf, yf, kind='linear')
        yf = f(X[vepp4_bpms.index(bpm)])
        Z[i] = yf
        i += 1

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot_surface(X, Y, Z, rstride=1, cstride=10, cmap='viridis',
                    linewidth=0, antialiased=True)
    plt.show()
