import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
import random
import csv
import aggregate_insight as ag


def dropout(a, percent, seed):
    # create a copy
    mat = a.copy()
    # number of values to replace
    prop = int(mat.size * percent)
    # indices to mask
    random.seed(seed)
    mask = random.sample(range(mat.size), prop)
    # replace with NaN
    np.put(mat, mask, [np.NaN]*len(mask))
    return mat

def randZipf(n, alpha, numSamples, seed):
    # Calculate Zeta values from 1 to n:
    tmp = np.power( np.arange(1, n+1), -alpha )
    zeta = np.r_[0.0, np.cumsum(tmp)]
    # Store the translation map:
    distMap = [x / zeta[-1] for x in zeta]
    # Generate an array of uniform 0-1 pseudo-random values:
    np.random.seed(seed)
    u = np.random.random(numSamples)
    # bisect them with distMap
    v = np.searchsorted(distMap, u)
    samples = [t-1 for t in v]
    return samples

def percentage_missing_zipf(N_samples, alpha, seed):

    s = randZipf(10, alpha, N_samples, seed)
    unique, counts = np.unique(s, return_counts=True)
    d = dict(zip(unique, counts / N_samples))
    return d

def missing_data(db, N_samples, alpha, seed):
    # ['sex', 's6', 'age', 'bp', 's5', 's1', 's2', 'bmi', 's4', 's3']


    rank = percentage_missing_zipf(N_samples, alpha, seed)
    #print(rank)
    df = db.copy()

    s3 = df['s3'].values
    s3 = dropout(s3, rank[9], seed)

    s4 = df['s4'].values
    s4 = dropout(s4, rank[8], seed)


    bmi = df['bmi'].values
    bmi = dropout(bmi, rank[7], seed)

    s2 = df['s2'].values
    s2 = dropout(s2, rank[6], seed)

    s1 = df['s1'].values
    s1 = dropout(s1, rank[5], seed)

    s5 = df['s5'].values
    s5 = dropout(s5, rank[4], seed)

    bp = df['bp'].values
    bp = dropout(bp, rank[3], seed)

    s6 = df['s6'].values
    s6 = dropout(s6, rank[1], seed)

    sex = df['sex'].values
    sex = dropout(sex, rank[0], seed)

    age = df['age'].values
    age = dropout(age, rank[2], seed)

    frame = { 's3': s3, 
            's4': s4, 'bmi': bmi,
             's2': s2, 's1': s1,
             's5': s5, 'bp': bp,
             's6': s6, 'sex': sex, 
             'age': age   
            } 

    missing_zipf = pd.DataFrame(frame)
    return missing_zipf

diab_bunch = load_diabetes()

df = pd.DataFrame(diab_bunch.data, columns = diab_bunch.feature_names)
columns = ['s3', 's4', 'bmi', 's2', 's1', 's5', 'bp', 's6', 'sex', 'age']
df = df.reindex(columns=columns)

db_ideal = df.copy()

#print(db_ideal)
#ideal_topk = ag.generate_skewness_insights(db_ideal, k)
#print(ideal_topk, len(ideal_topk))

N_samples = 4420

k_list = [3,5,8,10] #5,10,15,20,25,30,35,40,45
a_list = [1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7] #, 

for a in a_list:
  for k in k_list:
    topk = ag.generate_skewness_insights(db_ideal, k)
    for j in range(100):
        data = missing_data(df, N_samples, a, j)
        #print(data)

        missing_topk = ag.generate_skewness_insights(data, k)
        with open('results/v2_missing_vs_ideal_zipf.csv', 'a', newline='') as f:
          #print(missing_topk, len(missing_topk))
          #print(topk, len(topk))
          fields = [a, k, ag.rboresult(missing_topk, topk), ag.jaccard_similarity(missing_topk, topk)]
          print(fields)
          writer = csv.writer(f)
          writer.writerow(fields)

        