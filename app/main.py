from pipeline.extract import extract_from_excel
from pipeline.load import load_excel
from pipeline.transform import concact_data_frames

if __name__ == '__main__':
    data_frame_list = extract_from_excel('data/input')
    data_frame = concact_data_frames(data_frame_list)
    load_excel(data_frame, 'data/output', 'output')
