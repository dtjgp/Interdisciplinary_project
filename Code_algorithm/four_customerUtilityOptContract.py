import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt


def find_optimal_contract(alpha,beta):
    df1 = pd.read_csv('customer_consumption.csv')
    # timeslot_data = df1.iloc[:,0]
    customer_data = df1.iloc[:,1:]
    #对customer_data每列取平均值
    customer_data_mean = customer_data.mean(axis=0)
    customer_data_mean = customer_data_mean.values

    df2 = pd.read_csv('contracts_fee_total.csv')
    contracts_fee = df2.iloc[:,:]/365


    #根据每个客户的每天实际用电量求每一个客户的满意度
    satisify = np.zeros((len(customer_data),len(customer_data_mean)))
    for i in range(len(customer_data_mean)):
        for j in range (len(customer_data)):
            satisify[j][i] = customer_data_mean[i]*beta*(1-(customer_data.iloc[j,i]/customer_data_mean[i])**alpha)

    #求每个客户的总满足感, 对satisify每列相加
    satisify_sum = satisify.sum(axis=0)

    #每个客户对合同1-5的用户效用，即用客户总满足感减去合同的费用
    customer_utility = np.zeros((len(customer_data_mean),5))
    for i in range(len(customer_data_mean)):
        customer_utility[i][0] = satisify_sum[i] - contracts_fee.iloc[i,0]
        customer_utility[i][1] = satisify_sum[i] - contracts_fee.iloc[i,1]
        customer_utility[i][2] = satisify_sum[i] - contracts_fee.iloc[i,2]
        customer_utility[i][3] = satisify_sum[i] - contracts_fee.iloc[i,3]
        customer_utility[i][4] = satisify_sum[i] - contracts_fee.iloc[i,4] 


    #对用户效用加上一个随机数，该随机数相互独立且服从同gumble极值分布， 以便于在用户效用相同的情况下，随机选择一个合同
    customer_utility_random = np.zeros((len(customer_data_mean),5))
    for i in range(len(customer_data_mean)):
        customer_utility_random[i][0] = customer_utility[i][0] + np.random.gumbel()
        customer_utility_random[i][1] = customer_utility[i][1] + np.random.gumbel()
        customer_utility_random[i][2] = customer_utility[i][2] + np.random.gumbel()
        customer_utility_random[i][3] = customer_utility[i][3] + np.random.gumbel()
        customer_utility_random[i][4] = customer_utility[i][4] + np.random.gumbel()

    #计算对于每个用户，每个合同的用户效用比例
    customer_utility_random_ratio = np.zeros((len(customer_data_mean),5))
    exp_sum = np.zeros((len(customer_data_mean),1))
    for i in range(len(customer_data_mean)):
        exp_sum[i][0] = np.sum(np.exp(customer_utility_random[i]))
    for i in range(len(customer_data_mean)):
        customer_utility_random_ratio[i][0] = np.exp(customer_utility_random[i][0])/exp_sum[i]
        customer_utility_random_ratio[i][1] = np.exp(customer_utility_random[i][1])/exp_sum[i]
        customer_utility_random_ratio[i][2] = np.exp(customer_utility_random[i][2])/exp_sum[i]
        customer_utility_random_ratio[i][3] = np.exp(customer_utility_random[i][3])/exp_sum[i]
        customer_utility_random_ratio[i][4] = np.exp(customer_utility_random[i][4])/exp_sum[i]

    #找到每个客户对应的最大用户效用比例以及对应的合同，即最优合同
    customer_utility_random_ratio_max = np.zeros((len(customer_data_mean),2))
    for i in range(len(customer_data_mean)):
        customer_utility_random_ratio_max[i][0] = np.max(customer_utility_random_ratio[i])
        customer_utility_random_ratio_max[i][1] = np.argmax(customer_utility_random_ratio[i])+1

    #计算每个合同的用户数量和用户占比
    contract_user_num_ratio = np.zeros((5,2))
    for i in range(5):
        contract_user_num_ratio[i][0] = np.sum(customer_utility_random_ratio_max[:,1]==i+1)
        contract_user_num_ratio[i][1] = contract_user_num_ratio[i][0]/len(customer_utility_random_ratio_max)

    #画出两张图，表示用户选择最优合同后，合同数量和合同比例的分布
    plt.figure(1)
    plt.hist(customer_utility_random_ratio_max[:,1],bins=5,range=(1,6),rwidth=0.8)
    plt.xlabel('contract')
    plt.ylabel('Customer number')
    plt.title('Customer number of different contracts')
    plt.show()

    plt.figure(2)
    plt.bar([1,2,3,4,5],contract_user_num_ratio[:,1],width=0.8)
    plt.xlabel('contract')
    plt.ylabel('Customer ratio')
    plt.title('Customer ratio of different contracts')
    plt.show()

    return contract_user_num_ratio

#调用函数

ypsilon = -0.2 # demand_elasticity
p = 0.4 # assumed electricity price

alpha = 1/ypsilon +1
beta = p/(-alpha)

contract_user_num_ratio = find_optimal_contract(alpha,beta)
print(contract_user_num_ratio)


