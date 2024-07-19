import pandas as pd

def cleaning(file):
    region = pd.read_csv(file)
    return region.head()