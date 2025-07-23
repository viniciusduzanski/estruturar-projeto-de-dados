import glob  # Library for listing files
import os  # Library for manipulating files and folders
from typing import List

import pandas as pd
from pandas.io.formats.info import _DataFrameTableBuilderVerbose

path = 'data/input'


def extract_from_excel(path: str) -> List[pd.DataFrame]:
    """
    Function to read files from a data/input folder and
    return a list of dataframes

    Args:
        path (str): path to the folder with files

    Returns:
        List[pd.DataFrame]: list of dataframes

    Raises:
        FileNotFoundError: if directory doesn't exist or no Excel files found
    """
    all_files = glob.glob(os.path.join(path, '*.xlsx'))

    if not os.path.exists(path):
        raise FileNotFoundError(f'Directory {path} not found')

    if not all_files:
        raise FileNotFoundError(f'No Excel files found in {path}')

    data_frame_list: List[pd.DataFrame] = []

    for file in all_files:
        data_frame_list.append(pd.read_excel(file))

    return data_frame_list


if __name__ == '__main__':
    data_frame_list = extract_from_excel(path)
    print(data_frame_list)
