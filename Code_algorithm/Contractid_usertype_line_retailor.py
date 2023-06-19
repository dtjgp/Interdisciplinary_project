# 用来绘制每一个合同中，不同类别的用户的份额随着迭代次数的变化

import matplotlib.pyplot as plt
import numpy as np

def Contractid_usertype_line_retailor(contractid_usertype_share):
    number_of_contract = contractid_usertype_share.shape[0]
    
    fig, axs = plt.subplots(number_of_contract, 1, figsize=(10, 20))  # Create 5 subplots
    
    for i in range(number_of_contract):
        user_typei = contractid_usertype_share[i, :, :]
        for j in range(user_typei.shape[0]):
            axs[i].plot(user_typei[j, :], label=f"contract{i+1}, type{j}")
            
            axs[i].legend()
            axs[i].set_xlabel("iteration")
            axs[i].set_ylabel("user type share")
            axs[i].set_title(f"User type share iteration for contract {i+1}")
    plt.tight_layout()
    plt.savefig('contractid_usertype_line_retailor.png')
    plt.close()
        