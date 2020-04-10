import os
import numpy as np
import pandas as pd


DATA_DIR = "../saved/data/hrv_feature/DS1/"
file_list = os.listdir(DATA_DIR)

all_feature_list = []

for idx, data in enumerate(file_list):
    all_feature_list.append(pd.read_csv(DATA_DIR+data).dropna().values)
    
all_feature = pd.DataFrame(np.concatenate(all_feature_list))

all_feature.to_csv('train.csv', index=False)