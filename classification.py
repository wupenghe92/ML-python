from sklearn.tree import DecisionTreeClassifier as dtcl
from sklearn.neighbors import KNeighborsClassifier as KNN
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from matplotlib import pyplot as plt
from sklearn.metrics import roc_curve

def ss_measure(y_ground_truth, y_test):
    TP = 0
    FP = 0
    TN = 0
    FN = 0
    for i in range(len(y_test)): 
        if y_ground_truth[i]==y_test[i]==1:
            TP += 1 
        if y_test[i]==1 and y_ground_truth[i]==0:
            FP += 1
        if y_ground_truth[i]==y_test[i]==0:
            TN += 1
        if y_test[i]==0 and y_ground_truth[i]==1:
            FN += 1           
    return(TP,FP,TN,FN)

df1 = pd.read_csv('/Users/wupenghe/Desktop/CSE447/project/data/X_train.csv', header=0) # csv generated by featureExtraction_train.py
X_train = df1.values
df2 = pd.read_csv('/Users/wupenghe/Desktop/CSE447/project/data/y_train.csv', header=0) # csv generated by featureExtraction_train.py
y_train = df2.values
df3 = pd.read_csv('/Users/wupenghe/Desktop/CSE447/project/data/X_test.csv', header=0) # csv generated by featureExtraction_test.py
X_test = df3.values
df4 = pd.read_csv('/Users/wupenghe/Desktop/CSE447/project/data/test_label.csv', header=0)
test_label = df4.values
df6 = pd.read_csv('/Users/wupenghe/Desktop/CSE447/project/data/train_label.csv', header=0)
train_label = df6.values
df7 = pd.read_csv('/Users/wupenghe/Desktop/CSE447/project/data/ground_truth.csv', header=0)
y_ground_truth = df7['prob'].values


### apply classifiers ###

# Decision Tree
dtc = dtcl(criterion='entropy',max_depth=10,min_samples_split=i)
dtc.fit(X_train, y_train)
accuracy_dtc_train = dtc.score(X_train, y_train) # get the accuracy for training data
accuracy_dtc_test = dtc.score(X_test, y_ground_truth) # get the accuracy for testing data
prob_dtc = dtc.predict_proba(X_test)    
#y_test_dtc = dtc.predict(X_test)




            

# KNN
# class label acsending ordering
for j in xrange(8):
    delta = np.std(X_train[:,j])
    miu = np.mean(X_train[:,j])
    X_train[:,j] = (X_train[:,j]-miu)/delta
    X_test[:,j] = (X_test[:,j]-miu)/delta


knn = KNN(n_neighbors=190)
knn.fit(X_train, y_train)
accuracy_knn_train = knn.score(X_train, y_train) # get the accuracy for training data
accuracy_knn_test = knn.score(X_test, y_ground_truth) # get the accuracy for testing data
prob_knn = knn.predict_proba(X_test)


#
#### export results ###
##column1 = df4['user_id#merchant_id'].values
#column2_dtc = prob_dtc[:, 1]
#column2_knn = prob_knn[:, 1]
#factor = 2
#column2 = (np.add(column2_knn, column2_dtc)) / factor

#y_test = {"user_id#merchant_id": df4["user_id#merchant_id"].values, "prob": column2}
#df5 = pd.DataFrame(y_test, columns=["user_id#merchant_id", "prob"])
#df5.to_csv("/Users/wupenghe/Desktop/CSE447/project/data/y_test_1.csv", index=False)
#


#####
#column2 = column2*1;
#for i in xrange(len(column2)):
#    if column2[i] >= 0.5:
#        column2[i] = 1
#    else:
#        column2[i] = 0
#        
##acc = accuracy_score(y_ground_truth, column2)    
##print acc         
#
#TP,FP,TN,FN = ss_measure(y_ground_truth, column2)
#sensitivity_dtc = float(TP)/(TP+FN)
#specificity_dtc = float(TN)/(TN+FP)
#precision_dtc = float(TP)/(TP+FP)


##plot ROC curve
#fpr = dict()
#tpr = dict()
#fpr, tpr, _ = roc_curve(y_ground_truth, column2)
#lw=2
#plt.plot(fpr,tpr)
#plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
#plt.xlim([0.0, 1.0])
#plt.ylim([0.0, 1.0])
#plt.title("ROC curve")
#plt.xlabel("FPR")
#plt.ylabel("TPR")
#plt.show()

