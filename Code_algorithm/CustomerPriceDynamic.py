# 对合同的动态部分进行数据处理
# 读取合同信息，并且能够生成合同在每次迭代的时候的价格数据

import pandas as pd
import numpy as np
import os
import shutil

def CustomerPriceDynamic(contract_price):
    contract_price = np.array(contract_price) # shape of the contract_price is (iteration, 5, 3)
    contract_price = np.transpose(contract_price, (1, 2, 0)) # change the shape to (5, 3, iteration)
    
    contract1_price = contract_price[0, :, :] # shape of the contract1_price is (3, iteration)
    contract2_price = contract_price[1, :, :] # shape of the contract2_price is (3, iteration)
    contract3_price = contract_price[2, :, :] # shape of the contract3_price is (3, iteration)
    contract4_price = contract_price[3, :, :] # shape of the contract4_price is (3, iteration)
    contract5_price = contract_price[4, :, :] # shape of the contract5_price is (3, iteration)
    
    # change the ndarray to dataframe
    contract1_price = pd.DataFrame(contract1_price)
    contract2_price = pd.DataFrame(contract2_price)
    contract3_price = pd.DataFrame(contract3_price)
    contract4_price = pd.DataFrame(contract4_price)
    contract5_price = pd.DataFrame(contract5_price)
    
    # save the dataframe to csv file
    contract1_price.to_csv('contract1_price_iter.csv')
    contract2_price.to_csv('contract2_price_iter.csv')
    contract3_price.to_csv('contract3_price_iter.csv')
    contract4_price.to_csv('contract4_price_iter.csv')
    contract5_price.to_csv('contract5_price_iter.csv')
    
    # folder_name = 'contract_price_iter'
    # if not os.path.exists(folder_name):
    #     os.makedirs(folder_name)
        
    # file_list = ['contract1_price_iter.csv', 'contract2_price_iter.csv', 'contract3_price_iter.csv',
    #              'contract4_price_iter.csv', 'contract5_price_iter.csv']
    # for i in file_list:
    #     shutil.move(i, folder_name)