import math
import numpy as np
import matplotlib.pyplot as plt

def measure_time(f, n):
    import time
    start_time = time.time()
    res = f(n)
    end_time = time.time()
    return end_time-start_time, res

def compute_time(fn, start, stop, regression='exponential'): 
    n = np.arange(start, stop, 1)
    t = []
    for v in n:
        time, fib = measure_time(fn, v)
        t.append(time)
    t = np.array(t)

    if regression == "linear":
        polyfit = np.polyfit(n, t, 1)
    elif regression == "exponential":
        polyfit = np.polyfit(n, np.log(t), 1)

    r = []
    for v in n:
        if regression == "linear":
            r.append(polyfit[0]*v + polyfit[1]) 
        elif regression == "exponential":
            r.append(math.e**polyfit[1] * math.e**(polyfit[0]*v))
    r = np.array(r)
    return n, t, r, polyfit

def time_plot(n, r, t, regression, polyfit):
    fig, ax = plt.subplots()

    ax.set(xlabel='n', ylabel='time (s)', title='Time measurement for function call')
    ax.grid()

    if regression == "linear":
        eq = "y={:.3f}x+{:.3f}".format(polyfit[0], polyfit[1])
    elif regression == "exponential":
        eq = "y={:.3f}e^{:.3f}x".format(math.e**polyfit[0], polyfit[1])

    ax.plot(n, t, label="time plot")
    ax.plot(n, r, label=eq)

    plt.legend()

    fig.savefig("test.png")
    plt.show()
