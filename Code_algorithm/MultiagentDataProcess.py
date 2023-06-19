import pandas as pd
import numpy as np
import os
import shutil
'''
该函数进行的处理包括：
1. 每个用户的合同信息随着迭代次数的变化
2. 对于每个合同，其选择人群的类别随着迭代次数的变化
'''
def MultiagentDataProcess(contract_number, data, numberofcluster):
    # 输入进来的data为一个ndarray, shape为 (迭代次数, 430, 3)
    # 430为用户的数量，3为用户的id和合同编号和用户的类型
    # 该函数的作用是将数据转换为一个dataframe, 并且将用户的id和合同编号分别作为index和columns
    
    length_of_data = data.shape[0] # 获取数据的长度, 即迭代次数
    
    id_info = data[0,:,0].reshape(-1,1) # 获取用户的id信息, shape为(430, 1)
    contract_info = data[:,:,1].T # 获取用户的合同信息, 所有迭代次数下，所有的用户的合同编号， shape为(430, 迭代次数)
    
    # 计算每一类的用户的数量
    list_of_cluster = [i for i in range(numberofcluster)] # shape is (3,)
    # print(list_of_cluster)
    list_of_type = [] # 用来保存每一类用户的数量
    customer_type_data = data[0,:,:] # 获取第一次迭代的数据, shape为(430, 3), 通过这个便可以获得用户的类型信息
    # print(customer_type_data.shape)
    for j in range(len(list_of_cluster)):
        sum = 0
        for i in range(len(customer_type_data)):
            if customer_type_data[i,2] == list_of_cluster[j]:
                sum += 1
        list_of_type.append(sum)
    # print(list_of_type)
    list_of_type = np.array(list_of_type)
    list_of_type = list_of_type.reshape(-1,1)
    # print(list_of_type)
    
    #************************************************************************************************************************
    # 第一部分，提取用户的合同信息的变化，将其转换为一个dataframe
    # 将用户的id和合同信息合并，其中每一行代表一个用户的合同信息随着迭代次数的变化
    result_userid_contract = np.concatenate((id_info, contract_info), axis=1)
    
    # 将数据转换为dataframe
    df_id_contract = pd.DataFrame(result_userid_contract)   
    # save the data to csv
    df_id_contract.to_csv('customer_id_contract_data.csv', index=False) # 将用户的id和其选择合同号保存为csv文件
    
    # 计算result中，每一个contract的数量
    contract_market_number = np.zeros((contract_number, length_of_data))
    contract_market_share = np.zeros((contract_number, length_of_data))
    
    # 计算每一个合同的市场份额
    for i in range(length_of_data):
        round_contract_info = result_userid_contract[:,i+1]
        for k in range(contract_number):
            for j in range(len(round_contract_info)):
                if round_contract_info[j] == k+1:
                    contract_market_number[k][i] += 1
    
    # 计算每一个合同的市场份额
    for i in range(length_of_data):
        for k in range(contract_number):
            contract_market_share[k][i] = contract_market_number[k][i] / np.sum(contract_market_number[:,i])
    
    # 将数据转换为dataframe
    df1 = pd.DataFrame(contract_market_number)   
    df2 = pd.DataFrame(contract_market_share)
    
    # save the data to csv
    df1.to_csv('contract_market_number.csv', index=False)
    df2.to_csv('contract_market_share.csv', index=False)
    
    #************************************************************************************************************************
    # 第二部分，提取合同的选择人群的类别信息，将其转换为一个dataframe
    # 为每一个合同都设置一个ndarray，能够保存每次迭代过程中，其选择人群的类别信息
    contractid_usertype_number = np.zeros((contract_number, numberofcluster, length_of_data))
    contractid_usertype_share = np.zeros((contract_number, numberofcluster, length_of_data))
    
    for m in range(length_of_data): # 遍历每一次迭代
        # 获取每一次迭代的信息，其中包括合同号信息以及用户的类别信息，删除掉用户的id信息
        round_info = data[m,:,1:] # shape为(430, 2)，其中第一列为合同号选择信息，第二列为用户的类别信息
        
        for i in range(contract_number): # 遍历每一个合同号
            # 提取出round_info中的合同i的信息，其中第一列为合同号选择信息，第二列为用户的类别信息
            round_info_contracti = round_info[round_info[:,0] == i+1] #找出了这一次迭代中，所有合同号为i+1的用户的信息
            
            for k in range(numberofcluster): # 遍历每一个用户的类别, 0, 1, 2
                # 遍历合同i中的每一个用户，并将他们的类别信息进行统计
                for j in range(len(round_info_contracti)):
                    if round_info_contracti[j,1] == k: # 如果用户的类别为k
                        contractid_usertype_number[i,k,m] += 1 # 合同i中的类别为k的用户在第m次迭代中的数量加1
                    
    # 计算每一个合同的市场份额
    for i in range(contract_number):
        for j in range(numberofcluster):
            contractid_usertype_share[i,j,:] = contractid_usertype_number[i,j,:] / list_of_type[j]
        
    
    # 对每一个合同的信息进行保存
    contract1_usertype_number = contractid_usertype_number[0,:,:]
    contract1_usertype_share = contractid_usertype_share[0,:,:]
    contract2_usertype_number = contractid_usertype_number[1,:,:]
    contract2_usertype_share = contractid_usertype_share[1,:,:]
    contract3_usertype_number = contractid_usertype_number[2,:,:]
    contract3_usertype_share = contractid_usertype_share[2,:,:]
    contract4_usertype_number = contractid_usertype_number[3,:,:]
    contract4_usertype_share = contractid_usertype_share[3,:,:]
    contract5_usertype_number = contractid_usertype_number[4,:,:]
    contract5_usertype_share = contractid_usertype_share[4,:,:]
    
    # 将数据转换为dataframe
    df_contract1_usertype_number = pd.DataFrame(contract1_usertype_number)
    df_contract1_usertype_share = pd.DataFrame(contract1_usertype_share)
    df_contract2_usertype_number = pd.DataFrame(contract2_usertype_number)
    df_contract2_usertype_share = pd.DataFrame(contract2_usertype_share)
    df_contract3_usertype_number = pd.DataFrame(contract3_usertype_number)
    df_contract3_usertype_share = pd.DataFrame(contract3_usertype_share)
    df_contract4_usertype_number = pd.DataFrame(contract4_usertype_number)
    df_contract4_usertype_share = pd.DataFrame(contract4_usertype_share)
    df_contract5_usertype_number = pd.DataFrame(contract5_usertype_number)
    df_contract5_usertype_share = pd.DataFrame(contract5_usertype_share)
    
    # save the data to csv
    df_contract1_usertype_number.to_csv('contract1_usertype_number.csv', index=False)
    df_contract1_usertype_share.to_csv('contract1_usertype_share.csv', index=False)
    df_contract2_usertype_number.to_csv('contract2_usertype_number.csv', index=False)
    df_contract2_usertype_share.to_csv('contract2_usertype_share.csv', index=False)
    df_contract3_usertype_number.to_csv('contract3_usertype_number.csv', index=False)
    df_contract3_usertype_share.to_csv('contract3_usertype_share.csv', index=False)
    df_contract4_usertype_number.to_csv('contract4_usertype_number.csv', index=False)
    df_contract4_usertype_share.to_csv('contract4_usertype_share.csv', index=False)
    df_contract5_usertype_number.to_csv('contract5_usertype_number.csv', index=False)
    df_contract5_usertype_share.to_csv('contract5_usertype_share.csv', index=False)
    
    #************************************************************************************************************************
    # 第三部分，将所有生成的暂时用不到的数据，保存到一个文件夹中
    # # 创建一个文件夹
    # folder_name = 'MultiagentDataProcess_data'
    # if not os.path.exists(folder_name):
    #     os.makedirs(folder_name)
    
    # file_list = ['contract_market_number.csv', 'contract_market_share.csv', 'contract1_usertype_number.csv',
    #              'contract1_usertype_share.csv', 'contract2_usertype_number.csv', 'contract2_usertype_share.csv',
    #              'contract3_usertype_number.csv', 'contract3_usertype_share.csv', 'contract4_usertype_number.csv',
    #              'contract4_usertype_share.csv', 'contract5_usertype_number.csv', 'contract5_usertype_share.csv']
    # for i in file_list:
    #     shutil.move(i, folder_name)
    
    return contract_market_number, contract_market_share, contractid_usertype_number, contractid_usertype_share