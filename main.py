import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# import time
# import matplotlib.pyplot as plt
# import datetime
# import numpy as np
# import gc

# combine all runs for a target to one DF
#df = np.genfromtxt('old.csv', delimiter=',')[:1]

# df = pd.read_csv('cpu_new2.csv')
# df1 = pd.read_csv('cpu_old1.csv')
baseline_files = ['C:/Users/Tomas.PYTTEMJUK/Documents/OpenRA/Logs/baseline-0Pathfinder.csv', 'C:/Users/Tomas.PYTTEMJUK/Documents/OpenRA/Logs/baseline-1Pathfinder.csv', 'C:/Users/Tomas.PYTTEMJUK/Documents/OpenRA/Logs/baseline-2Pathfinder.csv', 'C:/Users/Tomas.PYTTEMJUK/Documents/OpenRA/Logs/baseline-3Pathfinder.csv', 'C:/Users/Tomas.PYTTEMJUK/Documents/OpenRA/Logs/baseline-4Pathfinder.csv']
pr_files = ['C:/Users/Tomas.PYTTEMJUK/Documents/OpenRA/Logs/pr-0Pathfinder.csv', 'C:/Users/Tomas.PYTTEMJUK/Documents/OpenRA/Logs/pr-1Pathfinder.csv', 'C:/Users/Tomas.PYTTEMJUK/Documents/OpenRA/Logs/pr-2Pathfinder.csv', 'C:/Users/Tomas.PYTTEMJUK/Documents/OpenRA/Logs/pr-3Pathfinder.csv', 'C:/Users/Tomas.PYTTEMJUK/Documents/OpenRA/Logs/pr-4Pathfinder.csv']

def readData(files):
    li = []
    for filename in files:
        df = pd.read_csv(filename, index_col=None, header=0, usecols=['time [ms]'])
        li.append(df)

    return pd.concat(li, axis=0, ignore_index=True)

baseline = readData(baseline_files)
pr = readData(pr_files)
# df = pd.read_csv('render_new3.csv', usecols = ['time'])

# df1 = pd.read_csv('render_old1.csv')
print(baseline.size)
print(baseline.head(5))
print(baseline.tail(5))

#baseline = baseline.astype(float)
# plt.figure(); 


ax = baseline.plot(kind='hist', label='baseline', color='tab:red', figsize=(20,10), stacked=True, alpha=0.5,bins=np.linspace(0.001, 30.001, 50), log=True); 
pr.plot(kind='hist', label='pr',color='tab:blue', ax=ax, stacked=True, alpha=0.5, bins=np.linspace(0.001, 30.001, 50), log=True); 
plt.legend();
plt.show()
