# 用来绘制每一个合同中，价格的动态变化

import matplotlib.pyplot as plt
import numpy as np

def Contract_price_line(contract_price): # contract_price: (iteration, 5, 3)
    # 将contract_price的数据转换成(5, 3, iteration)的形式
    contract_price = np.transpose(contract_price, (1, 2, 0))
    
    number_of_contract = contract_price.shape[0] # 合同的数量
    
    fig, axs = plt.subplots(number_of_contract, 1, figsize=(10, 20))  # Create 5 subplots
    
    for i in range(number_of_contract):
        contracti_dynamic_part = contract_price[i, :, :]
        for j in range(contracti_dynamic_part.shape[0]):
            axs[i].plot(contracti_dynamic_part[j, :], label=f"contract{i+1}, F{j+1}")
            axs[i].axhline(0.25, color='r', linestyle='--') # 画出0.25的水平线
            
            axs[i].legend()
            axs[i].set_xlabel("iteration")
            axs[i].set_ylabel("price of contract")
            axs[i].set_title(f"User type share iteration for contract {i+1}")
    plt.tight_layout()
    plt.savefig('contract_dynamic_price_line.png')
    plt.close()