import pandas as pd
import numpy as np

### feature extraction ###
df1 = pd.read_csv('/Users/Jia/Documents/nanana/course/CSE 347/project/datasets/test_label.csv', header=0)
test_label = df1.values
df2 = pd.read_csv('/Users/Jia/Documents/nanana/course/CSE 347/project/datasets/user_log.csv', header=0)
user_log = df2.values
df3 = pd.read_csv('/Users/Jia/Documents/nanana/course/CSE 347/project/datasets/user_info.csv', header=0)
user_info = df3.values

num = len(test_label)

userID = np.zeros(num)
merchantID = np.zeros(num)

feature_age = np.zeros(num)      
feature_gender = np.zeros(num)
feature_score_total = np.zeros(num) # calculate the total score for each customer based on different weights of four types of operations
feature_score_mc = np.zeros(num) # calculate the score for each customer based on different weights of four types of operations with specific merchant
feature_ratio_bf11 = np.zeros(num) # ratio of number of buying and total number of operations before 11/11
feature_ratio_on11 = np.zeros(num) # ratio of number of buying and total number of operations on 11/11
feature_ratiodf = np.zeros(num) # difference between previous two
feature_ratio_mc = np.zeros(num) # ratio of number of buying and total number of operations with specific merchant

score_weight = [1,5,10,7]

for i in xrange(num):
    a, b = test_label[i, 0].split("#")
    userID[i] = int(a)
    merchantID[i] = int(b)
    
    # extract age and gender features from user info
    index_info = np.where(user_info[:, 0] == userID[i])
    feature_age[i] = user_info[index_info[0][0], 1]
    feature_gender[i] = user_info[index_info[0][0], 2]
 
    # extract features from user log
    count_buy_on11 = 0 
    count_buy_bf11 = 0   
    count_buy_mc = 0
    count_other_on11 = 0 
    count_other_bf11 = 0 
    count_other_mc = 0
       
    index_log = np.where(user_log[:, 0] == userID[i])
    for j in xrange(len(index_log[0])):
        n = index_log[0][0] + j # row number of log
        action_type = user_log[n, 6]
        action_date = user_log[n, 5]
        feature_score_total[i] = feature_score_total[i] + score_weight[action_type]
        
        if user_log[n, 3] == merchantID[i]:
            feature_score_mc[i] = feature_score_mc[i] + score_weight[action_type]
    
        if action_type == 2:
            if user_log[n, 3] == merchantID[i]:
                count_buy_mc = count_buy_mc + 1
            if action_date == 1111:
                count_buy_on11 = count_buy_on11 + 1 
            else:
                count_buy_bf11 = count_buy_bf11 + 1 
        else:
            if user_log[n, 3] == merchantID[i]:
                count_other_mc = count_other_mc + 1
            if action_date == 1111:
                count_other_on11 = count_other_on11 + 1 
            else:
                count_other_bf11 = count_other_bf11 + 1
                           
    feature_ratio_bf11[i] = float(count_buy_bf11) / (count_other_bf11 + count_buy_bf11 + 1) # get rid of division by 0
    feature_ratio_on11[i] = float(count_buy_on11) / (count_other_on11 + count_buy_on11 + 1)
    feature_ratiodf[i] = (abs)(feature_ratio_on11[i] - feature_ratio_bf11[i])
    feature_ratio_mc[i] = float(count_buy_mc) / (count_other_mc + count_buy_mc + 1)
    
### export to csv ###
X_test = {"age": feature_age, "gender": feature_gender, "score_total": feature_score_total, "score_merchant": feature_score_mc, "ratio_before11": feature_ratio_bf11, "ratio_on11": feature_ratio_on11, "ratio_difference": feature_ratiodf, "ratio_merchant": feature_ratio_mc}
df4 = pd.DataFrame(X_test, columns=["age", "gender", "score_total", "score_merchant","ratio_before11", "ratio_on11", "ratio_difference", "ratio_merchant"])
df4.to_csv("X_test.csv", index=False)