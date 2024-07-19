import pandas as pd

def upload_data(request):
    region_1_file = request.FILES['region_1']
    region_2_file = request.FILES['region_2']
    region_3_file = request.FILES['region_3']

    df_region_1 = pd.read_csv(region_1_file)
    df_region_2 = pd.read_csv(region_2_file)
    df_region_3 = pd.read_csv(region_3_file)

    return df_region_1, df_region_2, df_region_3