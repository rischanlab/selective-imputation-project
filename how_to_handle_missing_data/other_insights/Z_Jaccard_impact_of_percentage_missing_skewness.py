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

input_file1 = 'results/drop_missing_skewness_missing_vs_ideal_random.csv'
input_file2 = 'results/impute_skewness_missing_vs_ideal_random.csv'


output_plot = 'skewness_jaccard_all_percentage_missing'

k = 5
# ===============================================================
# IDEAL VS STANDARD
df = pd.read_csv(input_file1, names=['percentage','k','RBO','Jaccard'])

dfj100 = df[(df['k'] == k) & (df['percentage'] == 0)]
dfj100 = dfj100['Jaccard']

dfj110 = df[(df['k'] == k) & (df['percentage'] == 10)]
dfj110 = dfj110['Jaccard']

dfj120 = df[(df['k'] == k) & (df['percentage'] == 20)]
dfj120 = dfj120['Jaccard']

dfj130 = df[(df['k'] == k) & (df['percentage'] == 30)]
dfj130 = dfj130['Jaccard']

dfj140 = df[(df['k'] == k) & (df['percentage'] == 40)]
dfj140 = dfj140['Jaccard']

dfj150 = df[(df['k'] == k) & (df['percentage'] == 50)]
dfj150 = dfj150['Jaccard']

dfj160 = df[(df['k'] == k) & (df['percentage'] == 60)]
dfj160 = dfj160['Jaccard']

dfj170 = df[(df['k'] == k) & (df['percentage'] == 70)]
dfj170 = dfj170['Jaccard']

dfj180 = df[(df['k'] == k) & (df['percentage'] == 80)]
dfj180 = dfj180['Jaccard']

dfj190 = df[(df['k'] == k) & (df['percentage'] == 90)]
dfj190 = dfj190['Jaccard']



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

dfj140 = list(mean_confidence_interval(dfj140))
dfj140.insert(0,40)
dfj140.insert(1,'Jaccard')

dfj150 = list(mean_confidence_interval(dfj150))
dfj150.insert(0,50)
dfj150.insert(1,'Jaccard')

dfj160 = list(mean_confidence_interval(dfj160))
dfj160.insert(0,60)
dfj160.insert(1,'Jaccard')

dfj170 = list(mean_confidence_interval(dfj170))
dfj170.insert(0,70)
dfj170.insert(1,'Jaccard')

dfj180 = list(mean_confidence_interval(dfj180))
dfj180.insert(0,80)
dfj180.insert(1,'Jaccard')

dfj190 = list(mean_confidence_interval(dfj190))
dfj190.insert(0,90)
dfj190.insert(1,'Jaccard')



df = pd.read_csv(input_file2, names=['percentage','k','RBO','Jaccard'])


dfj200 = df[(df['k'] == k) & (df['percentage'] == 0)]
dfj200 = dfj200['Jaccard']

dfj210 = df[(df['k'] == k) & (df['percentage'] == 10)]
dfj210 = dfj210['Jaccard']

dfj220 = df[(df['k'] == k) & (df['percentage'] == 20)]
dfj220 = dfj220['Jaccard']

dfj230 = df[(df['k'] == k) & (df['percentage'] == 30)]
dfj230 = dfj230['Jaccard']

dfj240 = df[(df['k'] == k) & (df['percentage'] == 40)]
dfj240 = dfj240['Jaccard']

dfj250 = df[(df['k'] == k) & (df['percentage'] == 50)]
dfj250 = dfj250['Jaccard']

dfj260 = df[(df['k'] == k) & (df['percentage'] == 60)]
dfj260 = dfj260['Jaccard']

dfj270 = df[(df['k'] == k) & (df['percentage'] == 70)]
dfj270 = dfj270['Jaccard']

dfj280 = df[(df['k'] == k) & (df['percentage'] == 80)]
dfj280 = dfj280['Jaccard']

dfj290 = df[(df['k'] == k) & (df['percentage'] == 90)]
dfj290 = dfj290['Jaccard']



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

dfj240 = list(mean_confidence_interval(dfj240))
dfj240.insert(0,40)
dfj240.insert(1,'Jaccard')

dfj250 = list(mean_confidence_interval(dfj250))
dfj250.insert(0,50)
dfj250.insert(1,'Jaccard')

dfj260 = list(mean_confidence_interval(dfj260))
dfj260.insert(0,60)
dfj260.insert(1,'Jaccard')

dfj270 = list(mean_confidence_interval(dfj270))
dfj270.insert(0,70)
dfj270.insert(1,'Jaccard')

dfj280 = list(mean_confidence_interval(dfj280))
dfj280.insert(0,80)
dfj280.insert(1,'Jaccard')

dfj290 = list(mean_confidence_interval(dfj290))
dfj290.insert(0,90)
dfj290.insert(1,'Jaccard')





df1 = pd.DataFrame([dfj100, dfj110, dfj120, dfj130, dfj140, dfj150, dfj160, dfj170, dfj180, dfj190])
df1.columns = ['k','measurement','mean','lb','ub']
df2 = pd.DataFrame([dfj200, dfj210, dfj220, dfj230, dfj240, dfj250, dfj260, dfj270, dfj280, dfj290])
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
ax.set_title("Impact missing on Effectiveness (Jaccard), 95% CI, k = 5")
ax.set_xlabel("percentage of skewness missing")
ax.set_ylabel("Effectiveness - Missing to Ideal")
x = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
xi = list(range(len(x)))
plt.xticks(xi, x)
# Display legend
ax.set_ylim(ymin=0.0)
ax.set_ylim(ymax=1.01)

ax.legend(loc='best')

plt.savefig('plot/' + output_plot + '.svg', format="svg", dpi = 1000)
plt.savefig('plot/' + output_plot + '.png')
plt.show()
