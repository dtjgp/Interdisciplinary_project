# 该段代码用于显示合约的动态价格，并且能够返回是否有合同不太正常的价格设置

import pickle

def Contract_dynamic_price(): 
    # 读取合同价格pickle数据
    with open('contract_price.pickle', 'rb') as f:
        contract_price_list = pickle.load(f)
    # print(contract_price_list)
    
    return contract_price_list
    
    
    
    
    
if __name__ == '__main__':
    Contract_dynamic_price()