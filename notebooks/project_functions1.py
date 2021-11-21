import pandas as pd 
import numpy as np

def load_and_process(url_or_path_to_csv_file):
    # Method Chain 1
    df = (
        pd.read_csv(url_or_path_to_csv_file)
        .drop(columns=['DGUID','UOM_ID','SCALAR_ID','VECTOR', 'COORDINATE','STATUS','SYMBOL','TERMINATED', 'DECIMALS'],axis=1)
        .dropna()
        .query("GEO != ['Nunavut', 'Northwest Territories','Yukon','Newfoundland and Labrador','Prince Edward Island','Nova Scotia','New Brunswick','Quebec','Ontario','Manitoba','Saskatchewan', 'Alberta']")
        .query("UOM != ['Percentage']")
        .rename(columns={"REF_DATE":"Year", "GEO":"Location", "SCALAR_FACTOR":"Scalar Factor", "VALUE":"Value"})
        )
    return df