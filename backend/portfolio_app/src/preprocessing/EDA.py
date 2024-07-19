import pandas as pd

def descriptive_stats(df):
    head = df.head()
    info = df.info()
    describe = df.describe()
    n_duplicates = df.duplicated.sum()
    corr = df.corr()
    return head, info, describe, n_duplicates, corr