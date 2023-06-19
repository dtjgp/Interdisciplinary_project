import pickle
import numpy as np

#read the pickle file
with open('contract_price.pickle', 'rb') as f:
    contract_price_list = pickle.load(f)
print(contract_price_list)

# type_list = [1, 2, 3, 4, 5]
# for i in range(len(type_list)):
#     if type_list[i] == 2:
#         contract_price_list[i] = contract_price_list[i] * 0.8    

# with open("contract_price.pickle", "wb") as f:
#     pickle.dump(contract_price_list, f)
    
# with open('contract_price.pickle', 'rb') as f:
#     contract_price_list = pickle.load(f)
# print(contract_price_list)
