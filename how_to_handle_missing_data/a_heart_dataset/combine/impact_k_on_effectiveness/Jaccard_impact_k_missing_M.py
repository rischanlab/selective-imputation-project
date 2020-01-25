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

input_file1 = 'results/drop_rows_missing_measures_vs_ideal.csv'
input_file2 = 'results/ignore_cells_missing_measures_vs_ideal.csv'
input_file3 = 'results/median_impute_missing_measures_vs_ideal.csv'
input_file4 = 'results/mode_impute_missing_measures_vs_ideal.csv'


output_plot = 'Jaccard_10_missing_measures_vs_ideal'

# ===============================================================
# IDEAL VS STANDARD

df1 = pd.read_csv(input_file1, names=['percentage','k','RBO','Jaccard'])

percent = 10
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
kj160 = df1[(df1['k'] == 80) & (df1['percentage'] == percent)]
kj160 = kj160['Jaccard']

kj166 = df1[(df1['k'] == 100) & (df1['percentage'] == percent)]
kj166 = kj166['Jaccard']

kj1192 = df1[(df1['k'] == 192) & (df1['percentage'] == percent)]
kj1192 = kj1192['Jaccard']


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
kj160.insert(0,80)
kj160.insert(1,'Jaccard')

kj166 = list(mean_confidence_interval(kj166))
kj166.insert(0,100)
kj166.insert(1,'Jaccard')

kj1192 = list(mean_confidence_interval(kj1192))
kj1192.insert(0,192)
kj1192.insert(1,'Jaccard')

df1 = pd.DataFrame([kj15, kj110, kj113, kj120, kj150, kj160, kj166, kj1192])
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

kj250 = df2[(df2['k'] == 80) & (df2['percentage'] == percent)]
kj250 = kj250['Jaccard']
kj260 = df2[(df2['k'] == 80) & (df2['percentage'] == percent)]
kj260 = kj260['Jaccard']

kj266 = df2[(df2['k'] == 100) & (df2['percentage'] == percent)]
kj266 = kj266['Jaccard']

kj2192 = df2[(df2['k'] == 192) & (df2['percentage'] == percent)]
kj2192 = kj2192['Jaccard']



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
kj260.insert(0,80)
kj260.insert(1,'Jaccard')

kj266 = list(mean_confidence_interval(kj266))
kj266.insert(0,100)
kj266.insert(1,'Jaccard')

kj2192 = list(mean_confidence_interval(kj2192))
kj2192.insert(0,192)
kj2192.insert(1,'Jaccard')

df2 = pd.DataFrame([kj25, kj210, kj213, kj220, kj250, kj260, kj266, kj2192])
df2.columns = ['k','measurement','mean','lb','ub']


df3 = pd.read_csv(input_file3, names=['percentage','k','RBO','Jaccard'])


kj35 = df3[(df3['k'] == 5) & (df3['percentage'] == percent)]
kj35 = kj35['Jaccard']

kj310 = df3[(df3['k'] == 10) & (df3['percentage'] == percent)]
kj310 = kj310['Jaccard']

kj313 = df3[(df3['k'] == 15) & (df3['percentage'] == percent)]
kj313 = kj313['Jaccard']

kj320 = df3[(df3['k'] == 20) & (df3['percentage'] == percent)]
kj320 = kj320['Jaccard']


kj350 = df3[(df3['k'] == 80) & (df3['percentage'] == percent)]
kj350 = kj350['Jaccard']
kj360 = df3[(df3['k'] == 80) & (df3['percentage'] == percent)]
kj360 = kj360['Jaccard']

kj366 = df3[(df3['k'] == 50) & (df3['percentage'] == percent)]
kj366 = kj366['Jaccard']

kj3192 = df3[(df3['k'] == 192) & (df3['percentage'] == percent)]
kj3192 = kj3192['Jaccard']



kj35 = list(mean_confidence_interval(kj35))
kj35.insert(0,5)
kj35.insert(1,'Jaccard')


kj310 = list(mean_confidence_interval(kj310))
kj310.insert(0,10)
kj310.insert(1,'Jaccard')

kj313 = list(mean_confidence_interval(kj313))
kj313.insert(0,15)
kj313.insert(1,'Jaccard')

kj320 = list(mean_confidence_interval(kj320))
kj320.insert(0,20)
kj320.insert(1,'Jaccard')

kj350 = list(mean_confidence_interval(kj350))
kj350.insert(0,50)
kj350.insert(1,'Jaccard')

kj360 = list(mean_confidence_interval(kj360))
kj360.insert(0,80)
kj360.insert(1,'Jaccard')

kj366 = list(mean_confidence_interval(kj366))
kj366.insert(0,100)
kj366.insert(1,'Jaccard')

kj3192 = list(mean_confidence_interval(kj3192))
kj3192.insert(0,192)
kj3192.insert(1,'Jaccard')

df3 = pd.DataFrame([kj35, kj310, kj313, kj320, kj350, kj360, kj366, kj3192])
df3.columns = ['k','measurement','mean','lb','ub']



df4 = pd.read_csv(input_file4, names=['percentage','k','RBO','Jaccard'])


kj45 = df4[(df4['k'] == 5) & (df4['percentage'] == percent)]
kj45 = kj45['Jaccard']

kj410 = df4[(df4['k'] == 10) & (df4['percentage'] == percent)]
kj410 = kj410['Jaccard']

kj413 = df4[(df4['k'] == 15) & (df4['percentage'] == percent)]
kj413 = kj413['Jaccard']

kj420 = df4[(df4['k'] == 20) & (df4['percentage'] == percent)]
kj420 = kj420['Jaccard']


kj450 = df4[(df4['k'] == 80) & (df4['percentage'] == percent)]
kj450 = kj450['Jaccard']
kj460 = df4[(df4['k'] == 50) & (df4['percentage'] == percent)]
kj460 = kj460['Jaccard']

kj466 = df4[(df4['k'] == 100) & (df4['percentage'] == percent)]
kj466 = kj466['Jaccard']

kj4192 = df4[(df4['k'] == 192) & (df4['percentage'] == percent)]
kj4192 = kj4192['Jaccard']



kj45 = list(mean_confidence_interval(kj45))
kj45.insert(0,5)
kj45.insert(1,'Jaccard')


kj410 = list(mean_confidence_interval(kj410))
kj410.insert(0,10)
kj410.insert(1,'Jaccard')

kj413 = list(mean_confidence_interval(kj413))
kj413.insert(0,15)
kj413.insert(1,'Jaccard')

kj420 = list(mean_confidence_interval(kj420))
kj420.insert(0,20)
kj420.insert(1,'Jaccard')

kj450 = list(mean_confidence_interval(kj450))
kj450.insert(0,50)
kj450.insert(1,'Jaccard')

kj460 = list(mean_confidence_interval(kj460))
kj460.insert(0,80)
kj460.insert(1,'Jaccard')

kj466 = list(mean_confidence_interval(kj466))
kj466.insert(0,100)
kj466.insert(1,'Jaccard')

kj4192 = list(mean_confidence_interval(kj4192))
kj4192.insert(0,192)
kj4192.insert(1,'Jaccard')

df4 = pd.DataFrame([kj45, kj410, kj413, kj420, kj450, kj460, kj366, kj4192])
df4.columns = ['k','measurement','mean','lb','ub']


mean4 = df4[df4['measurement'] == 'Jaccard'].reset_index()
mean4 = mean4['mean']
ub4 = df4[df4['measurement'] == 'Jaccard'].reset_index()
ub4 = ub4['ub']
lb4 = df4[df4['measurement'] == 'Jaccard'].reset_index()
lb4 = lb4['lb']


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
ax.plot(mean2, lw = 1, color = '#b65332', alpha = 1, label = 'Ignore missing cells', marker='<', linestyle='-', linewidth=2, markersize=12)
ax.plot(mean3, lw = 1, color = '#5be19a', alpha = 1, label = 'Impute using median + most frequent', marker='o', linestyle='-', linewidth=2, markersize=12)
ax.plot(mean4, lw = 1, color = '#ece554', alpha = 1, label = 'Impute using most frequent', marker='s', linestyle='--', linewidth=2, markersize=12)


# Shade the confidence interval
ax.fill_between(t, lb1, ub1, color = '#539caf', alpha = 0.4)
ax.fill_between(t, lb2, ub2, color = '#b65332', alpha = 0.4)
ax.fill_between(t, lb3, ub3, color = '#5be19a', alpha = 0.4)
ax.fill_between(t, lb4, ub4, color = '#ffff80', alpha = 0.4)


# Label the axes and provide a title
ax.set_title("Impact of k on Effectiveness, 10 % missing on M")
ax.set_xlabel("k")
ax.set_ylabel("Jaccard- missingTopK to idealTopK")
x = [5, 10, 15, 20, 50, 80, 100, 192]
xi = list(range(len(x)))
plt.xticks(xi, x)
# Display legend
ax.set_ylim(ymin=0.0)
ax.set_ylim(ymax=1.1)

ax.legend(loc='best')

plt.savefig('plot/' + output_plot + '.svg', format="svg", dpi = 1000)
plt.savefig('plot/' + output_plot + '.png')
plt.show()
