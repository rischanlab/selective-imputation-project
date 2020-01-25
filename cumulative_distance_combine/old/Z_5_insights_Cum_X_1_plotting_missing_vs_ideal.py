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


input_file4 = 'results/cum_sim_missing_a_m_vs_ideal.csv'
input_file5 = 'results/cum_div_missing_a_m_vs_ideal.csv'

output_plot = 'cum_10_missing_attributes_vs_ideal'

# ===============================================================
# IDEAL VS STANDARD


df4 = pd.read_csv(input_file4, names=['percentage','k','Cumulative_distance'])

percent = 10

kj41 = df4[(df4['k'] == 1) & (df4['percentage'] == percent)]
kj41 = kj41['Cumulative_distance']

kj42 = df4[(df4['k'] == 2) & (df4['percentage'] == percent)]
kj42 = kj42['Cumulative_distance']

kj43 = df4[(df4['k'] == 3) & (df4['percentage'] == percent)]
kj43 = kj43['Cumulative_distance']

kj44 = df4[(df4['k'] == 4) & (df4['percentage'] == percent)]
kj44 = kj44['Cumulative_distance'] 

kj45 = df4[(df4['k'] == 5) & (df4['percentage'] == percent)]
kj45 = kj45['Cumulative_distance']

kj46 = df4[(df4['k'] == 6) & (df4['percentage'] == percent)]
kj46 = kj46['Cumulative_distance']

kj47 = df4[(df4['k'] == 7) & (df4['percentage'] == percent)]
kj47 = kj47['Cumulative_distance']

kj48 = df4[(df4['k'] == 8) & (df4['percentage'] == percent)]
kj48 = kj48['Cumulative_distance']

kj49 = df4[(df4['k'] == 9) & (df4['percentage'] == percent)]
kj49 = kj49['Cumulative_distance']

kj410 = df4[(df4['k'] == 10) & (df4['percentage'] == percent)]
kj410 = kj410['Cumulative_distance']

kj411 = df4[(df4['k'] == 11) & (df4['percentage'] == percent)]
kj411 = kj411['Cumulative_distance']

kj412 = df4[(df4['k'] == 12) & (df4['percentage'] == percent)]
kj412 = kj412['Cumulative_distance']

kj413 = df4[(df4['k'] == 13) & (df4['percentage'] == percent)]
kj413 = kj413['Cumulative_distance']

kj420 = df4[(df4['k'] == 20) & (df4['percentage'] == percent)]
kj420 = kj420['Cumulative_distance']

kj430 = df4[(df4['k'] == 30) & (df4['percentage'] == percent)]
kj430 = kj430['Cumulative_distance']

kj440 = df4[(df4['k'] == 40) & (df4['percentage'] == percent)]
kj440 = kj440['Cumulative_distance']


kj450 = df4[(df4['k'] == 50) & (df4['percentage'] == percent)]
kj450 = kj450['Cumulative_distance']
kj460 = df4[(df4['k'] == 60) & (df4['percentage'] == percent)]
kj460 = kj460['Cumulative_distance']

kj466 = df4[(df4['k'] == 66) & (df4['percentage'] == percent)]
kj466 = kj466['Cumulative_distance']

kj4192 = df4[(df4['k'] == 192) & (df4['percentage'] == percent)]
kj4192 = kj4192['Cumulative_distance']


kj41 = list(mean_confidence_interval(kj41))
kj41.insert(0,1)
kj41.insert(1,'Cumulative_distance')

kj42 = list(mean_confidence_interval(kj42))
kj42.insert(0,2)
kj42.insert(1,'Cumulative_distance')

kj43 = list(mean_confidence_interval(kj43))
kj43.insert(0,3)
kj43.insert(1,'Cumulative_distance')

kj44 = list(mean_confidence_interval(kj44))
kj44.insert(0,4)
kj44.insert(1,'Cumulative_distance')

kj45 = list(mean_confidence_interval(kj45))
kj45.insert(0,5)
kj45.insert(1,'Cumulative_distance')

kj46 = list(mean_confidence_interval(kj46))
kj46.insert(0,6)
kj46.insert(1,'Cumulative_distance')

kj47 = list(mean_confidence_interval(kj47))
kj47.insert(0,7)
kj47.insert(1,'Cumulative_distance')

kj48 = list(mean_confidence_interval(kj48))
kj48.insert(0,8)
kj48.insert(1,'Cumulative_distance')

kj49 = list(mean_confidence_interval(kj49))
kj49.insert(0,9)
kj49.insert(1,'Cumulative_distance')

kj410 = list(mean_confidence_interval(kj410))
kj410.insert(0,10)
kj410.insert(1,'Cumulative_distance')

kj411 = list(mean_confidence_interval(kj411))
kj411.insert(0,11)
kj411.insert(1,'Cumulative_distance')

kj412 = list(mean_confidence_interval(kj412))
kj412.insert(0,12)
kj412.insert(1,'Cumulative_distance')

kj413 = list(mean_confidence_interval(kj413))
kj413.insert(0,13)
kj413.insert(1,'Cumulative_distance')

kj420 = list(mean_confidence_interval(kj420))
kj420.insert(0,20)
kj420.insert(1,'Cumulative_distance')

kj430 = list(mean_confidence_interval(kj430))
kj430.insert(0,30)
kj430.insert(1,'Cumulative_distance')

kj440 = list(mean_confidence_interval(kj440))
kj440.insert(0,40)
kj440.insert(1,'Cumulative_distance')

kj450 = list(mean_confidence_interval(kj450))
kj450.insert(0,50)
kj450.insert(1,'Cumulative_distance')

kj460 = list(mean_confidence_interval(kj460))
kj460.insert(0,60)
kj460.insert(1,'Cumulative_distance')

kj466 = list(mean_confidence_interval(kj466))
kj466.insert(0,66)
kj466.insert(1,'Cumulative_distance')

kj4192 = list(mean_confidence_interval(kj4192))
kj4192.insert(0,192)
kj4192.insert(1,'Cumulative_distance')

df4 = pd.DataFrame([kj45,  kj410,  kj420, kj450, kj4192])
df4.columns = ['k','measurement','mean','lb','ub']


df5 = pd.read_csv(input_file5, names=['percentage','k','Cumulative_distance'])


kj51 = df5[(df5['k'] == 1) & (df5['percentage'] == percent)]
kj51 = kj51['Cumulative_distance']

kj52 = df5[(df5['k'] == 2) & (df5['percentage'] == percent)]
kj52 = kj52['Cumulative_distance']

kj53 = df5[(df5['k'] == 3) & (df5['percentage'] == percent)]
kj53 = kj53['Cumulative_distance']

kj54 = df5[(df5['k'] == 4) & (df5['percentage'] == percent)]
kj54 = kj54['Cumulative_distance'] 

kj55 = df5[(df5['k'] == 5) & (df5['percentage'] == percent)]
kj55 = kj55['Cumulative_distance']

kj56 = df5[(df5['k'] == 6) & (df5['percentage'] == percent)]
kj56 = kj56['Cumulative_distance']

kj57 = df5[(df5['k'] == 7) & (df5['percentage'] == percent)]
kj57 = kj57['Cumulative_distance']

kj58 = df5[(df5['k'] == 8) & (df5['percentage'] == percent)]
kj58 = kj58['Cumulative_distance']

kj59 = df5[(df5['k'] == 9) & (df5['percentage'] == percent)]
kj59 = kj59['Cumulative_distance']

kj510 = df5[(df5['k'] == 10) & (df5['percentage'] == percent)]
kj510 = kj510['Cumulative_distance']

kj511 = df5[(df5['k'] == 11) & (df5['percentage'] == percent)]
kj511 = kj511['Cumulative_distance']

kj512 = df5[(df5['k'] == 12) & (df5['percentage'] == percent)]
kj512 = kj512['Cumulative_distance']

kj513 = df5[(df5['k'] == 13) & (df5['percentage'] == percent)]
kj513 = kj513['Cumulative_distance']

kj520 = df5[(df5['k'] == 20) & (df5['percentage'] == percent)]
kj520 = kj520['Cumulative_distance']

kj530 = df5[(df5['k'] == 30) & (df5['percentage'] == percent)]
kj530 = kj530['Cumulative_distance']

kj540 = df5[(df5['k'] == 40) & (df5['percentage'] == percent)]
kj540 = kj540['Cumulative_distance']


kj550 = df5[(df5['k'] == 50) & (df5['percentage'] == percent)]
kj550 = kj550['Cumulative_distance']
kj560 = df5[(df5['k'] == 60) & (df5['percentage'] == percent)]
kj560 = kj560['Cumulative_distance']

kj566 = df5[(df5['k'] == 66) & (df5['percentage'] == percent)]
kj566 = kj566['Cumulative_distance']

kj5192 = df5[(df5['k'] == 192) & (df5['percentage'] == percent)]
kj5192 = kj5192['Cumulative_distance']


kj51 = list(mean_confidence_interval(kj51))
kj51.insert(0,1)
kj51.insert(1,'Cumulative_distance')

kj52 = list(mean_confidence_interval(kj52))
kj52.insert(0,2)
kj52.insert(1,'Cumulative_distance')

kj53 = list(mean_confidence_interval(kj53))
kj53.insert(0,3)
kj53.insert(1,'Cumulative_distance')

kj54 = list(mean_confidence_interval(kj54))
kj54.insert(0,4)
kj54.insert(1,'Cumulative_distance')

kj55 = list(mean_confidence_interval(kj55))
kj55.insert(0,5)
kj55.insert(1,'Cumulative_distance')

kj56 = list(mean_confidence_interval(kj56))
kj56.insert(0,6)
kj56.insert(1,'Cumulative_distance')

kj57 = list(mean_confidence_interval(kj57))
kj57.insert(0,7)
kj57.insert(1,'Cumulative_distance')

kj58 = list(mean_confidence_interval(kj58))
kj58.insert(0,8)
kj58.insert(1,'Cumulative_distance')

kj59 = list(mean_confidence_interval(kj59))
kj59.insert(0,9)
kj59.insert(1,'Cumulative_distance')

kj510 = list(mean_confidence_interval(kj510))
kj510.insert(0,10)
kj510.insert(1,'Cumulative_distance')

kj511 = list(mean_confidence_interval(kj511))
kj511.insert(0,11)
kj511.insert(1,'Cumulative_distance')

kj512 = list(mean_confidence_interval(kj512))
kj512.insert(0,12)
kj512.insert(1,'Cumulative_distance')

kj513 = list(mean_confidence_interval(kj513))
kj513.insert(0,13)
kj513.insert(1,'Cumulative_distance')

kj520 = list(mean_confidence_interval(kj520))
kj520.insert(0,20)
kj520.insert(1,'Cumulative_distance')

kj530 = list(mean_confidence_interval(kj530))
kj530.insert(0,30)
kj530.insert(1,'Cumulative_distance')

kj540 = list(mean_confidence_interval(kj540))
kj540.insert(0,40)
kj540.insert(1,'Cumulative_distance')

kj550 = list(mean_confidence_interval(kj550))
kj550.insert(0,50)
kj550.insert(1,'Cumulative_distance')

kj560 = list(mean_confidence_interval(kj560))
kj560.insert(0,60)
kj560.insert(1,'Cumulative_distance')

kj566 = list(mean_confidence_interval(kj566))
kj566.insert(0,66)
kj566.insert(1,'Cumulative_distance')

kj5192 = list(mean_confidence_interval(kj5192))
kj5192.insert(0,192)
kj5192.insert(1,'Cumulative_distance')

df5 = pd.DataFrame([kj55, kj510, kj520, kj550, kj5192])
df5.columns = ['k','measurement','mean','lb','ub']






mean4 = df4[df4['measurement'] == 'Cumulative_distance'].reset_index()
mean4 = mean4['mean']
ub4 = df4[df4['measurement'] == 'Cumulative_distance'].reset_index()
ub4 = ub4['ub']
lb4 = df4[df4['measurement'] == 'Cumulative_distance'].reset_index()
lb4 = lb4['lb']

mean5 = df5[df5['measurement'] == 'Cumulative_distance'].reset_index()
mean5 = mean5['mean']
ub5 = df5[df5['measurement'] == 'Cumulative_distance'].reset_index()
ub5 = ub5['ub']
lb5 = df5[df5['measurement'] == 'Cumulative_distance'].reset_index()
lb5 = lb5['lb']


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


t = np.arange(len(mean4))

_, ax = plt.subplots()
# Plot the data, set the linewidth, color and transparency of the
# line, provide a label for the legend
ax.plot(mean4, lw = 1, color = '#ece554', alpha = 1, label = 'Similarity to reference', marker='s', linestyle='--', linewidth=2, markersize=12)
ax.plot(mean5, lw = 1, color = '#0d0e0f', alpha = 1, label = 'Deviation/outstanding', marker='x', linestyle='-.', linewidth=2, markersize=12)


# Shade the confidence interval
ax.fill_between(t, lb4, ub4, color = '#ffff80', alpha = 0.4)
ax.fill_between(t, lb5, ub5, color = '#87888a', alpha = 0.4)


# Label the axes and provide a title
ax.set_title("Impact of k on Effectiveness, 95% CI, 10 % missing")
ax.set_xlabel("k")
ax.set_ylabel("Effectiveness Cumulative distance - Missing to Ideal")
x = [5,10,20,50,192]
xi = list(range(len(x)))
plt.xticks(xi, x)
ax.invert_yaxis()
# Display legend
ax.set_ylim(ymin=0.5)
ax.set_ylim(ymax=1.0)

ax.legend(loc='best')

plt.savefig('plot/' + output_plot + '.svg', format="svg", dpi = 1000)
plt.savefig('plot/' + output_plot + '.png')
plt.show()
