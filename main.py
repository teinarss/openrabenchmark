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
logsPath = 'C:/Users/Tomas.PYTTEMJUK/Documents/OpenRA/Logs/'

baseline_files = ['baseline-harv-0Pathfinder.csv', 'baseline-harv-1Pathfinder.csv', 'baseline-harv-2Pathfinder.csv', 'baseline-harv-3Pathfinder.csv', 'baseline-harv-4Pathfinder.csv']
pr_files = ['pr-harv-0Pathfinder.csv', 'pr-harv-1Pathfinder.csv', 'pr-harv-2Pathfinder.csv',  'pr-harv-3Pathfinder.csv',  'pr-harv-4Pathfinder.csv']

def readData(files):
    li = []
    for filename in files:
        df = pd.read_csv(logsPath + filename, index_col=None, header=0, usecols=['time [ms]'])
        li.append(df)

    return pd.concat(li, axis=0, ignore_index=True)

baseline = readData(baseline_files)
pr = readData(pr_files)
# df = pd.read_csv('render_new3.csv', usecols = ['time'])
# kwargs = dict(alpha=0.5, bins=100, density=True, stacked=True)
# df1 = pd.read_csv('render_old1.csv')
# print(baseline.size)
# print(baseline.head(5))
# print(baseline.tail(5))

#fig, ax = plt.subplots()

#baseline = baseline.astype(float)
plt.figure(figsize=(20,10)); 
bins=np.linspace(0.001, 40.001, 100)
#bins = 'auto'
plt.hist(baseline['time [ms]'], color='tab:red', label='Baseline',stacked=True, alpha=0.5,bins=bins, log=False)
plt.hist(pr['time [ms]'], color='tab:blue', label='PR', stacked=True, alpha=0.5,bins=bins, log=False)

# ax = baseline.plot(kind='hist', label='baseline', color='tab:red', figsize=(20,10), stacked=True, alpha=0.5,bins=np.linspace(0.001, 30.001, 50), log=True); 
# pr.plot(kind='hist', label='pr',color='tab:blue', ax=ax, stacked=True, alpha=0.5, bins=np.linspace(0.001, 30.001, 50), log=True); 
# plt.xlim(50,75)
# plt.legend();
plt.legend();
plt.show()
