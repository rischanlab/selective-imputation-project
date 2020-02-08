import csv
import rbo_func as rbo
import pandas as pd
import numpy as np

def rboresult(groundtruth, new, p=0.95):
    return rbo.rbo(groundtruth, new, p)['ext']


def jaccard_similarity(list1, list2):
    s1 = set(list1)
    s2 = set(list2)
    return len(s1.intersection(s2)) / len(s1.union(s2))

def convert_to_one(item):
    S = []
    for i in item:
        S.append(((''.join(i))))
    return S

def get_topk(k, file):
    df = pd.read_csv(file, index_col=0)
    df = df.head(k).values.tolist()
    x = convert_to_one(df)
    return x


def get_unique(k, file):
    df = pd.read_csv(file, index_col=0)
    df = df.head(k)
    uniq1 = df.level_0.unique().tolist()
    uniq2 = df.level_1.unique().tolist()
    uniq = set(uniq1 + uniq2)
    return list(uniq)

def generate_skewness_insights(data):
    topk = data.skew(axis=0).sort_values(ascending=False)
    topk = topk.to_frame().reset_index()
    topk = topk.rename(columns={'index': 'atr', '0': 'skew'})
    # top5 = top5.values.tolist()
    topk = topk[['atr']]
    topk_ = topk.values.tolist()
    S = []
    for i in topk_:
        S.append(((''.join(i))))
    S
    return S

def generate_skewness_insights_abs(data):
    topk = data.skew(axis=0)
    topk = topk.to_frame().reset_index()
    topk = topk.rename(columns={'index': 'atr', 0: 'skew'})
    # top5 = top5.values.tolist()
    topk['skew'] = abs(topk['skew'])
    topk = topk.sort_values(by=['skew'], ascending=False)
    topk = topk[['atr']]
    topk_ = topk.values.tolist()
    S = []
    for i in topk_:
        S.append(((''.join(i))))
    S
    return S

def generate_kurtosis_insights(data):
    topk = data.kurt(axis=0).sort_values(ascending=False)
    topk = topk.to_frame().reset_index()
    topk = topk.rename(columns={'index': 'atr', 0: 'kurt'})
    # top5 = top5.values.tolist()
    topk = topk[['atr']]
    topk_ = topk.values.tolist()
    S = []
    for i in topk_:
        S.append(((''.join(i))))
    S
    return S

def generate_kurtosis_insights_abs(data):
    topk = data.kurt(axis=0)
    topk = topk.to_frame().reset_index()
    topk = topk.rename(columns={'index': 'atr', 0: 'kurt'})
    topk['kurt'] = abs(topk['kurt'])
    topk = topk.sort_values(by=['kurt'], ascending=False)
    # top5 = top5.values.tolist()
    topk = topk[['atr']]
    topk_ = topk.values.tolist()
    S = []
    for i in topk_:
        S.append(((''.join(i))))
    S
    return S

def generate_correlation_insights(data):
    dataCorr = data.corr(method='pearson')
    dataCorr = dataCorr[abs(dataCorr) >= 0].stack().reset_index()
    dataCorr = dataCorr[dataCorr['level_0'].astype(str) != dataCorr['level_1'].astype(str)]

    # filtering out lower/upper triangular duplicates
    dataCorr['ordered-cols'] = dataCorr.apply(lambda x: '-'.join(sorted([x['level_0'], x['level_1']])), axis=1)
    dataCorr = dataCorr.drop_duplicates(['ordered-cols'])
    dataCorr.drop(['ordered-cols'], axis=1, inplace=True)

    topk = dataCorr.sort_values(by=[0], ascending=False)
    topk = topk[['level_0', 'level_1']]
    # S = [item for sublist in topk_nomissing for item in sublist]
    topk = topk.reset_index()
    topk.drop(topk.columns[[0]], axis=1, inplace=True)
    topk_ = topk[['level_0', 'level_1']]
    topk_ = topk_.values.tolist()
    S = []
    for i in topk_:
        S.append(((''.join(i))))
    S
    return S

def generate_correlation_insights_abs(data):
    dataCorr = data.corr(method='pearson')
    dataCorr = dataCorr[abs(dataCorr) >= 0].stack().reset_index()
    dataCorr = dataCorr[dataCorr['level_0'].astype(str) != dataCorr['level_1'].astype(str)]

    # filtering out lower/upper triangular duplicates
    dataCorr['ordered-cols'] = dataCorr.apply(lambda x: '-'.join(sorted([x['level_0'], x['level_1']])), axis=1)
    dataCorr = dataCorr.drop_duplicates(['ordered-cols'])
    dataCorr.drop(['ordered-cols'], axis=1, inplace=True)
    columns = ['level_0','level_1','score']
    dataCorr.columns = columns
    dataCorr['score'] = abs(dataCorr['score'])
    topk = dataCorr.sort_values(by=['score'], ascending=False)

    topk = topk[['level_0', 'level_1']]
    # S = [item for sublist in topk_nomissing for item in sublist]
    topk = topk.reset_index()
    topk.drop(topk.columns[[0]], axis=1, inplace=True)
    topk_ = topk[['level_0', 'level_1']]
    topk_ = topk_.values.tolist()
    S = []
    for i in topk_:
        S.append(((''.join(i))))
    S
    return S


### Correlation Cum Functions 

def correlation_ideal(data):
    dataCorr = data.corr(method='pearson')
    dataCorr = dataCorr[abs(dataCorr) >= 0].stack().reset_index()
    dataCorr = dataCorr[dataCorr['level_0'].astype(str) != dataCorr['level_1'].astype(str)]

    # filtering out lower/upper triangular duplicates
    dataCorr['ordered-cols'] = dataCorr.apply(lambda x: '-'.join(sorted([x['level_0'], x['level_1']])), axis=1)
    dataCorr = dataCorr.drop_duplicates(['ordered-cols'])
    dataCorr.drop(['ordered-cols'], axis=1, inplace=True)

    topk = dataCorr.sort_values(by=[0], ascending=False)
    columns = ['a','b','score']
    topk.columns = columns
    topk['combined_col'] = topk[['a', 'b']].astype(str).apply(''.join, axis=1)
    topk['score'] = topk['score'] + 1
    topk = topk.reset_index()
    topk['id'] = topk.index + 1
    topk = topk[['id','combined_col','score']]
    return topk

def get_sum_correlation_ideal(k, df):
    df = df.head(k)
    df['real_score'] = 1/np.log(df['id'] + 1) * df['score']
    return df['real_score'].sum()

def get_sum_correlation_insights_cum(k, df_ideal, df):
    data = df
    dataCorr = data.corr(method='pearson')
    dataCorr = dataCorr[abs(dataCorr) >= 0].stack().reset_index()
    dataCorr = dataCorr[dataCorr['level_0'].astype(str) != dataCorr['level_1'].astype(str)]

    # filtering out lower/upper triangular duplicates
    dataCorr['ordered-cols'] = dataCorr.apply(lambda x: '-'.join(sorted([x['level_0'], x['level_1']])), axis=1)
    dataCorr = dataCorr.drop_duplicates(['ordered-cols'])
    dataCorr.drop(['ordered-cols'], axis=1, inplace=True)

    topk = dataCorr.sort_values(by=[0], ascending=False)
    columns = ['a','b','score']
    topk.columns = columns
    topk = topk.head(k)
    topk['combined_col'] = topk[['a', 'b']].astype(str).apply(''.join, axis=1)
    topk.drop(topk.columns[[0,1,2]], axis=1, inplace=True)
    topk = topk.merge(df_ideal,on='combined_col')
    topk = topk.reset_index()
    topk['id'] = topk.index + 1
    topk = topk[['id','combined_col','score']]
    topk['real_score'] = 1/np.log(topk['id'] + 1) * topk['score']
    return topk['real_score'].sum()

## Skewness Cum Functions

def skew_ideal(data):
    topk = data.skew(axis=0).sort_values(ascending=False)
    topk = topk.to_frame().reset_index()
    topk = topk.rename(columns={'index': 'atr', 0: 'skew'})
    topk['skew'] = topk['skew'] + abs(topk['skew'].min())
    topk = topk.reset_index()
    topk['id'] = topk.index + 1
    topk = topk[['id','atr','skew']]
    return topk

def get_sum_skew_ideal(k, df):
    df = df.head(k)
    df['real_score'] = 1/np.log(df['id'] + 1) * df['skew']
    return df['real_score'].sum()

def get_sum_skew_insights_cum(k, df_ideal, df):
    data = df
    topk = data.skew(axis=0).sort_values(ascending=False)
    topk = topk.to_frame().reset_index()
    topk = topk.rename(columns={'index': 'atr', 0: 'skew'})
    topk = topk[['atr']]

    topk = topk.head(k)
    topk = topk.merge(df_ideal,on='atr')
    topk = topk.reset_index()
    topk['id'] = topk.index + 1
    topk = topk[['id','atr','skew']]
    topk['real_score'] = 1/np.log(topk['id'] + 1) * topk['skew']
    return topk['real_score'].sum()


## Kurotsis Cum Functions

def kurt_ideal(data):
    topk = data.kurt(axis=0).sort_values(ascending=False)
    topk = topk.to_frame().reset_index()
    topk = topk.rename(columns={'index': 'atr', 0: 'kurt'})
    topk['kurt'] = topk['kurt'] + abs(topk['kurt'].min())
    topk = topk.reset_index()
    topk['id'] = topk.index + 1
    topk = topk[['id','atr','kurt']]
    return topk

def get_sum_kurt_ideal(k, df):
    df = df.head(k)
    df['real_score'] = 1/np.log(df['id'] + 1) * df['kurt']
    return df['real_score'].sum()

def get_sum_kurt_insights_cum(k, df_ideal, df):
    data = df
    topk = data.kurt(axis=0).sort_values(ascending=False)
    topk = topk.to_frame().reset_index()
    topk = topk.rename(columns={'index': 'atr', 0: 'kurt'})
    topk = topk[['atr']]

    topk = topk.head(k)
    topk = topk.merge(df_ideal,on='atr')
    topk = topk.reset_index()
    topk['id'] = topk.index + 1
    topk = topk[['id','atr','kurt']]
    topk['real_score'] = 1/np.log(topk['id'] + 1) * topk['kurt']
    return topk['real_score'].sum()


### Correlation Cum Functions ABS



def correlation_ideal_abs(data):
    dataCorr = data.corr(method='pearson')
    dataCorr = dataCorr[abs(dataCorr) >= 0].stack().reset_index()
    dataCorr = dataCorr[dataCorr['level_0'].astype(str) != dataCorr['level_1'].astype(str)]

    # filtering out lower/upper triangular duplicates
    dataCorr['ordered-cols'] = dataCorr.apply(lambda x: '-'.join(sorted([x['level_0'], x['level_1']])), axis=1)
    dataCorr = dataCorr.drop_duplicates(['ordered-cols'])
    dataCorr.drop(['ordered-cols'], axis=1, inplace=True)

    topk = dataCorr
    columns = ['a','b','score']
    topk.columns = columns
    topk['combined_col'] = topk[['a', 'b']].astype(str).apply(''.join, axis=1)
    topk['score'] = abs(topk['score'])
    topk = topk.sort_values(by=['score'], ascending=False)
    topk = topk.reset_index()
    topk['id'] = topk.index + 1
    topk = topk[['id','combined_col','score']]
    return topk

def get_sum_correlation_ideal_abs(k, df):
    df = df.head(k)
    df['real_score'] = 1/np.log(df['id'] + 1) * df['score']
    return (df,df['real_score'].sum())

def get_sum_correlation_insights_cum_abs(k, df_ideal, df):
    data = df
    dataCorr = data.corr(method='pearson')
    dataCorr = dataCorr[abs(dataCorr) >= 0].stack().reset_index()
    dataCorr = dataCorr[dataCorr['level_0'].astype(str) != dataCorr['level_1'].astype(str)]

    # filtering out lower/upper triangular duplicates
    dataCorr['ordered-cols'] = dataCorr.apply(lambda x: '-'.join(sorted([x['level_0'], x['level_1']])), axis=1)
    dataCorr = dataCorr.drop_duplicates(['ordered-cols'])
    dataCorr.drop(['ordered-cols'], axis=1, inplace=True)

    topk = dataCorr
    columns = ['a','b','score']
    topk.columns = columns
    topk['score'] = abs(topk['score'])
    topk = topk.sort_values(by=['score'], ascending=False)
    topk = topk.head(k)
    topk['combined_col'] = topk[['a', 'b']].astype(str).apply(''.join, axis=1)
    topk.drop(topk.columns[[0,1,2]], axis=1, inplace=True)
    topk = topk.merge(df_ideal,on='combined_col')
    topk = topk.reset_index()
    topk['id'] = topk.index + 1
    topk = topk[['id','combined_col','score']]
    topk['real_score'] = 1/np.log(topk['id'] + 1) * topk['score']
    return (topk, topk['real_score'].sum())

## Skewness Cum Functions ABS

def skew_ideal_abs(data):
    topk = data.skew(axis=0)
    topk = topk.to_frame().reset_index()
    topk = topk.rename(columns={'index': 'atr', 0: 'skew'})
    topk['skew'] = abs(topk['skew'])
    topk = topk.sort_values(by=['skew'], ascending=False)
    topk = topk.reset_index()
    topk['id'] = topk.index + 1
    topk = topk[['id','atr','skew']]
    return topk

def get_sum_skew_ideal_abs(k, df):
    df = df.head(k)
    df['real_score'] = 1/np.log(df['id'] + 1) * df['skew']
    return (df,df['real_score'].sum())

def get_sum_skew_insights_cum_abs(k, df_ideal, df):
    data = df
    topk = data.skew(axis=0)
    topk = topk.to_frame().reset_index()
    topk = topk.rename(columns={'index': 'atr', 0: 'skew'})
    topk['skew'] = abs(topk['skew'])
    topk = topk.sort_values(by=['skew'], ascending=False)

    topk = topk[['atr']]

    topk = topk.head(k)
    topk = topk.merge(df_ideal,on='atr')
    topk = topk.reset_index()
    topk['id'] = topk.index + 1
    topk = topk[['id','atr','skew']]
    topk['real_score'] = 1/np.log(topk['id'] + 1) * topk['skew']
    return (topk, topk['real_score'].sum())


## Kurotsis Cum Functions ABS

def kurt_ideal_abs(data):
    topk = data.kurt(axis=0)
    topk = topk.to_frame().reset_index()
    topk = topk.rename(columns={'index': 'atr', 0: 'kurt'})
    topk['kurt'] = abs(topk['kurt'])
    topk = topk.sort_values(by=['kurt'], ascending=False)
    topk = topk.reset_index()
    topk['id'] = topk.index + 1
    topk = topk[['id','atr','kurt']]
    return topk

def get_sum_kurt_ideal_abs(k, df):
    df = df.head(k)
    df['real_score'] = 1/np.log(df['id'] + 1) * df['kurt']
    return df['real_score'].sum()

def get_sum_kurt_insights_cum_abs(k, df_ideal, df):
    data = df
    topk = data.kurt(axis=0).sort_values(ascending=False)
    topk = topk.to_frame().reset_index()
    topk = topk.rename(columns={'index': 'atr', 0: 'kurt'})
    topk['kurt'] = abs(topk['kurt'])
    topk = topk.sort_values(by=['kurt'], ascending=False)
    topk = topk[['atr']]

    topk = topk.head(k)
    topk = topk.merge(df_ideal,on='atr')
    topk = topk.reset_index()
    topk['id'] = topk.index + 1
    topk = topk[['id','atr','kurt']]
    topk['real_score'] = 1/np.log(topk['id'] + 1) * topk['kurt']
    return topk['real_score'].sum()