import pandas as pd
from typing import List


def concact_data_frames(data_frame_list: List[pd.DataFrame]) -> pd.DataFrame:
    """
    Function to transform lists of dataframes into one dataframe
    """
    return pd.concat(data_frame_list, ignore_index=True)
