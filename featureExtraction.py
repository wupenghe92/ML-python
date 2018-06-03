import pandas as pd
import numpy as np

df1 = pd.read_csv('/Users/wupenghe/Desktop/CSE447/project/data/train_label_short.csv', header=0)
train_label = df1.values
df2 = pd.read_csv('/Users/wupenghe/Desktop/CSE447/project/data/user_log.csv', header=0)
user_log = df2.values
#df3 = pd.read_csv('/Users/wupenghe/Desktop/CSE447/project/data/user_info.csv', header=0)
#user_info = df3.values

#user_info_id = user_info[:,0]

#extract age and gender features of users
user_ID = np.zeros((len(train_label),1))
merchant_ID = np.zeros((len(train_label),1))

feature_age = np.zeros((len(train_label),1))      
feature_gender = np.zeros((len(train_label),1))
feature_score = np.zeros((len(train_label),1))
feature_ratio_bf11 = np.zeros((len(train_label),1))
feature_ratio_on11 = np.zeros((len(train_label),1))
feature_ratiodf = np.zeros((len(train_label),1))


score_weight = [1,5,10,7]


for i in xrange(len(train_label)):
    a,b = train_label[i,0].split("#")
    user_ID[i] = int(a)
    merchant_ID[i] = int(b) 
    #index_info = np.where(user_info[:,0] == user_ID[i])
    #feature_age[i] = user_info[index_info[0][0],1]
    #feature_gender[i] = user_info[index_info[0][0],2]
    
    # log features
    count_buy_on11 = 0 
    count_buy_bf11 = 0   
    count_other_on11 = 0 
    count_other_bf11 = 0 
       
    index_log = np.where(user_log[:,0] == user_ID[i])
    for j in xrange(len(index_log[0])):
        n = index_log[0][0]+j
        action_type = user_log[n,6]
        action_date = user_log[n,5]
        feature_score[i] = feature_score[i] + score_weight[action_type]
        if action_type == 2:
            if action_date == 1111:
                count_buy_on11 = count_buy_on11 + 1 
            else:
                count_buy_bf11 = count_buy_bf11 + 1 
        else:
            if action_date == 1111:
                count_other_on11 = count_other_on11 + 1 
            else:
                count_other_bf11 = count_other_bf11 + 1
                           
    feature_ratio_bf11[i] = float(count_buy_bf11)/(count_other_bf11+count_buy_bf11)
    feature_ratio_on11[i] = float(count_buy_on11)/(count_other_on11+count_buy_on11)
    feature_ratiodf[i] = feature_ratio_on11[i] - feature_ratio_bf11[i]
    
            
        
    
    #print i,user,merchant
    
    
    
    
    
    
    
    
    
    

#for i in xrange(len(user_info)):
#prob = df['prob'].values
#merchant = df2['merchant_id'].values
##for x in range(0, 130364):
#    #if prob[x] == 1:
#        #a,b = data[x, 0].split("#")
#
#for y in range(0, 26258292):
#    #if data2[y, 0] == int(a) and data2[y, 3] == int(b):
#        if data2[y, 0] == 6125:
#            print data2[y, :]
#            for x in range(0, 130364):
#                a,b = data[x, 0].split("#")
#                if int(b) == 4811 and int(a) == data2[y, 0]:
#                    print prob[x]
#	            
	            
