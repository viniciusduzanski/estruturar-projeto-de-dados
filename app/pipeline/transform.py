import pandas as pd
from typing import List

"""
Function to transform lists of dataframes into one dataframe
"""

def concact_data_frames(data_frame_list: List[pd.DataFrame]) -> pd.DataFrame:
    return pd.concat(data_frame_list, ignore_index=True)
    