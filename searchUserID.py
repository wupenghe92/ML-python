from matplotlib import pyplot as plt
from sklearn.neighbors import KNeighborsClassifier as KNN
import numpy as np
import csv

user_ID = 123456


with open('/Users/wupenghe/Desktop/CSE447/project/data/user_log1.csv','r') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        if user_ID == row[0]: 
        print user_ID
        break
        
    