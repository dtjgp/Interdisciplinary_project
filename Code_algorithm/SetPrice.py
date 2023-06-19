import pickle
import numpy as np  

def SetPrice():
    contract1_price = [0.446, 0.446, 0.446]
    contract2_price = [0.498824, 0.412275, 0.412275]
    contract3_price = [0.4082, 0.3641, 0.2815]
    contract4_price = [0.4209, 0.4209, 0.4209]
    contract5_price = [0.3478, 0.3478, 0.3478]

    price_list = [contract1_price, contract2_price, contract3_price, contract4_price, contract5_price]
    price_list = np.array(price_list)
    
    # 保存数据
    with open("contract_price.pickle", "wb") as p:
        pickle.dump(price_list, p)
        
    static_price = [143.05, 93.5, 182.07, 168.716, 218.54]
    static_price = np.array(static_price)
    static_price = static_price.reshape(-1,1)
    with open("static_price.pickle", "wb") as p:
        pickle.dump(static_price, p)
    
if __name__ == '__main__':
    SetPrice()