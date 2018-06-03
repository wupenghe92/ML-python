
# -*- coding: utf-8 -*-
import sys
import numpy as np
import re
import pandas

#read test data

user=np.empty(0,dtype=int)
merchant=np.empty(0,dtype=int)
label=np.empty(0,dtype=int)
with open('/Users/wupenghe/Desktop/CSE447/project/data/train_label copy.csv','r') as fp:
    flag=True    
    for line in fp:
        if flag:
            flag=False
            continue
        data=re.split('\W',line)
        user=np.append(user,int(data[0]))
        merchant=np.append(merchant,int(data[1]))
        label = np.append(label,int(data[2]))

#X_train = np.concatenate(user,merchant,axis=1)
y_train = label
#X_test = data_test[:,0:11]
#y_test = data_test[:,11]
