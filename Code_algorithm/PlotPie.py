import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import io

def PlotPie(iteration_time, contract_market_share):
    images = []

    for j in range(contract_market_share.shape[1]):
        plt.figure()
        plt.pie(contract_market_share[:, j], labels=['contract1', 'contract2', 'contract3', 'contract4', 'contract5'], autopct='%1.1f%%')
        plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular

        #add a title
        # add a list of the months of the yeaer as labels
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', "Nov", "Dec"]
        # set list that can generate the list of months according to the iteration time
        month_list = []
        for i in range(iteration_time):
            month_list.append(months[i%12])
        plt.title(f"Contract market share iteration in {month_list[j]}")
        # plt.title(f"Contract market share iteration in {months[j]}")
        
        # Save the pie chart as an image in memory
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)

        # Load the image using PIL and append it to the images list
        image = Image.open(buf)
        images.append(image)

        # Close the pyplot figure to free up memory
        plt.close()

    # Save the images as an animated GIF
    images[0].save('animated_pie_charts.gif', save_all=True, append_images=images[1:], duration=500, loop=0)  