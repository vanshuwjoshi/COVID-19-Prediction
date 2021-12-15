import glob

import numpy as np
import pandas as pd
import shutil
import os
train_labels = pd.read_csv(r"C:\Users\vansh\OneDrive\Desktop\Data Challenge 2\stat441fall2021dc2\train_labels.csv")

# To create an updated training dataset in order to seperate the images of two classes.

label_1 = train_labels[train_labels['Label']==1]
print(len(label_1))
label_0 = train_labels[train_labels['Label']==0]
print(len(label_0))

# copy the images with label 0 to another folder
for i,row in label_0.iterrows():
    name = row.File
    org = r"C:\Users\vansh\OneDrive\Desktop\Data Challenge 2\stat441fall2021dc2\train\train\train"
    new = r"C:\Users\vansh\OneDrive\Desktop\Data Challenge 2\updated_train\0"
    for file in glob.iglob(os.path.join(org, name)):
        shutil.copy(file, new)

# copy the images with label 1 to another folder
for i,row in label_1.iterrows():
    name = row.File
    org = r"C:\Users\vansh\OneDrive\Desktop\Data Challenge 2\stat441fall2021dc2\train\train\train"
    new = r"C:\Users\vansh\OneDrive\Desktop\Data Challenge 2\updated_train\1"
    for file in glob.iglob(os.path.join(org, name)):
        shutil.copy(file, new)
