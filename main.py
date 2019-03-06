import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# import time
# import matplotlib.pyplot as plt
# import datetime
# import numpy as np
# import gc

df = pd.read_csv('new.csv').drop_duplicates()
df1 = pd.read_csv('old.csv').drop_duplicates()
print(df.size)
print(df.head(5))

# plt.figure(); 
ax = df.plot(kind='hist', x='tick', y='time', label='new', color='tab:red', figsize=(20,10), stacked=True, alpha=0.5,bins=np.linspace(0.001, 15.001, 50), log=True); 
df1.plot(kind='hist', x='tick', y='time', label='old',color='tab:blue', ax=ax, stacked=True, alpha=0.5, bins=np.linspace(0.001, 15.001, 50), log=True); 
plt.show()