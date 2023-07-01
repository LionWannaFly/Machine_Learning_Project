import os
import random
import shutil

num_img=500
i=0

labels = ['bellflower','daisy','dandelion','tulip','sunflower','rose','lotus','iris']
path = "D:/school/ML/Machine_Learning_Project/Data/flowers"
train="D:/school/ML/Machine_Learning_Project/Data/train"
test="D:/school/ML/Machine_Learning_Project/Data/test"
for f in range(8):
    i=0
    folder_path = os.path.join(path, labels[f])
    train_path=os.path.join(train, labels[f])
    test_path=os.path.join(test, labels[f])
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if i<num_img:
            shutil.move(os.path.join(folder_path, file), os.path.join(test_path, file))
        else:
            shutil.move(os.path.join(folder_path, file), os.path.join(train_path, file))
        i+=1