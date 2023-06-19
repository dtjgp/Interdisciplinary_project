import os
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np


def CustomerConsumption(file_path, numberofcluster): # file_path为用户的用电数据的路径，numberofcluster为聚类的类别数
    
    df = pd.read_csv(file_path) # 读取用户的用电数据，数据为csv格式，用电数据是一天的用电量，每半小时进行一次记录，共48个数据
    customer_data = df.iloc[:, 1:]
    customer_array = customer_data.values
    customer_array = customer_array.T # 将数据转换为numpy array的格式，方便后续的处理，转置之后数据的格式为(430,48)，430为用户的数量，48为每个用户的用电数据
    
    kmenas = KMeans(n_clusters=numberofcluster)
    kmenas.fit(customer_array)
    K_means_labels = kmenas.labels_
    K_means_labels = K_means_labels.reshape(-1,1) # 将聚类的结果转换为numpy array的格式，格式为(430,1)

    #add the label to the numpy array
    customer_array = np.concatenate((customer_array, K_means_labels), axis=1) # 将聚类的结果添加到用户的用电数据中，格式为(430,49)
    
    average_use = np.zeros((numberofcluster, 2))#第一列存储平均值，第二列存储label，格式为(3,2)


    for i in range(numberofcluster): #对于每一个类别
        # print(i)
        # define a temp array to store the data
        temp = []
        for j in range(len(customer_array)): #对于每一个用户
            if customer_array[j][-1] == i:
                temp.append(customer_array[j,:-1]) #存储了目前所有的数据
        temp = np.array(temp)
        # print(temp.shape)
        
        # 求解平均值，为的是求解每一个类别中，所有的用户的平均用电量，然后将平均用电量从大到小进行排序，然后将用户的label进行重新排序
        temp_mean = temp.mean(axis=0) 
        temp_sum = temp_mean.sum()
        average_use[i][0] = temp_sum
        average_use[i][1] = i
    # sort the average_use from the big to small
    average_use = average_use[average_use[:,0].argsort()[::-1]] # 将平均用电量从大到小进行排序
    # print(average_use)
    
    # 将用户的label进行重新排序
    for i in range(len(customer_array)):
        for j in range(len(average_use)):
            if customer_array[i][-1] == average_use[j][-1]:
                customer_array[i][-1] = (j+1)*10
    # print(customer_array)

    # customer_array last column devided by 10, and then substract 1
    customer_array[:,-1] = (customer_array[:,-1]/10 - 1).astype(int)
    # print(customer_array)

    ####################################################################################################
    # 给数据增加行名称和列名称，并最终保存为csv文件
    # transfer the numpy array to pandas dataframe
    # add row name and column name
    
    column_name = [x for x in range(48)]
    for i in column_name:
        column_name[i] = 'timestamp' + str(i)
    column_name.insert(48, 'customer_type')
    
    row_name = [x for x in range(430)]
    for i in row_name:
        row_name[i] = 'customer' + str(i)
    
    df = pd.DataFrame(customer_array, index=row_name, columns=column_name)
    # save the dataframe to csv file
    df.to_csv('customer_consumption_type_combine.csv', index=False)
    
    
    return customer_array

# a = CustomerConsumption('customer_consumption_total.csv')
# print(a.shape)
# numberofcluster = 3
    
# df = pd.read_csv('customer_consumption_total.csv')
# customer_data = df.iloc[:, 1:]
# customer_array = customer_data.values
# customer_array = customer_array.T

# kmenas = KMeans(n_clusters=numberofcluster)
# kmenas.fit(customer_array)
# K_means_labels = kmenas.labels_
# K_means_labels = K_means_labels.reshape(-1,1)
# # print(K_means_labels.shape)
# customer_array = np.concatenate((customer_array, K_means_labels), axis=1) 
# # print(customer_array.shape)

# # define a array to store the average use and label
# average_use = np.zeros((numberofcluster, 2))#第一列存储平均值，第二列存储label


# for i in range(numberofcluster): #对于每一个类别
#     # print(i)
#     # define a temp array to store the data
#     temp = []
#     for j in range(len(customer_array)): #对于每一个用户
#         if customer_array[j][-1] == i:
#             temp.append(customer_array[j,:-1]) #存储了目前所有的数据
#     temp = np.array(temp)
#     # print(temp.shape)
    
#     # 求解平均值
#     temp_mean = temp.mean(axis=0)
#     temp_sum = temp_mean.sum()
#     average_use[i][0] = temp_sum
#     average_use[i][1] = i
# # sort the average_use from the big to small
# average_use = average_use[average_use[:,0].argsort()[::-1]]
# print(average_use)
        
# for i in range(len(customer_array)):
#     for j in range(len(average_use)):
#         if customer_array[i][-1] == average_use[j][-1]:
#             customer_array[i][-1] = (j+1)*10
# # print(customer_array)

# # customer_array last column devided by 10, and then substract 1
# customer_array[:,-1] = (customer_array[:,-1]/10 - 1).astype(int)
# print(customer_array)
# 按照设定值来对不同的用户进行分类，其中2为低用电量用户，1为中用电量用户，0为高用电量用户
if __name__ == '__main__':
    CustomerConsumption('customer_consumption_total.csv')
    print('Done!')
