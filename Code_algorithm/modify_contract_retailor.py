# it is for modify contract of the retailor in the retailor's multiagent environment
# just to see the contract market share can shifted as the retailor's contract changed

import pickle
import numpy as np
import pandas as pd

def modify_contract_retailor():
    #**********************************************************************************************************************
    # read the file of each contract market number
    # first, read the market number of each contract, which is the contract_market_number.csv
    contract_market_number = pd.read_csv('contract_market_number.csv')
    # transfer the data into numpy array
    contract_market_number = contract_market_number.values
    # extract the last iteration of the regulator multiagent model run
    last_contract_market_number = contract_market_number[:,-1]
    # extract the initial contract market number
    initial_contract_market_number = contract_market_number[:,0]
    
    #**********************************************************************************************************************
    # read the files of each contract dynamic price
    # read the contract1_price_iter.csv, contract2_price_iter.csv, contract3_price_iter.csv, contract4_price_iter.csv, contract5_price_iter.csv
    # contract1_price_iter = pd.read_csv('contract1_price_iter.csv')
    # contract2_price_iter = pd.read_csv('contract2_price_iter.csv')
    # contract3_price_iter = pd.read_csv('contract3_price_iter.csv')
    # contract4_price_iter = pd.read_csv('contract4_price_iter.csv')
    # contract5_price_iter = pd.read_csv('contract5_price_iter.csv')
    # # transfer the data into numpy array
    # contract1_price_iter = contract1_price_iter.values
    # contract2_price_iter = contract2_price_iter.values
    # contract3_price_iter = contract3_price_iter.values
    # contract4_price_iter = contract4_price_iter.values
    # contract5_price_iter = contract5_price_iter.values
    # # extract the price of each contract
    # contract1_price_iter = contract1_price_iter[:,1:]
    # contract2_price_iter = contract2_price_iter[:,1:]
    # contract3_price_iter = contract3_price_iter[:,1:]
    # contract4_price_iter = contract4_price_iter[:,1:]
    # contract5_price_iter = contract5_price_iter[:,1:]
    # # concatenate the contract price
    # contract_price_iter = np.stack((contract1_price_iter, contract2_price_iter, contract3_price_iter, contract4_price_iter, contract5_price_iter)) # the shape is (5,3,49)
    # initial_contract_price = contract_price_iter[:,:,1] # the shape is (5,3,1)
    
    
    mod_whether_mod= input('Do you want to modify the contract data? (y/n)')
    if mod_whether_mod == 'n':
        pass
    elif mod_whether_mod == 'y':
        mod_contract_number = int(input('Please input the contract number you want to modify:'))
        
        # open the contract_price.pickle
        with open("contract_price_retailor.pickle", "rb") as p:
            contract_price_after_iteration = pickle.load(p) # the data is the contract price after iteration of the regulator multiagent model run
        with open('static_price.pickle', 'rb') as p:
            static_price = pickle.load(p)
        
        print('You are modifying the contract', mod_contract_number)
        print('The number of users in the begining is:', int(initial_contract_market_number[mod_contract_number - 1]), 'And now there are %d users:'%last_contract_market_number[mod_contract_number - 1])
        print('The contract price before modification is:', contract_price_after_iteration[mod_contract_number - 1], 'The static price is:', static_price[mod_contract_number - 1])
        
        # modify the contract price
        mod_contract_price_list = input('Please input the contract price you want to modify:') #input is a string
        mod_contract_price = mod_contract_price_list.split(',') # split the string into a list
        mod_contract_price = [float(i) for i in mod_contract_price] # convert the string into float
        
        # change the mod_contract_price into numpy array
        mod_contract_price = np.array(mod_contract_price)
        
        # transfer the data into 
        contract_price_after_iteration[mod_contract_number-1] = mod_contract_price
        print('The contract price after modification is:', contract_price_after_iteration[mod_contract_number-1])
        
        # save the data in the pickle
        with open("contract_price_retailor.pickle", "wb") as p:
            pickle.dump(contract_price_after_iteration, p)
        
        
        
    