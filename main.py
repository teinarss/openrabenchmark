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

bleed_files = ['bleed-0Pathfinder.csv', 'bleed-1Pathfinder.csv', 'bleed-2Pathfinder.csv', 'bleed-3Pathfinder.csv', 'bleed-4Pathfinder.csv']
baseline_files = ['no-flags-class-0Pathfinder.csv', 'no-flags-class-1Pathfinder.csv', 'no-flags-class-2Pathfinder.csv', 'no-flags-class-3Pathfinder.csv', 'no-flags-class-4Pathfinder.csv']
pr_files = ['no-flags-struct-0Pathfinder.csv', 'no-flags-struct-1Pathfinder.csv', 'no-flags-struct-2Pathfinder.csv',  'no-flags-struct-3Pathfinder.csv',  'no-flags-struct-4Pathfinder.csv']
flag_files = ['flags-struct-0Pathfinder.csv', 'flags-struct-1Pathfinder.csv', 'flags-struct-2Pathfinder.csv',  'flags-struct-3Pathfinder.csv',  'flags-struct-4Pathfinder.csv']
opti_files = ['flags-struct-opti-0Pathfinder.csv', 'flags-struct-opti-1Pathfinder.csv', 'flags-struct-opti-2Pathfinder.csv',  'flags-struct-opti-3Pathfinder.csv',  'flags-struct-opti-4Pathfinder.csv']
more_opi = ['more-opi-0Pathfinder.csv', 'more-opi-1Pathfinder.csv', 'more-opi-2Pathfinder.csv',  'more-opi-3Pathfinder.csv',  'more-opi-4Pathfinder.csv']
more_opi1 = ['more-opi1-0Pathfinder.csv', 'more-opi1-1Pathfinder.csv', 'more-opi1-2Pathfinder.csv',  'more-opi1-3Pathfinder.csv',  'more-opi1-4Pathfinder.csv']


bleed_tree_files = ['bleed-tree-0Pathfinder.csv', 'bleed-tree-1Pathfinder.csv', 'bleed-tree-2Pathfinder.csv']
pr_tree_files = ['pr-tree-0Pathfinder.csv', 'pr-tree-1Pathfinder.csv', 'pr-tree-2Pathfinder.csv']


def getFileNames(file, count):
    res = []
    for x in range(count):
        res.append(file.format(x))

    return res

def readData(files):
    li = []
    for filename in files:
        df = pd.read_csv(logsPath + filename, index_col=None, header=0, usecols=['time [ms]'])
        li.append(df)

    return pd.concat(li, axis=0, ignore_index=True)

# m_bleed_files = getFileNames('bleed1-{}Pathfinder.csv', 5)
# pr_files = getFileNames('pr1-{}Pathfinder.csv', 5)


m_bleed_files = getFileNames('bleed-renderble-{}tick_time.csv', 5)
pr_files = getFileNames('pr-renderble-{}tick_time.csv', 5)

print(len(m_bleed_files))
bleed = readData(m_bleed_files)
pr = readData(pr_files)




# df = pd.read_csv('render_new3.csv', usecols = ['time'])
# kwargs = dict(alpha=0.5, bins=100, density=True, stacked=True)
# df1 = pd.read_csv('render_old1.csv')
# print(baseline.size)
# print(baseline.head(5))
# print(baseline.tail(5))

#fig, ax = plt.subplots()
log = True
#baseline = baseline.astype(float)
plt.figure(figsize=(20,10)); 
bins=np.linspace(0.001, 60.001, 200)
#bins = 'auto'
plt.hist(bleed['time [ms]'], color='tab:red', label='Bleed',stacked=True, alpha=0.5,bins=bins, log=log)

# plt.hist(baseline['time [ms]'], color='tab:red', label='Class',stacked=True, alpha=0.5,bins=bins, log=log)
plt.hist(pr['time [ms]'], color='tab:blue', label='pr', stacked=True, alpha=0.5,bins=bins, log=log)
# plt.hist(flag['time [ms]'], color='tab:green', label='Struct w flag', stacked=True, alpha=0.5,bins=bins, log=log)
#plt.hist(opti['time [ms]'], color='tab:blue', label='Struct w flag opti', stacked=True, alpha=0.5,bins=bins, log=log)
#plt.hist(m_opti1['time [ms]'], color='tab:red', label='moar', stacked=True, alpha=0.5,bins=bins, log=log)

# ax = baseline.plot(kind='hist', label='baseline', color='tab:red', figsize=(20,10), stacked=True, alpha=0.5,bins=np.linspace(0.001, 30.001, 50), log=True); 
# pr.plot(kind='hist', label='pr',color='tab:blue', ax=ax, stacked=True, alpha=0.5, bins=np.linspace(0.001, 30.001, 50), log=True); 
# plt.xlim(50,75)
# plt.legend();
plt.legend();
plt.show()
