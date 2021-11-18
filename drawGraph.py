import pandas as pd
import matplotlib.pyplot as plt
from random import randint
from time import perf_counter

import sortingAlgos

ITERATIONS = 30
N = 1000
N_INCREMENT = 500
ALGOS = [sortingAlgos.merge, sorted]

def timeListSort(l, algo):
    starting_time = perf_counter()
    sorted_arr = algo(l)
    time_taken = perf_counter() - starting_time
    return time_taken, sorted_arr

def generateAndSortAList(n):
    l = [randint(0, n) for x in range(n)]
    all_times = {}
    sorted_lists = {}
    for algo in ALGOS:
        time_taken, sorted_arr = timeListSort(l, algo)
        all_times[str(algo)] = time_taken
        sorted_lists[str(algo)] = sorted_arr
    # for index, val in enumerate(sorted_lists.values()):
    #     if index > 0:
    #         if val != sorted_lists.values()[index]:
    #             raise RuntimeError("Lists don't match")
    return all_times

def saveAndPlotDF(df):
    df = df.set_index('N')
    df.to_csv("test.csv")
    print("Created .csv")
    df.plot(ylabel='Time', legend=True)
    plt.show()

def collectSortTimes():
    global N
    df = pd.DataFrame()
    for i in range(ITERATIONS):
        if i % 10 == 0:
            print("i = ", i)
        all_times = generateAndSortAList(N)
        d = {'N': N, **all_times}
        df = df.append(d, ignore_index=True)
        N += N_INCREMENT
    return df

if __name__ == "__main__":
    loop_start = perf_counter()
    df = collectSortTimes()
    loop_end = perf_counter()
    print(f"{loop_end - loop_start = }")
    saveAndPlotDF(df)
