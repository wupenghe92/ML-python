from matplotlib import pyplot as plt
from sklearn.neighbors import KNeighborsClassifier as KNN
import numpy as np

path1 = "/Users/wupenghe/Desktop/CSE447/project/data/train_label_processed.csv"
path2 = "/Users/wupenghe/Desktop/CSE447/project/data/test_label_processed.csv"
data_train = np.genfromtxt(path1, dtype=float, delimiter=',', skip_header=0) 
data_test = np.genfromtxt(path2, dtype=float, delimiter=',', skip_header=0) 

X_train = data_train[:,0:1]
y_train = data_train[:,2]
X_test =  data_train[:,0:1]

h = KNN(n_neighbors=10)
h.fit(X_train,y_train)
result1 = h.predict_proba(X_test)
result = result1[:,0]
#write result
     

np.savetxt('/Users/wupenghe/Desktop/CSE447/project/lalala.csv',result,fmt='%f',delimiter=',')