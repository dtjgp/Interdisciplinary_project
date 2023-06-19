import numpy as np
import pandas as pd
from three_contractModel import *
from CustomerConsumption import CustomerConsumption
import pickle


def FindOptimalContract(selfid,self_contract, neighbor_contract):
    
    customer_array = CustomerConsumption('customer_consumption_total.csv', numberofcluster=3)
    contract_number = 5 # 定义合同的数量

    # 设定参数
    ypsilon = -0.2 # demand_elasticity
    p = 0.4 # assumed electricity price
    alpha = 1/ypsilon +1
    beta = p/(-alpha)
    
    # 找到对应的用户的数据
    self_customer_data = customer_array[selfid,:-1]
    self_customer_data = self_customer_data.reshape(1,-1)

    # 求出该用户的用电平均值
    customer_data_mean = self_customer_data.mean(axis=1)
    
    # 求出该用户的满意度(实时，单一用户)，使用的是four_customerUtilityOptContract这个模型中用到的公式
    self_satisify = np.zeros((1, self_customer_data.shape[1]))
    for i in range(self_customer_data.shape[1]):
        self_satisify[0][i] = customer_data_mean*beta*(1-(self_customer_data[0][i]/customer_data_mean)**alpha)
    
    # 求出该用户的总满意度
    self_satisify_sum = self_satisify.sum(axis=1)
    
    # 打开合同参数pickle文件
    with open('contract_price.pickle', 'rb') as f:
        contract_price_list = pickle.load(f)
        
    contract1_price = contract_price_list[0]
    contract2_price = contract_price_list[1]
    contract3_price = contract_price_list[2]
    contract4_price = contract_price_list[3]
    contract5_price = contract_price_list[4]
    
    # 在这里需要调用合同类，来进行计算
    Contract1 = ElectricityContract(contract1_price, 143.05, 1)
    Contract2 = ElectricityContract(contract2_price, 93.5, 2)
    Contract3 = ElectricityContract(contract3_price, 182.07, 3)
    Contract4 = ElectricityContract(contract4_price, 168.716, 4)
    Contract5 = ElectricityContract(contract5_price, 218.54, 5)
    
    
    
    #create a numpy array to store the energy consumption and the contract number
    self_consumption = np.zeros((contract_number,2))
    
    self_consumption[0,0] = Contract1.calculate_total_usage(self_customer_data)
    self_consumption[0,1] = Contract1.contract_number
    self_consumption[1,0] = Contract2.calculate_total_usage(self_customer_data)
    self_consumption[1,1] = Contract2.contract_number
    self_consumption[2,0] = Contract3.calculate_total_usage(self_customer_data)
    self_consumption[2,1] = Contract3.contract_number
    self_consumption[3,0] = Contract4.calculate_total_usage(self_customer_data)
    self_consumption[3,1] = Contract4.contract_number
    self_consumption[4,0] = Contract5.calculate_total_usage(self_customer_data)
    self_consumption[4,1] = Contract5.contract_number
    
    for i in range(len(self_consumption)):
        # 不能使用np.exp，因为np.exp的值太小，会出现问题
        # self_consumption[i,0] = np.exp(self_satisify_sum - self_consumption[i,0] + np.random.gumbel())
        self_consumption[i,0] = self_satisify_sum - self_consumption[i,0] + np.random.gumbel()
    
    # 判断目前的用户是哪个合同，并且找到邻居的合同
    contract_consumption = np.zeros((2,1))
    for i in range(len(self_consumption)):
        if self_consumption[i,1] == self_contract:
            contract_consumption[0,0] = self_consumption[i,0]
        elif self_consumption[i,1] == neighbor_contract:
            contract_consumption[1,0] = self_consumption[i,0]      
    # print(contract_consumption) 
    
    # compare the energy consumption and find the optimal contract
    if contract_consumption[0,0] < contract_consumption[1,0]: # 用户的效用越大越好
        optimal_contract = neighbor_contract
        #marker about whether the contract is changed
        whetherchanged = 1
    else:
        optimal_contract = self_contract
        whetherchanged = 0
    
    return optimal_contract, whetherchanged


if __name__ == '__main__':
    a, b = FindOptimalContract(10,1,3)
    print(a)
    print(b)
