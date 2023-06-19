import numpy as np
import pandas as pd
from three_contractModel import *
import pickle


# 该函数用于检测每一次的循环过程中，检测每个合同的市场份额是否低于了阈值
def MarketShareWarning(contract_number,round_data, InitialMarketShare):
    # warning_contract_number = 0
    warning_contract_number_reduce = 0
    warning_contract_number_increase = 0
    
    #每个合同的进价, 每个合同在变化的时候，都不能够低于这个数值，否则算作违规
    # EntryPrice_shift = 0.25
    EntryPrice_shift = 0.3
    EntryPrice_static = 50
    '''
    市场上的合同的变化规则如下：
    1. 如果合同的市场份额下降了50%以上，则合同的价格下降5%
    2. 如果合同的市场份额上升了50%以上，则合同的价格上升5%
    3. 合同在变化的过程中，不能够低于进价
    '''
    
    # change the round_data to numpy array
    round_data = np.array(round_data) # shape为(430, 2)
    InitialMarketShare = np.array(InitialMarketShare) # shape为(430, 2)
    
    # 获取每一个合同的市场份额
    round_contract_info = round_data[:,1] # 获取每一个用户的合同编号
    round_contract_number = np.zeros((contract_number, 1))
    round_contract_share = np.zeros((contract_number, 1))
    
    initial_contract_info = InitialMarketShare[:,1] 
    initial_contract_number = np.zeros((contract_number, 1))
    initial_contract_share = np.zeros((contract_number, 1))
    
    # 计算每一个合同的市场数量
    for i in range(contract_number):
        for j in range(len(round_contract_info)):
            if round_contract_info[j] == i+1:
                round_contract_number[i] += 1 
            if initial_contract_info[j] == i+1:
                initial_contract_number[i] += 1    
        
    # 计算每一个合同的市场份额
    for i in range(contract_number):
        round_contract_share[i] = round_contract_number[i] / np.sum(round_contract_number)
        initial_contract_share[i] = initial_contract_number[i] / np.sum(initial_contract_number)
    
    # 判断合同的市场份额是否比初始的时候低
    # initial_contract_share是最开始的市场份额
    # round_contract_share是每一轮的市场份额
    # need to find out the market share loss: parameter: share_div
    share_div = np.zeros((contract_number, 1))
    for i in range(contract_number):
        share_div[i] = (initial_contract_share[i] - round_contract_share[i]) / initial_contract_share[i] # 计算每个合同的市场份额的损失比值
        
        # 市场份额下降的合同编号
        if share_div[i] > 0.5:
            print(f"Warning: The market share of contract {i+1} is reduced more than 50%")
            warning_contract_number_reduce = i+1
        # 市场份额上升的合同编号
        elif share_div[i] < -0.5:
            print(f"Warning: The market share of contract {i+1} is increased more than 50%")
            warning_contract_number_increase = i+1
        else:
            pass
        
    # # 检测每一个合同的市场份额是否低于阈值
    # for i in range(len(round_contract_share)):
    #     if round_contract_share[i] < 0.1:
    #         print(f"Warning: The market share of contract {i+1} is lower than 10%")
    #         # 提取该数值，用于调用three_contractModel.py中的函数
    #         warning_contract_number = i+1     
  
    # 如果没有合同的市场份额低于阈值，则不需要调用three_contractModel.py中的函数
    if warning_contract_number_reduce == 0:
        print("No contract is in warning state in reduce")
    else:
        # 读取合同价格pickle数据
        with open('contract_price.pickle', 'rb') as f:
            contract_price_list = pickle.load(f)
        # 读取合同价格数据

        type_list = [1, 2, 3, 4, 5]
        for i in range(len(type_list)):
            if type_list[i] == warning_contract_number_reduce:
                #首先将合同的价格降低5%
                contract_price_list[i] = contract_price_list[i] * 0.95 
                # 判断合同的各个时间段的价格是否低于进价,如果低于进价，则按照进价进行计算
                for j in range(len(contract_price_list[i])):
                    if contract_price_list[i][j] < EntryPrice_shift:
                        contract_price_list[i][j] = EntryPrice_shift
                    else:
                        pass

        with open("contract_price.pickle", "wb") as f:
            pickle.dump(contract_price_list, f)
    
    if warning_contract_number_increase == 0:
        print("No contract is in warning state in increase")
    else:
        # 读取合同价格pickle数据
        with open('contract_price.pickle', 'rb') as f:
            contract_price_list = pickle.load(f)
        # 读取合同价格数据
        type_list = [1, 2, 3, 4, 5]
        for i in range(len(type_list)):
            if type_list[i] == warning_contract_number_increase:
                #首先将合同的价格增加5%
                contract_price_list[i] = contract_price_list[i] * 1.05
        
        with open("contract_price.pickle", "wb") as f:
            pickle.dump(contract_price_list, f)
        

