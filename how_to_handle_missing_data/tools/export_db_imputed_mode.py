import random
import matplotlib.pyplot as plt
import psycopg2 as pg
import pandas.io.sql as psql
import numpy as np
import pandas as pd
from sqlalchemy import create_engine
import utilities as util

# get connected to the database

connection = pg.connect("dbname=aheart_dataset_random user=postgres password=zenvisage")
engine = create_engine(r'postgresql+psycopg2://postgres:zenvisage@localhost:5432/aheart_dataset_random_mode_impute')



mlist = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3]

print("Mode Imputation export to Postgre")
for i in mlist:
    for j in range(100):
        #print(int(i * 100), j)
        x = int(i * 100)
        table_name = "db_" + str(x) + "rand_missing_attr" + str(j+1)
        db = psql.read_sql("SELECT * FROM " + table_name, connection)
        db.drop(db.columns[[0]], axis=1, inplace=True)
        #print(table_name)
        data = util.mode_impute(db)

        new_table_name = "db_" + str(x) + "rand_missing_attr" + str(j + 1)
        print("Exporting ... ", new_table_name)
        data.to_sql(new_table_name, engine)


for i in mlist:
    for j in range(100):
        #print(int(i * 100), j)
        x = int(i * 100)
        table_name = "db_" + str(x) + "rand_missing_measure" + str(j+1)
        db = psql.read_sql("SELECT * FROM " + table_name, connection)
        db.drop(db.columns[[0]], axis=1, inplace=True)
        #print(table_name)
        data = util.mode_impute(db)

        new_table_name = "db_" + str(x) + "rand_missing_measure" + str(j + 1)
        print("Exporting ... ", new_table_name)
        data.to_sql(new_table_name, engine)



for i in mlist:
    for j in range(100):
        #print(int(i * 100), j)
        x = int(i * 100)
        table_name = "db_" + str(x) + "rand_missing_a_m" + str(j+1)
        db = psql.read_sql("SELECT * FROM " + table_name, connection)
        db.drop(db.columns[[0]], axis=1, inplace=True)
        #print(table_name)
        data = util.mode_impute(db)

        new_table_name = "db_" + str(x) + "rand_missing_a_m" + str(j + 1)
        print("Exporting ... ", new_table_name)
        data.to_sql(new_table_name, engine)

