import random
import numpy as np
import pandas as pd
import pandas.io.sql as psql
import psycopg2 as pg
from sqlalchemy import create_engine



def dropout(a, size, percent, seed):
    # create a copy
    mat = a.copy()
    # number of values to replace
    prop = int(size * percent)
    # indices to mask
    random.seed(seed)
    mask = random.sample(range(mat.size), prop)
    # replace with NaN
    #print(size)
    #print(prop)
    print(mask)
    np.put(mat, mask, [np.nan]*len(mask))
    return mat


def missing_data_attr(db, size, percent, seed):

    cp = df['cp'].values
    cp = dropout(cp, size, percent, seed)

    thal = df['thal'].values
    thal = dropout(thal, size, percent, seed)

    exang = df['exang'].values
    exang = dropout(exang, size, percent, seed)
    
    # restecg = df['restecg'].values
    # restecg = dropout(restecg, size, percent, seed)

    sex = df['sex'].values
    sex = dropout(sex, size, percent, seed)

    fbs = df['fbs'].values
    fbs = dropout(fbs, size, percent, seed)


    #num = df['num'].values
    #readmitted = dropout(readmitted, percent*rank[7], seed)

    #['cp', 'thal', 'slope', 'exang', 'restecg', 'sex', 'fbs']

    frame = { 'cp': cp, 'thal': thal, 
             'exang': exang, 
             'sex': sex, 'fbs': fbs
            #'num': num       
            } 

    missing_attr = pd.DataFrame(frame)

    return missing_attr

def missing_data_measure(db, size, percent, seed):

    age = df['age'].values
    age = dropout(age, size, percent, seed)

    restbp = df['restbp'].values
    restbp = dropout(restbp, size, percent, seed)

    chol = df['chol'].values
    chol = dropout(chol, size, percent, seed)

    thalach = df['thalach'].values
    thalach = dropout(thalach, size, percent, seed)

    ca = df['ca'].values
    ca = dropout(ca, size, percent, seed)

    oldpeak = df['oldpeak'].values
    oldpeak = dropout(oldpeak, size, percent, seed)


    frame = { 'age': age, 'restbp': restbp, 
            'chol': chol, 'thalach': thalach,
             'ca': ca
            } 

    missing_measure = pd.DataFrame(frame)
    return missing_measure


#a_columns = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'thal']
#m_columns = ['age', 'restbp', 'chol', 'thalach', 'ca', 'oldpeak']

table_name = 'heart'
connection = pg.connect("dbname=aheart_dataset_random_same_column_same_count_missing user=postgres password=zenvisage")
db = psql.read_sql("SELECT * FROM " + table_name, connection)
db.drop(db.columns[[0]], axis=1, inplace=True)




mlist = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
size = 299
engine = create_engine(r'postgresql+psycopg2://postgres:zenvisage@localhost:5432/aheart_dataset_random_same_column_same_count_missing')

print("Data missing export to Postgre")
for i in mlist:
    for j in range(100):
        #print(int(i * 100), j)
        x = int(i * 100)
        #print(df)
        #print(df.columns.to_series().groupby(df.dtypes).groups)
        # db missing is db with row contains missing drop 
        # db NaN is db with row contain missing keep 
        table_name1 = "db_" + str(x) + "rand_missing_attr" + str(j+1)
        table_name2 = "db_" + str(x) + "rand_missing_measure" + str(j + 1)

        #table_namea = "db_" + str(x) + "dropnan_attr" + str(j+1)
        #table_nameb = "db_" + str(x) + "dropnan_measure" + str(j + 1)
        #table_namec = "db_" + str(x) + "dropnan_a_m" + str(j + 1)

        df = db.copy()
        df_a_m = db.copy()
        df_attr = df.select_dtypes(['object'])
        df_measure = df.select_dtypes(['int64']).astype(float)

        df_attr = df_attr.drop('num', 1)
        df_attr_missing = missing_data_attr(df_attr, size, i, j)
        df_attr_missing['num'] = df['num'].values
        new_df_attr = pd.concat([df_attr_missing, df_measure], axis=1, ignore_index=False, sort=False)

        df_measure_missing = missing_data_measure(df_measure, size, i, j)
        new_df_measure = pd.concat([df.select_dtypes(['object']), df_measure_missing], axis=1, ignore_index=False, sort=False)

        


        # print("Exporting...", table_name1)
        # new_df_attr.to_sql(table_name1, engine)
        # #new_df_attr.dropna(inplace=True)
        # #new_df_attr.to_sql(table_namea, engine)


        # print("Exporting...", table_name2)
        
        # new_df_measure.to_sql(table_name2, engine)
        # # new_df_measure.dropna(inplace=True)
        # # new_df_measure.to_sql(table_nameb, engine)


