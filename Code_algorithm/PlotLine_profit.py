# plot the profit of each contract through the iteration in the line

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def PlotLine_profit(profit_list):
    profit_list = profit_list.T # shape:(5, iteration)
    plt.figure()
    for i in range(len(profit_list)):
        plt.plot(profit_list[i], label=f"contract{i+1}")
    plt.legend()
    plt.xlabel("iteration")
    plt.ylabel("profit")
    plt.title("Profit iteration")
    
    # Save the image
    plt.savefig('linechart_profit.png')
    
    plt.close()