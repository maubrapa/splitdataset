#%%
#!/usr/bin/env python
# coding: utf-8
import os
# import random
from collections import Counter
from sklearn.model_selection import train_test_split

#%%
dataset_path = '/home/maubrapa/datasets/ts_yolo_format_v3'
# dataset_path = './data/'

# %%
# n=os.path.join(path, f)
def getLabelIndex(sample_path):
    #labels=['noovertaking','turnleft','turnright','60kmh','80kmh','bridge','trucksright','40kmh','placapare']
    labels=['noovertaking','turnleft','placapare']
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

# %% Stratified Train-Test Splits
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.50, random_state=1, stratify=y)

print(Counter(y),'\n')
print(Counter(y_train))
print(Counter(y_test))
# %% Create train and test files
# https://www.theunixschool.com/2013/08/python-how-to-write-list-to-file.html?m=1
file_train = open('ts2_train.txt', 'w')
X_train = map(lambda x: x+'\n', X_train)
file_train.writelines(X_train)
file_train.close()

file_test = open('ts2_test.txt', 'w')
X_test = map(lambda x: x+'\n', X_test)
file_test.writelines(X_test)
file_test.close()
