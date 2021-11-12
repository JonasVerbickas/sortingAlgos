import pandas as pd
import matplotlib.pyplot as plt
from random import randint
from time import perf_counter

import sortingAlgos

ITERATIONS = 50
N = 100
N_INCREMENT = 50
ALGOS = [sorted, sortingAlgos.bubble, sortingAlgos.insertion]

def timeListSort(l, algo):
    starting_time = perf_counter()
    sorted_arr = algo(l)
    time_taken = perf_counter() - starting_time
    return time_taken

def generateAndSortAList(n):
    l = [randint(0, n) for x in range(n)]
    all_times = {}
    for algo in ALGOS:
        time_taken = timeListSort(l, algo)
        all_times[str(algo)] = time_taken
    return all_times

def saveAndPlotDF(df):
    df.to_csv("test.csv", index=False)
    print("Created .csv")
    for col in df.columns:
        if col != 'N':
            df.plot(x='N', y=col, kind = 'scatter')
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