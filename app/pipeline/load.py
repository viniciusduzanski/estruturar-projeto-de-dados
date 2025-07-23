import logging
import os

import pandas as pd


def load_excel(
    data_frame: pd.DataFrame, output_path: str, file_name: str
) -> str:
    """
    Receive a dataframe and save it as an Excel file.

    Args:
    data_frame (pd.DataFrame): dataframe to be saved as an Excel file
    output_path (str): path where the file will be saved
    file_name(path): name of the file to be saved

    Return: "File saved successfully"
    """

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    try:
        path = f'{output_path}/{file_name}.xlsx'
        data_frame.to_excel(path, index=False)
        return 'File saved successfully'
    except Exception as e:
        logging.error(f'Failed to save Excel file: {e}')
        raise
