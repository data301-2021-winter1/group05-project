def load_and_process(url_or_path_to_csv_file):
    mylist = ['Hotels', 'Motels', 'Camping', 'Other accommodation']
    pattern = '|'.join(mylist)
    df = pd.read_csv(url_or_path_to_csv_file)
    df = (  
        df.rename(columns={'REF_DATE': 'Year', 'GEO': 'Province', 'VALUE':'Dollar Value in Millions', 'Products':'Accomodation'})
        .drop(columns=['DGUID', 'SCALAR_ID', 'VECTOR', 'UOM_ID', 'Indicators', 'SCALAR_FACTOR','COORDINATE', 'STATUS', 'SYMBOL', 'TERMINATED', 'DECIMALS'],axis=1)
        .loc[lambda row: df['Products'].str.contains(pattern)==True]
        .loc[lambda row: df['GEO'].str.contains('British Columbia')==True]
        .dropna()
        )
    return df

df= load_and_process('../data/raw/tourism.csv')
print(df)