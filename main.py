import heartpy as hp
import matplotlib.pyplot as plt
import pandas as pd
sample_rate = 250

data = hp.get_data('ECG4.txt')

plt.figure(figsize=(12,4))
plt.plot(data)
plt.show()

wd, m = hp.process(data, sample_rate)

#visualise in plot of custom size
plt.figure(figsize=(12,4))
hp.plotter(wd, m)
df = pd.DataFrame()
#display computed measures

for measure in m.keys():
    print('%s: %f' %(measure, m[measure]))
    df[measure] =  m[measure]