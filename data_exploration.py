#Imports
import pandas as pd;

#Dataframe
df1 = pd.read_csv("data/location_meta.csv");

#Explore data

def explore_data(dataset):
    columns = dataset.columns;
    columns_total = len(dataset.columns);
    cells = dataset.size;
    rows = dataset.size/len(dataset.columns);
    datatypes = dataset.dtypes;
    missingvalues = dataset.isna().sum();
    return  (print("Columns ", columns), print("Columns total ", columns_total), print("Cells ", cells), print("Rows ", rows), print("Datatypes ", datatypes), print("Missigvalues ", missingvalues))

explore_data(df1);




