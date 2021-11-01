def load_and_process(url_or_path_to_csv_file):
    data = ('../data/raw/tourism.csv')
    df = (   
        pd.read_csv(url_or_path_to_csv_file)
        .rename(columns={'REF_DATE': 'Year', 'GEO': 'Province', 'UOM': 'Currency'})
        .drop(columns=['DGUID','UOM_ID','SCALAR_ID','VECTOR', 'COORDINATE', 'STATUS','SYMBOL','TERMINATED', 'DECIMALS'],axis=1)
        .drop(rows=['Total tourism expenditures', 'Total tourism products',
           'Total transportation', 'Passenger air transport',
           'Passenger rail transport', 'Passenger water transport',
           'Interurban, charter and tour bus transport', 'Taxis',
           'Vehicle rental', 'Vehicle repairs and parts', 'Vehicle fuel', 'Total food and beverage services',
           'Meals from accommodation', 'Meals from restaurants',
           'Alcoholic beverages from accommodation',
           'Alcoholic beverages from restaurants',
           'Meals and alcoholic beverages from other tourism industries',
           'Total other tourism products', 'Recreation and entertainment',
           'Travel services', 'Convention fees', 'Pre-trip expenses',
           'Total other products', 'Groceries',
           'Beer, wine, and liquor from stores', 'Urban transit and parking',
           'Miscellaneous products'])
        .dropna()
        .query("GEO != ['Nunavut', 'Northwest Territories','Yukon','Newfoundland and Labrador','Prince Edward Island','Nova Scotia','New Brunswick','Quebec','Ontario','Manitoba','Saskatchewan', 'Alberta']")
        
    )


    return df
print (df)