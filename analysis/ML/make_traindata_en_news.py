import re
import math
import numpy as np
import pandas as pd
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score ,precision_score , recall_score , confusion_matrix , f1_score
from sklearn.model_selection import GridSearchCV
from ast import literal_eval
from gensim.models.keyedvectors import KeyedVectors
from sklearn.decomposition import PCA
pca = PCA(n_components=40)


###################### 2017 up1
"""
eucl_data = pd.read_csv('../cluster/en_news/2017_up1/en_news_2017_up1_euclidean.csv', error_bad_lines=False)
eucl_data['closer#'] = 2 # cosine 1 , euclidean 2

cosine_data = pd.read_csv('../cluster/en_news/2017_up1/en_news_2017_up1_cosine.csv', error_bad_lines=False)
cosine_data['closer#'] = 1 # cosine 1 , euclidean 2

data_2017U1 = eucl_data
data_2017U1.append(cosine_data)

data_2017U1['period'] = '201711' # 2020년의 up 1 , 첫번째 1

print(data_2017U1)
"""

###################### 2017 up2
"""
eucl_data = pd.read_csv('../cluster/en_news/2017_up2/en_news_2017_up2_euclidean.csv', error_bad_lines=False)
eucl_data['closer#'] = 2 # cosine 1 , euclidean 2

cosine_data = pd.read_csv('../cluster/en_news/2017_up2/en_news_2017_up2_cosine.csv', error_bad_lines=False)
cosine_data['closer#'] = 1 # cosine 1 , euclidean 2

data_2020D1 = eucl_data
data_2020D1.append(cosine_data)

data_2020D1['period'] = '202021' # 2020년의 down 2 , 첫번째 1

print(data_2020D1)
"""


###################### 2020 up1
eucl_data = pd.read_csv('../cluster/en_news/2020_up1/en_news_2020_up1_euclidean.csv', error_bad_lines=False)
eucl_data['closer#'] = 2 # cosine 1 , euclidean 2

cosine_data = pd.read_csv('../cluster/en_news/2020_up1/en_news_2020_up1_cosine.csv', error_bad_lines=False)
cosine_data['closer#'] = 1 # cosine 1 , euclidean 2

data_2020U1 = eucl_data
data_2020U1.append(cosine_data)

data_2020U1['period'] = '202011' # 2020년의 up 1 , 첫번째 1

print(data_2020U1)

###################### 2020 down1
eucl_data = pd.read_csv('../cluster/en_news/2020_down1/en_news_2020_down1_euclidean.csv', error_bad_lines=False)
eucl_data['closer#'] = 2 # cosine 1 , euclidean 2

cosine_data = pd.read_csv('../cluster/en_news/2020_down1/en_news_2020_down1_cosine.csv', error_bad_lines=False)
cosine_data['closer#'] = 1 # cosine 1 , euclidean 2

data_2020D1 = eucl_data
data_2020D1.append(cosine_data)

data_2020D1['period'] = '202021' # 2020년의 down 2 , 첫번째 1

print(data_2020D1)

###################### data concat

data_train = pd.concat([data_2020U1,data_2020D1],ignore_index=True)


###################### ML

x_data_df = data_train[['period','raw_data','closer#','category','label','Silhouette']]
y_data_df = data_train['result']

# random frest

# xg boost

# Logistic regression
# dnn
# x_data_df['raw_data'] = x_data_df['raw_data'].apply(literal_eval)
#x_data_df['raw_data'] = x_data_df.apply(lambda row: pca.fit(row['raw_data']), axis=1)

x_data_df['raw_data'] = x_data_df['raw_data'].apply(lambda x: x[1:len(x)-1].split(','))

x_data_df['raw_data'] = x_data_df['raw_data'].apply(lambda x: np.array(x))

#x_data_df['raw_data'] = x_data_df['raw_data'].apply(lambda x: np.array(x))






#list(map(float, a[0].split("*")))


#x_test_df = data_train[['period','closer#','category','label','Silhouette']]
#dt_clf = DecisionTreeClassifier(random_state = 11) # decision tree

X_train,X_test, y_train, y_test = train_test_split(x_data_df,y_data_df,test_size=0.2,random_state=11)

rf_clf = RandomForestClassifier(random_state = 11 ,n_jobs=-1) # random forest

rf_clf.fit(X_train,y_train)    # random forest training
rf_pred = rf_clf.predict(X_test)  # random forest predict

#x_test_df['result'] = rf_pred

print('Random Forest Accuracy :  ',accuracy_score(y_test,rf_pred))
print('Random Forest Precision :  ',precision_score(y_test,rf_pred))
print('Random Forest Recall :  ',recall_score(y_test,rf_pred))
print('Random Forest f1 :  ',f1_score(y_test,rf_pred))