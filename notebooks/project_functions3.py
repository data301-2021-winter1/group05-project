import numpy as np
import pandas as pd

def load_and_process(url_or_path_to_csv_file):
    df = (
    pd.read_csv(url_or_path_to_csv_file)
    .drop(columns=['DGUID','UOM_ID','SCALAR_ID','VECTOR', 'COORDINATE', 'STATUS','SYMBOL','TERMINATED', 'DECIMALS'],axis=1)
    .dropna()
    .rename(columns={"REF_DATE":"Year", "GEO":"Location", "SCALAR_FACTOR":"Scalar Factor", "VALUE":"Value"})
   
)
    return df