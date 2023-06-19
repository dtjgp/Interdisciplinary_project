# 用来绘制关于合同id和用户类别的饼图

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import io

def Contractid_usertype_pie(iteration_time, contractid_usertype_share):
    images = []
    
    # 每一个合同号与用户类型的数据的矩阵为 (3，迭代次数)
    number_of_contract = contractid_usertype_share.shape[0]
    fig, axs = plt.subplots(1, number_of_contract)
    
    for j in range(contractid_usertype_share.shape[2]): # 迭代的次数
        fig, axs = plt.subplots(1, 5, figsize=(15, 3))  # Create 5 subplots
        # 将每个合同的信息分别提取出来
        for i in range(number_of_contract): # 合同的数量
            axs[i].pie(contractid_usertype_share[i, :, j], labels=['type0', 'type1', 'type2'], autopct='%1.1f%%')
            axs[i].axis('equal')  # Equal aspect ratio ensures the pie chart is circular
            axs[i].set_title(f"Contract {i+1} in {j+1} month")
            
        # Save the pie chart as an image in memory
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)

        # Load the image using PIL and append it to the images list
        image = Image.open(buf)
        images.append(image)

        # Close the pyplot figure to free up memory
        plt.close(fig) 

    # Save the images as an animated GIF
    images[0].save('contractid_customertype_share.gif', save_all=True, append_images=images[1:], duration=500, loop=0)

            
        
