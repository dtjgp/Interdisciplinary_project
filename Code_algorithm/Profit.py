import pandas as pd
import numpy as np
from three_contractModel import *
import pickle 

# 获取每一个用户的用电数据，然后计算用户在其选择的合同下，一个月的电费
# 目前的合同计算的是用户的一年的电费，所以在计算用户该月使用这个合同的电费的时候，需要将一年的用电成本除以12
# 计算合同的成本开销的时候，需要将使用其合同的用户的用电数据乘以成本价格，然后再除以12
def Profit(round_data):
    # preprocess the round_data
    # change the round_data from a list to ndarray
    round_data = np.array(round_data) # shape:(430, 3),其中包括用户id，合同编号，用户类型
    # print("round_data's shape is:", round_data.shape)
    
    # get the contract_number data and reshape to (430,2)
    userid_conid = round_data[:,:2].reshape(430,2) # shape:(430,2)
    # print("userid_conid's shape is:", userid_conid.shape)
    
    # read the contract price data
    customer_consumption = pd.read_csv('customer_consumption_type_combine.csv') 
    # transform the customer_consumption to ndarray
    customer_consumption = np.array(customer_consumption) # shape:(430, 49), in which the last column is the customer type
    customer_consumption = customer_consumption[:,:-1] # shape:(430, 48)
    # print("customer_consumption's shape is:", customer_consumption.shape)
    
    # concat the user consumption data and the contract price data
    cus_consumption_contractid = np.concatenate((customer_consumption, userid_conid), axis=1) # shape:(430, 50), contains the user consumption and the user id and contract id
    # print("cus_consumption_contractid's shape is:", cus_consumption_contractid.shape)
    
    # read the pickle data of the contract dynamic price
    with open('contract_price.pickle', 'rb') as f:
        contract_price = pickle.load(f) # shape:(5,3)
    
    # read the pickle data of the contract static price
    with open('static_price.pickle', 'rb') as f:
        static_price = pickle.load(f) # shape:(5,1)
    static_price = np.array(static_price).reshape(-1,1) # shape:(5,1)
    # print("static_price's shape is:", static_price.shape)
    # for i in range(len(static_price)):
    #     print(static_price[i,0])
        
    list_of_contract = [i for i in range(1,6)]
    # change the list_of_contract to ndarray
    list_of_contract = np.array(list_of_contract).reshape(-1,1) # shape:(5,1)
    # print("list_of_contract's shape is:", list_of_contract.shape)
    
    # concat the list_of_contract and the contract_price
    contract_price = np.concatenate((list_of_contract, contract_price), axis=1) # shape:(5,4), the first column is the contract id
    # print("contract_price's shape is:", contract_price.shape)
    
    # set the pruchase price of each contract
    purchase_price = [0.3, 0.3, 0.3]# this part can be represented a function in the future
    # purchase_price = [0.25, 0.25, 0.25]# this part can be represented a function in the future

    purchase_price = np.array(purchase_price).reshape(-1,1) # shape:(3,1)
    '''
    just set the dynamic part in here, in the future we can change it to a function
    '''
    
    # set a list to store the number of each contract has
    list_of_userid_conid = []
    # list_of_userid_conid_num = []
    for j in range(5): # in here, range(1,6) means the contract id is from 1 to 5
        templist = []
        # sum = 0
        for i in range(len(cus_consumption_contractid)):
            if cus_consumption_contractid[i,-1] == j+1:
                # sum += 1
                templist.append(cus_consumption_contractid[i,-2:])
        templist = np.array(templist).reshape(-1,2)
        
        # concat the templist and the list_of_userid_conid
        list_of_userid_conid.append(templist)
        # list_of_userid_conid_num.append(sum)
    
    # set a list to store the consumption of each contract
    list_of_each_contract_consumption = []
    for i in range(len(list_of_userid_conid)): # for each contract
        contracti = list_of_userid_conid[i] # shape:(n,2)
        templist = []
        for j in range(len(contracti)): # for each user
            userid_temp = contracti[j,0]
            # print(type(userid_temp), userid_temp)
            # print(userid_temp)
            templist.append(cus_consumption_contractid[int(userid_temp),:-2])
        templist = np.array(templist).reshape(-1,48)
        list_of_each_contract_consumption.append(templist) # shape:(5,n,48)  
    # print(len(list_of_each_contract_consumption))
    
    # calculate the consumption of each contract and the purchase price of each contract
    profit_list = []
    for i in range(len(list_of_each_contract_consumption)):
        # in the loop function, i is the contract id, and in here, we need to calculate the consumption of each contract as well as the purchase price of each contract
        # set the contract model of contract i
        contracti_consumption = list_of_each_contract_consumption[i]
        contract_dynamic_price = contract_price[i,1:]
   
        ContractModeli = ElectricityContract(contract_dynamic_price, static_price[i], i+1)
        ContractModel_purchase = ElectricityContract(purchase_price, static_price[i], i+1)
        # calculate the consumption of the contract i users
        contracti_user_fee = ContractModeli.calculate_total_usage(contracti_consumption) # cost of users who choose the contract i, shape:(n,1)
        # calculate the purchase price of the contract i users
        contracti_purchase = ContractModel_purchase.calculate_total_usage(contracti_consumption) # purchase price of contract i, shape:(n,1)
        
        # change the contracti_user_fee and contracti_purchase to ndarray
        contracti_user_fee = np.array(contracti_user_fee).reshape(-1,1)
        contracti_purchase = np.array(contracti_purchase).reshape(-1,1)
        
        # calculate the profit of the contract i
        sumation_of_the_profiti = (np.sum(contracti_user_fee) - np.sum(contracti_purchase))/12 # the result is a number of the single month profit of the contract i
        profit_list.append(sumation_of_the_profiti) # final profit result of each contract, shape:(5,1)
    
    return profit_list # shape:(5,1)    
                
    
    