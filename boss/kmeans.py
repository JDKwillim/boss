import random
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt
# 读取数据
d=pd.read_csv('job_clean2.csv')
d.info()
df=pd.read_csv('job_clean2.csv',usecols=[3,11])
# print(df.head(5))
# print(df['experience'].unique())

# 标准化 归一化
z_scaler=preprocessing.StandardScaler()
data_z=z_scaler.fit_transform(df)
data_z=pd.DataFrame(data_z)

minmax_scale=preprocessing.MinMaxScaler().fit(data_z)
dataa=minmax_scale.transform(data_z)
print(pd.DataFrame(dataa))
#
# # k值选取
K=range(1,8)
meandistortions=[]

for k in K:
    kmeans=KMeans(n_clusters=k)
    kmeans.fit(dataa)
    meandistortions.append(
        sum(
            np.min(cdist(dataa,kmeans.cluster_centers_,'euclidean'),axis=1)/dataa.shape[0]
        )
    )
plt.plot(K,meandistortions,'bx--')
plt.xlabel('k')
plt.show()
#
k_means=KMeans(init='k-means++',n_clusters=4,max_iter=500)
k_means.fit(dataa)
label=k_means.fit_predict(dataa)
print(label)
print("--------11111111111111111111111--")
print(dataa)
#
colors=['blue','green','red','purple']
for i in range(4):
    plt.scatter(dataa[label==i,0],dataa[label==i,1],s=50,c=colors[i],marker='o',alpha=0.5)
    plt.scatter(k_means.cluster_centers_[:,0],k_means.cluster_centers_[:,1],s=200,c='black',marker='*',label='Centroids')
    plt.legend()
    plt.grid()
plt.show()
data1=d['job_title']
data2=data1.values

dat_type=pd.DataFrame(label)
dat_type.columns=['类别']
dat=pd.merge(d,dat_type,left_index=True,right_index=True)
pd.set_option('display.max_row',None)
# print(dat.sort_values('类别'))
# dat.to_csv('jieguo.csv',index=False,encoding='utf8')
