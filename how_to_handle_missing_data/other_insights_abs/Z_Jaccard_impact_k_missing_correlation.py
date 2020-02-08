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

input_file1 = 'results/drop_missing_correlation_missing_vs_ideal_abs.csv'
input_file2 = 'results/impute_correlation_missing_vs_ideal_abs.csv'


output_plot = 'correlation_Jaccard_50_vs_ideal'

# ===============================================================
# IDEAL VS STANDARD

df1 = pd.read_csv(input_file1, names=['percentage','k','RBO','Jaccard'])

percent = 50
#[5, 10, 15, 20, 100, 256]


kj15 = df1[(df1['k'] == 5) & (df1['percentage'] == percent)]
kj15 = kj15['Jaccard']

kj110 = df1[(df1['k'] == 10) & (df1['percentage'] == percent)]
kj110 = kj110['Jaccard']

kj113 = df1[(df1['k'] == 15) & (df1['percentage'] == percent)]
kj113 = kj113['Jaccard']

kj120 = df1[(df1['k'] == 20) & (df1['percentage'] == percent)]
kj120 = kj120['Jaccard']

kj150 = df1[(df1['k'] == 50) & (df1['percentage'] == percent)]
kj150 = kj150['Jaccard']
kj160 = df1[(df1['k'] == 60) & (df1['percentage'] == percent)]
kj160 = kj160['Jaccard']

kj178 = df1[(df1['k'] == 78) & (df1['percentage'] == percent)]
kj178 = kj178['Jaccard']



kj15 = list(mean_confidence_interval(kj15))
kj15.insert(0,5)
kj15.insert(1,'Jaccard')

kj110 = list(mean_confidence_interval(kj110))
kj110.insert(0,10)
kj110.insert(1,'Jaccard')

kj113 = list(mean_confidence_interval(kj113))
kj113.insert(0,15)
kj113.insert(1,'Jaccard')

kj120 = list(mean_confidence_interval(kj120))
kj120.insert(0,20)
kj120.insert(1,'Jaccard')

kj150 = list(mean_confidence_interval(kj150))
kj150.insert(0,50)
kj150.insert(1,'Jaccard')

kj160 = list(mean_confidence_interval(kj160))
kj160.insert(0,60)
kj160.insert(1,'Jaccard')

kj178 = list(mean_confidence_interval(kj178))
kj178.insert(0,78)
kj178.insert(1,'Jaccard')

df1 = pd.DataFrame([kj15, kj110, kj113, kj120, kj150, kj160, kj178])
df1.columns = ['k','measurement','mean','lb','ub']


df2 = pd.read_csv(input_file2, names=['percentage','k','RBO','Jaccard'])



kj25 = df2[(df2['k'] == 5) & (df2['percentage'] == percent)]
kj25 = kj25['Jaccard']

kj210 = df2[(df2['k'] == 10) & (df2['percentage'] == percent)]
kj210 = kj210['Jaccard']


kj213 = df2[(df2['k'] == 15) & (df2['percentage'] == percent)]
kj213 = kj213['Jaccard']

kj220 = df2[(df2['k'] == 20) & (df2['percentage'] == percent)]
kj220 = kj220['Jaccard']

kj250 = df2[(df2['k'] == 50) & (df2['percentage'] == percent)]
kj250 = kj250['Jaccard']
kj260 = df2[(df2['k'] == 60) & (df2['percentage'] == percent)]
kj260 = kj260['Jaccard']

kj278 = df2[(df2['k'] == 78) & (df2['percentage'] == percent)]
kj278 = kj278['Jaccard']



kj25 = list(mean_confidence_interval(kj25))
kj25.insert(0,5)
kj25.insert(1,'Jaccard')

kj210 = list(mean_confidence_interval(kj210))
kj210.insert(0,10)
kj210.insert(1,'Jaccard')

kj213 = list(mean_confidence_interval(kj213))
kj213.insert(0,15)
kj213.insert(1,'Jaccard')

kj220 = list(mean_confidence_interval(kj220))
kj220.insert(0,20)
kj220.insert(1,'Jaccard')

kj250 = list(mean_confidence_interval(kj250))
kj250.insert(0,50)
kj250.insert(1,'Jaccard')

kj260 = list(mean_confidence_interval(kj260))
kj260.insert(0,60)
kj260.insert(1,'Jaccard')

kj278 = list(mean_confidence_interval(kj278))
kj278.insert(0,78)
kj278.insert(1,'Jaccard')


df2 = pd.DataFrame([kj25, kj210, kj213, kj220, kj250, kj260, kj278])
df2.columns = ['k','measurement','mean','lb','ub']




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
ax.plot(mean1, lw = 1, color = '#539caf', alpha = 1, label = 'Drop rows contain missing', marker='x', linestyle='-.', linewidth=2, markersize=12)
ax.plot(mean2, lw = 1, color = '#b65332', alpha = 1, label = 'Impute using median', marker='<', linestyle='-', linewidth=2, markersize=12)

# Shade the confidence interval
ax.fill_between(t, lb1, ub1, color = '#539caf', alpha = 0.4)
ax.fill_between(t, lb2, ub2, color = '#b65332', alpha = 0.4)

# Label the axes and provide a title
ax.set_title("Impact of k on Effectiveness, 50 % missing correlation")
ax.set_xlabel("k")
ax.set_ylabel("Jaccard - missingTopK to idealTopK")
x = [5,10,15,20,50,60,75]
xi = list(range(len(x)))
plt.xticks(xi, x)
# Display legend
ax.set_ylim(ymin=0.0)
ax.set_ylim(ymax=1.1)

ax.legend(loc='best')

plt.savefig('plot/' + output_plot + '.svg', format="svg", dpi = 1000)
plt.savefig('plot/' + output_plot + '.png')
plt.show()
