import warnings
from utils.dataloader import dataLoad
from utils.dataloader import timeset
from utils.segmentation import SignalML, SignalV
from utils.dataloader import *

import os
import numpy as np
import pandas as pd
import hrvanalysis
import scipy
from config.parameter import *
import pyhrv
import pyhrv.time_domain as td
import pyhrv.frequency_domain as fd
import pyhrv.nonlinear as nl
from tqdm import tqdm

warnings.filterwarnings('ignore')

print("***********************************")
print("Arrhythmia Data's Feature Extractor")
print("***********************************")

data_all = dataLoad()

ml = data_all[0]
v_ = data_all[1]
peak = data_all[2]
all_label = data_all[4]
dataname = data_all[5]
all_label_seg = all_label[1:len(all_label) - 1]
label_seg = all_label_seg['Type']

types_important = label_seg.reset_index(drop=True)

# ----------------------------------------------------
# for label plotting
label_plot = all_label['Type']
type_plot = label_plot.reset_index(drop=True)
# ----------------------------------------------------

peak_seg = peak[1:len(peak) - 1]
seg_peak = all_label['Sample']

main = SignalML(ml, peak)

signal_ml = main.SegmentPreAfter()

time = timeset(ml)
length = len(signal_ml)


ecg_df_ml = pd.DataFrame(signal_ml)
feat_labels = pd.get_dummies(types_important)
label_setting = feat_labels['N']

for i in range(len(Peak32) // 32):
    data = np.diff(PEAK_STACK[i])
    RR_INTERVAL.append(data)

for i in tqdm(range(len(Peak32) // 32)):
    data = hrvanalysis.extract_features.get_frequency_domain_features(RR_INTERVAL[i])
    FREQUENCY_HRV_FEATURE.append(data)

for i in tqdm(range(len(Peak32) // 32)):
    data = hrvanalysis.extract_features.get_poincare_plot_features(RR_INTERVAL[i])
    print(data)
    POINCARE_HRV_FEATURE.append(data)

for i in tqdm(range(len(Peak32) // 32)):
    data = hrvanalysis.extract_features.get_csi_cvi_features(RR_INTERVAL[i])
    print(data)
    CSICVI_HRV_FEATURE.append(data)

TimeHrvData = pd.DataFrame(TIME_HRV_FEATURE)
FrequencyHrvData = pd.DataFrame(FREQUENCY_HRV_FEATURE)
PoincareHrvData = pd.DataFrame(POINCARE_HRV_FEATURE)
CsicviHrvData = pd.DataFrame(CSICVI_HRV_FEATURE)
LabelData = pd.DataFrame(LABEL_STACK, columns=['Label'])
AllFeature = pd.concat([TimeHrvData, FrequencyHrvData, PoincareHrvData, CsicviHrvData], axis=1)
TotalData = pd.concat([AllFeature, LabelData], axis=1)


