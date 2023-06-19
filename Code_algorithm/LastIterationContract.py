# 这个函数是用来retailor的模型计算中，帮助其提取最后一次迭代之后，各个合同的市场份额的函数

import pandas as pd
import numpy as np

def LastIterationContract(filepath):
    
    # read the file of the customer_id_contract_data.csv
    df_id_contract = pd.read_csv('customer_id_contract_data.csv')
    
    #transform the dataframe to a ndarray
    id_contract = np.array(df_id_contract) # shape is (430, iteration_time+1)
    
    # get the last iteration of the contract data
    last_iteration_contract = id_contract[:, -1].reshape(-1,1) # shape is (430,1)
    # get the customer's id
    customer_id = last_iteration_contract[:,0].reshape(-1,1) # shape is (430,1)
    
    # concate the customer_id and customer_consumption and customer_type
    customer_info_array = np.concatenate((customer_id, last_iteration_contract), axis=1) # shape is (430,2)
    
    return customer_info_array