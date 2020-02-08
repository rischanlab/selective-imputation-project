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

input_file1 = 'results/missing_a_m_vs_ideal_small_missing.csv'



output_plot = 'small_missing_percentage_a_m_vs_ideal'

k = 10
# ===============================================================
# IDEAL VS STANDARD
df = pd.read_csv(input_file1, names=['percentage','k','RBO','Jaccard'])

dfj100 = df[(df['k'] == k) & (df['percentage'] == 0)]
dfj100 = dfj100['Jaccard']

dfj110 = df[(df['k'] == k) & (df['percentage'] == 1)]
dfj110 = dfj110['Jaccard']

dfj120 = df[(df['k'] == k) & (df['percentage'] == 2)]
dfj120 = dfj120['Jaccard']

dfj130 = df[(df['k'] == k) & (df['percentage'] == 3)]
dfj130 = dfj130['Jaccard']

dfj140 = df[(df['k'] == k) & (df['percentage'] == 4)]
dfj140 = dfj140['Jaccard']

dfj150 = df[(df['k'] == k) & (df['percentage'] == 5)]
dfj150 = dfj150['Jaccard']

dfj160 = df[(df['k'] == k) & (df['percentage'] == 6)]
dfj160 = dfj160['Jaccard']

dfj170 = df[(df['k'] == k) & (df['percentage'] == 7)]
dfj170 = dfj170['Jaccard']

dfj180 = df[(df['k'] == k) & (df['percentage'] == 8)]
dfj180 = dfj180['Jaccard']

dfj190 = df[(df['k'] == k) & (df['percentage'] == 9)]
dfj190 = dfj190['Jaccard']

dfj1100 = df[(df['k'] == k) & (df['percentage'] == 10)]
dfj1100 = dfj1100['Jaccard']



dfj100 = list(mean_confidence_interval(dfj100))
dfj100.insert(0,0)
dfj100.insert(1,'Jaccard')

dfj110 = list(mean_confidence_interval(dfj110))
dfj110.insert(0,1)
dfj110.insert(1,'Jaccard')

dfj120 = list(mean_confidence_interval(dfj120))
dfj120.insert(0,2)
dfj120.insert(1,'Jaccard')

dfj130 = list(mean_confidence_interval(dfj130))
dfj130.insert(0,3)
dfj130.insert(1,'Jaccard')

dfj140 = list(mean_confidence_interval(dfj140))
dfj140.insert(0,4)
dfj140.insert(1,'Jaccard')

dfj150 = list(mean_confidence_interval(dfj150))
dfj150.insert(0,5)
dfj150.insert(1,'Jaccard')

dfj160 = list(mean_confidence_interval(dfj160))
dfj160.insert(0,6)
dfj160.insert(1,'Jaccard')

dfj170 = list(mean_confidence_interval(dfj170))
dfj170.insert(0,7)
dfj170.insert(1,'Jaccard')

dfj180 = list(mean_confidence_interval(dfj180))
dfj180.insert(0,8)
dfj180.insert(1,'Jaccard')

dfj190 = list(mean_confidence_interval(dfj190))
dfj190.insert(0,9)
dfj190.insert(1,'Jaccard')

dfj1100 = list(mean_confidence_interval(dfj1100))
dfj1100.insert(0,10)
dfj1100.insert(1,'Jaccard')


df1 = pd.DataFrame([dfj100, dfj110, dfj120, dfj130, dfj140, dfj150, dfj160, dfj170, dfj180, dfj190, dfj1100])
df1.columns = ['k','measurement','mean','lb','ub']


mean1 = df1[df1['measurement'] == 'Jaccard'].reset_index()
mean1 = mean1['mean']
ub1 = df1[df1['measurement'] == 'Jaccard'].reset_index()
ub1 = ub1['ub']
lb1 = df1[df1['measurement'] == 'Jaccard'].reset_index()
lb1 = lb1['lb']


df = pd.read_csv(input_file1, names=['percentage','k','RBO','Jaccard'])

dfj100 = df[(df['k'] == k) & (df['percentage'] == 0)]
dfj100 = dfj100['RBO']

dfj110 = df[(df['k'] == k) & (df['percentage'] == 1)]
dfj110 = dfj110['RBO']

dfj120 = df[(df['k'] == k) & (df['percentage'] == 2)]
dfj120 = dfj120['RBO']

dfj130 = df[(df['k'] == k) & (df['percentage'] == 3)]
dfj130 = dfj130['RBO']

dfj140 = df[(df['k'] == k) & (df['percentage'] == 4)]
dfj140 = dfj140['RBO']

dfj150 = df[(df['k'] == k) & (df['percentage'] == 5)]
dfj150 = dfj150['RBO']

dfj160 = df[(df['k'] == k) & (df['percentage'] == 6)]
dfj160 = dfj160['RBO']

dfj170 = df[(df['k'] == k) & (df['percentage'] == 7)]
dfj170 = dfj170['RBO']

dfj180 = df[(df['k'] == k) & (df['percentage'] == 8)]
dfj180 = dfj180['RBO']

dfj190 = df[(df['k'] == k) & (df['percentage'] == 9)]
dfj190 = dfj190['RBO']

dfj1100 = df[(df['k'] == k) & (df['percentage'] == 10)]
dfj1100 = dfj1100['RBO']



dfj100 = list(mean_confidence_interval(dfj100))
dfj100.insert(0,0)
dfj100.insert(1,'RBO')

dfj110 = list(mean_confidence_interval(dfj110))
dfj110.insert(0,1)
dfj110.insert(1,'RBO')

dfj120 = list(mean_confidence_interval(dfj120))
dfj120.insert(0,2)
dfj120.insert(1,'RBO')

dfj130 = list(mean_confidence_interval(dfj130))
dfj130.insert(0,3)
dfj130.insert(1,'RBO')

dfj140 = list(mean_confidence_interval(dfj140))
dfj140.insert(0,4)
dfj140.insert(1,'RBO')

dfj150 = list(mean_confidence_interval(dfj150))
dfj150.insert(0,5)
dfj150.insert(1,'RBO')

dfj160 = list(mean_confidence_interval(dfj160))
dfj160.insert(0,6)
dfj160.insert(1,'RBO')

dfj170 = list(mean_confidence_interval(dfj170))
dfj170.insert(0,7)
dfj170.insert(1,'RBO')

dfj180 = list(mean_confidence_interval(dfj180))
dfj180.insert(0,8)
dfj180.insert(1,'RBO')

dfj190 = list(mean_confidence_interval(dfj190))
dfj190.insert(0,9)
dfj190.insert(1,'RBO')

dfj1100 = list(mean_confidence_interval(dfj1100))
dfj1100.insert(0,10)
dfj1100.insert(1,'RBO')



df2 = pd.DataFrame([dfj100, dfj110, dfj120, dfj130, dfj140, dfj150, dfj160, dfj170, dfj180, dfj190, dfj1100])
df2.columns = ['k','measurement','mean','lb','ub']


mean2 = df2[df2['measurement'] == 'RBO'].reset_index()
mean2 = mean2['mean']
ub2 = df2[df2['measurement'] == 'RBO'].reset_index()
ub2 = ub2['ub']
lb2 = df2[df2['measurement'] == 'RBO'].reset_index()
lb2 = lb2['lb']

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
ax.plot(mean1, lw = 1, color = '#539caf', alpha = 1, label = 'Jaccard', marker='x', linestyle='-.', linewidth=2, markersize=12)
ax.plot(mean2, lw = 1, color = '#b65332', alpha = 1, label = 'RBO', marker='<', linestyle='-', linewidth=2, markersize=12)
# ax.plot(mean3, lw = 1, color = '#5be19a', alpha = 1, label = 'Impute using median + most frequent', marker='o', linestyle='-', linewidth=2, markersize=12)
# ax.plot(mean4, lw = 1, color = '#ece554', alpha = 1, label = 'Impute using most frequent', marker='s', linestyle='--', linewidth=2, markersize=12)



# Shade the confidence interval
ax.fill_between(t, lb1, ub1, color = '#539caf', alpha = 0.4)
ax.fill_between(t, lb2, ub2, color = '#b65332', alpha = 0.4)
# ax.fill_between(t, lb3, ub3, color = '#5be19a', alpha = 0.4)
# ax.fill_between(t, lb4, ub4, color = '#ffff80', alpha = 0.4)



# Label the axes and provide a title
ax.set_title("Impact missing on Deviation Effectiveness, k = 10")
ax.set_xlabel("percentage of missing on A + M")
ax.set_ylabel("Effectiveness - misingTopK to idealTopK")
x = [0,1,2,3,4,5,6,7,8,9,10]
xi = list(range(len(x)))
plt.xticks(xi, x)
# Display legend
ax.set_ylim(ymin=0.0)
ax.set_ylim(ymax=1.01)

ax.legend(loc='best')

plt.savefig('plot/' + output_plot + '.svg', format="svg", dpi = 1000)
plt.savefig('plot/' + output_plot + '.png')
plt.show()
