#%%
#!/usr/bin/env python
# coding: utf-8
import os
# import random
from collections import Counter
from sklearn.model_selection import train_test_split

#%%
dataset_path = '/media/maubrapa/hd1t/datasets/ts_yolo_format_v3'

# %%
# n=os.path.join(path, f)
def getLabelIndex(sample_path):
    labels=['placapare']
    # labels=['noovertaking','turnleft','turnright','60kmh','80kmh','bridge','trucksright','40kmh']
    for l in labels: # percorre a lista labels
        if(sample_path.find(l) != -1):
            # print(labels.index(l))
            return(labels.index(l))

#%%
ext = '.jpg'
X = [] # list of path 
y = [] # and class

# ind = 0
for path, dirs, files in os.walk(dataset_path):
    classNumber = getLabelIndex(path)
    if(classNumber is not None):
        print(classNumber, ': Path', path)
        for f in files:
            if ext in f:
                X.append(os.path.join(path, f))
                y.append(classNumber)

# %% Create file
file_train = open('path_list.txt', 'w')
X = map(lambda x: x+'\n', X)
file_train.writelines(X)
file_train.close()