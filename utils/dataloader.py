# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 16:27:59 2019
@author: SWH
"""

import pandas as pd
import numpy as np
import scipy.io as io

import torch

def dataLoad():
    data_name = input("Input file name:")
    data = io.loadmat("/"+data_name+".mat", squeeze_me=True)
    return mldata, v5data, peak, stype, csv_peak_label, data_name

def timeset(data):
    time = []
    for t in range(0, len(data), 1):
        time.append(t)
    return np.array(time)