import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy.stats
def mean_confidence_interval(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    return m, m-h, m+h

input_file1 = 'aggregate/div_missing_attributes_vs_ideal.csv'
input_file2 = 'aggregate/sim_missing_attributes_vs_ideal.csv'
input_file3 = 'aggregate/div_missing_zipf_attributes_vs_ideal.csv'
input_file4 = 'aggregate/sim_missing_zipf_attributes_vs_ideal.csv'


output_plot = 'jaccard_all_percentage_missing_attributes_vs_ideal'

# ===============================================================
# IDEAL VS STANDARD
df = pd.read_csv(input_file1, names=['percentage','k','RBO','Jaccard'])

dfj100 = df[(df['k'] == 5) & (df['percentage'] == 0)]
dfj100 = dfj100['Jaccard']

dfj110 = df[(df['k'] == 5) & (df['percentage'] == 10)]
dfj110 = dfj110['Jaccard']

dfj120 = df[(df['k'] == 5) & (df['percentage'] == 20)]
dfj120 = dfj120['Jaccard']

dfj130 = df[(df['k'] == 5) & (df['percentage'] == 30)]
dfj130 = dfj130['Jaccard']

dfj100 = list(mean_confidence_interval(dfj100))
dfj100.insert(0,0)
dfj100.insert(1,'Jaccard')

dfj110 = list(mean_confidence_interval(dfj110))
dfj110.insert(0,10)
dfj110.insert(1,'Jaccard')

dfj120 = list(mean_confidence_interval(dfj120))
dfj120.insert(0,20)
dfj120.insert(1,'Jaccard')

dfj130 = list(mean_confidence_interval(dfj130))
dfj130.insert(0,30)
dfj130.insert(1,'Jaccard')


df = pd.read_csv(input_file2, names=['percentage','k','RBO','Jaccard'])


dfj200 = df[(df['k'] == 5) & (df['percentage'] == 0)]
dfj200 = dfj200['Jaccard']

dfj210 = df[(df['k'] == 5) & (df['percentage'] == 10)]
dfj210 = dfj210['Jaccard']

dfj220 = df[(df['k'] == 5) & (df['percentage'] == 20)]
dfj220 = dfj220['Jaccard']

dfj230 = df[(df['k'] == 5) & (df['percentage'] == 30)]
dfj230 = dfj230['Jaccard']

dfj200 = list(mean_confidence_interval(dfj200))
dfj200.insert(0,0)
dfj200.insert(1,'Jaccard')

dfj210 = list(mean_confidence_interval(dfj210))
dfj210.insert(0,10)
dfj210.insert(1,'Jaccard')

dfj220 = list(mean_confidence_interval(dfj220))
dfj220.insert(0,20)
dfj220.insert(1,'Jaccard')

dfj230 = list(mean_confidence_interval(dfj230))
dfj230.insert(0,30)
dfj230.insert(1,'Jaccard')

df = pd.read_csv(input_file3, names=['percentage','k','RBO','Jaccard'])


dfj300 = df[(df['k'] == 5) & (df['percentage'] == 0)]
dfj300 = dfj300['Jaccard']

dfj310 = df[(df['k'] == 5) & (df['percentage'] == 10)]
dfj310 = dfj310['Jaccard']

dfj320 = df[(df['k'] == 5) & (df['percentage'] == 20)]
dfj320 = dfj320['Jaccard']

dfj330 = df[(df['k'] == 5) & (df['percentage'] == 30)]
dfj330 = dfj330['Jaccard']

dfj300 = list(mean_confidence_interval(dfj300))
dfj300.insert(0,0)
dfj300.insert(1,'Jaccard')

dfj310 = list(mean_confidence_interval(dfj310))
dfj310.insert(0,10)
dfj310.insert(1,'Jaccard')

dfj320 = list(mean_confidence_interval(dfj320))
dfj320.insert(0,20)
dfj320.insert(1,'Jaccard')

dfj330 = list(mean_confidence_interval(dfj330))
dfj330.insert(0,30)
dfj330.insert(1,'Jaccard')

df = pd.read_csv(input_file4, names=['percentage','k','RBO','Jaccard'])



dfj400 = df[(df['k'] == 5) & (df['percentage'] == 0)]
dfj400 = dfj400['Jaccard']

dfj410 = df[(df['k'] == 5) & (df['percentage'] == 10)]
dfj410 = dfj410['Jaccard']

dfj420 = df[(df['k'] == 5) & (df['percentage'] == 20)]
dfj420 = dfj420['Jaccard']

dfj430 = df[(df['k'] == 5) & (df['percentage'] == 30)]
dfj430 = dfj430['Jaccard']

dfj400 = list(mean_confidence_interval(dfj400))
dfj400.insert(0,0)
dfj400.insert(1,'Jaccard')

dfj410 = list(mean_confidence_interval(dfj410))
dfj410.insert(0,10)
dfj410.insert(1,'Jaccard')

dfj420 = list(mean_confidence_interval(dfj420))
dfj420.insert(0,20)
dfj420.insert(1,'Jaccard')

dfj430 = list(mean_confidence_interval(dfj430))
dfj430.insert(0,30)
dfj430.insert(1,'Jaccard')



df1 = pd.DataFrame([dfj100, dfj110, dfj120, dfj130])
df1.columns = ['k','measurement','mean','lb','ub']
df2 = pd.DataFrame([dfj200, dfj210, dfj220, dfj230])
df2.columns = ['k','measurement','mean','lb','ub']
df3 = pd.DataFrame([dfj300, dfj310, dfj320, dfj330])
df3.columns = ['k','measurement','mean','lb','ub']
df4 = pd.DataFrame([dfj400, dfj410, dfj420, dfj430])
df4.columns = ['k','measurement','mean','lb','ub']


mean1 = df1[df1['measurement'] == 'Jaccard'].reset_index()
mean1 = mean1['mean']
ub1 = df1[df1['measurement'] == 'Jaccard'].reset_index()
ub1 = ub1['ub']
lb1 = df1[df1['measurement'] == 'Jaccard'].reset_index()
lb1 = lb1['lb']

mean2 = df2[df2['measurement'] == 'Jaccard'].reset_index()
mean2 = mean2['mean']
ub2 = df2[df2['measurement'] == 'Jaccard'].reset_index()
ub2 = ub2['ub']
lb2 = df2[df2['measurement'] == 'Jaccard'].reset_index()
lb2 = lb2['lb']

mean3 = df3[df3['measurement'] == 'Jaccard'].reset_index()
mean3 = mean3['mean']
ub3 = df3[df3['measurement'] == 'Jaccard'].reset_index()
ub3 = ub3['ub']
lb3 = df3[df3['measurement'] == 'Jaccard'].reset_index()
lb3 = lb3['lb']

mean4 = df4[df4['measurement'] == 'Jaccard'].reset_index()
mean4 = mean4['mean']
ub4 = df4[df4['measurement'] == 'Jaccard'].reset_index()
ub4 = ub4['ub']
lb4 = df4[df4['measurement'] == 'Jaccard'].reset_index()
lb4 = lb4['lb']

# Set some parameters to apply to all plots. These can be overridden
# in each plot if desired
import matplotlib
# Plot size to 14" x 7"
matplotlib.rc('figure', figsize = (14, 14))
# Font size to 14
matplotlib.rc('font', size = 25)
# Do not display top and right frame lines
matplotlib.rc('axes.spines', top = False, right = False)
# Remove grid lines
matplotlib.rc('axes', grid = False)
# Set backgound color to white
matplotlib.rc('axes', facecolor = 'white')


t = np.arange(len(mean1))

_, ax = plt.subplots()
# Plot the data, set the linewidth, color and transparency of the
# line, provide a label for the legend
ax.plot(mean1, lw = 1, color = '#539caf', alpha = 1, label = 'Deviation missing random', marker='x', linestyle='-.', linewidth=2, markersize=12)
ax.plot(mean2, lw = 1, color = '#b65332', alpha = 1, label = 'Sim missing random', marker='<', linestyle='-', linewidth=2, markersize=12)
#ax.plot(mean3, lw = 1, color = '#5be19a', alpha = 1, label = 'Deviation zipf missing', marker='o', linestyle='-', linewidth=2, markersize=12)
#ax.plot(mean4, lw = 1, color = '#ece554', alpha = 1, label = 'Sim zipf missing', marker='s', linestyle='--', linewidth=2, markersize=12)

# Shade the confidence interval
ax.fill_between(t, lb1, ub1, color = '#539caf', alpha = 0.4)
ax.fill_between(t, lb2, ub2, color = '#b65332', alpha = 0.4)
#ax.fill_between(t, lb3, ub3, color = '#5be19a', alpha = 0.4)
#ax.fill_between(t, lb4, ub4, color = '#ffff80', alpha = 0.4)


# Label the axes and provide a title
ax.set_title("Impact missing on Effectiveness (Jaccard), 95% CI, k = 5")
ax.set_xlabel("percentage of missing")
ax.set_ylabel("Effectiveness - Missing A to Ideal")
x = [0, 10, 20, 30]
xi = list(range(len(x)))
plt.xticks(xi, x)
# Display legend
ax.set_ylim(ymin=0.0)
ax.set_ylim(ymax=1.01)

ax.legend(loc='best')

plt.savefig('plot/' + output_plot + '.svg', format="svg", dpi = 1000)
plt.savefig('plot/' + output_plot + '.png')
plt.show()
