#define a function to plot a linechart

import matplotlib.pyplot as plt
import numpy as np

def PlotLine_retailor(contract_market_share):
    plt.figure()
    for i in range(contract_market_share.shape[0]):
        plt.plot(contract_market_share[i, :], label=f"contract{i+1}")
    plt.legend()
    plt.xlabel("iteration")
    plt.ylabel("contract market share")
    plt.title("Contract market share iteration")
    
    # Save the image
    plt.savefig('linechart_retailor.png')
    
    plt.close()
    
    