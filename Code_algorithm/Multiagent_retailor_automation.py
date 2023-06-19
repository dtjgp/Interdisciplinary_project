import random
import numpy as np
import pandas as pd
from mesa import Agent, Model
from mesa.space import ContinuousSpace
from mesa.time import RandomActivation
import matplotlib.pyplot as plt
import imageio
from PIL import Image
import pickle
from SetPrice import SetPrice
from LastIterationContract import LastIterationContract
from Profit_retailor import Profit_retailor
from CustomerConsumption import CustomerConsumption
from FindOptimalContract_retailor import FindOptimalContract_retailor
from MultiagentDataProcess_retailor import MultiagentDataProcess_retailor
from PlotPie_retailor import PlotPie_retailor
from PlotLine_retailor import PlotLine_retailor
from MarketShareWarning import MarketShareWarning
from Contractid_usertype_pie_retailor import Contractid_usertype_pie_retailor
from Contractid_usertype_line_retailor import Contractid_usertype_line_retailor
from Contract_dynamic_price_retailor import Contract_dynamic_price_retailor
from Contract_price_line_retailor import Contract_price_line_retailor
from CustomerPriceDynamic_retailor import CustomerPriceDynamic_retailor
from PlotLine_profit_retailor import PlotLine_profit_retailor
from modify_contract_retailor import modify_contract_retailor
from pickle_regulator_retailor import pickle_regulator_retailor
from modify_contract_retailor_automation import modify_contract_retailor_automation

'''
在售电方的角度，用户此时的选择结果是定值，是根据前两年的运算结果出来的，所以需要跟regulator之间做一些调整
'''

class Person(Agent):
    # unique_id: agent的唯一标识符
    def __init__(self, unique_id, model): 
        super().__init__(unique_id, model) # 根据unique_id, 调取用户数据来匹配每一个用户的用电数据
        
        self.contract_number = self.get_contract_number() # 定义用户的合同编号
        self.old_contract = self.contract_number # 定义用户的旧合同编号
        self.type = self.get_type() # 定义用户的类型，0为高用电量用户，1为中用电量用户，2为低用电量用户，这部分在下面有专门的方法来定义
        self.fedality = self.determine_fedality() # 定义用户的忠诚度, 这部分在后面有专门的方法来定义
    
    def get_contract_number(self):
        customer_id = self.unique_id
        contract_number = customer_info_array[customer_id,1]
        return contract_number    
    
    # 通过unique_id来获取用户的用电数据
    def get_type(self):
        customer_id = self.unique_id
        customer_data = customer_array[customer_id,:]
        # print(customer_data.shape)
        type = customer_data[-1]
        return type      
    
    def step(self):
        self.move() # move方法
        other_person = self.interact() # interact方法
        if other_person:
            self.communicate_contract(other_person) # communicate_contract方法

    def move(self): 
        dx, dy = random.uniform(-1, 1), random.uniform(-1, 1) # 随机生成一个[-1,1]之间的数
        self.model.space.move_agent(self, (self.pos[0] + dx, self.pos[1] + dy)) # 移动agent

    def interact(self):  
        self.determine_fedality() # 确定用户的忠诚度
        # 定义用户的沟通成功率
        same_zone_rate = 0.7
        different_zone_rate = 0.3
        
        neighbors = self.model.space.get_neighbors(self.pos, radius=1, include_center=False)    # 获取agent的邻居
        same_zone_neighbors = [neighbor for neighbor in neighbors if self.get_zone() == self.get_zone()]    # 获取agent的同区域邻居
        different_zone_neighbors = [neighbor for neighbor in neighbors if self.get_zone() != self.get_zone()]   # 获取agent的不同区域邻居

        # 首先进行忠诚度判断
        if random.random() > self.fedality: # 如果随机数大于用户的忠诚度，则用户不会接受任何的变化
            return None
        # 如果用户的忠诚度低于阈值，则用户会接受新的合同
        else:
            # 该部分为模拟不同类型的用户在交换信息的时候，信息交换成功的概率较低，而相同的用户交换信息的时候，信息交换成功的概率较高
            if len(same_zone_neighbors) > 0 and random.random() < same_zone_rate: # 如果同区域邻居大于0且随机数小于0.9
                return random.choice(same_zone_neighbors)               # 随机返回一个同区域邻居
            elif len(different_zone_neighbors) > 0 and random.random() < different_zone_rate:   # 如果不同区域邻居大于0且随机数小于0.1
                return random.choice(different_zone_neighbors)                  # 随机返回一个不同区域邻居
            else:   
                return None
    #  1.interact方法是用来判断用户是否能够接收到新的合同,相同区域的用户沟通成功的概率为0.9,不同区域的用户沟通成功的概率为0.1
    #  2.在确认双方能够进行信息交流之后，接下来要去进行判断用户的忠诚度，如果用户的忠诚度高于阈值，则用户不会接受任何的变化，反之如果用户的忠诚度低于阈值，则用户会接受新的合同

    def determine_fedality(self): # 确定用户的忠诚度
        # 用户的忠诚度与其用电类型有关，用电量较大的用户，相对忠诚度会更低，因为会更倾向于使用更便宜的合同
        # 而用电量较小的用户，相对忠诚度会更高，因为会更倾向于使用更稳定的合同
        if self.type == 0:      #高电量用户
            fedality = random.uniform(0.8, 0.9)
        elif self.type == 1:    #中电量用户
            fedality = random.uniform(0.4, 0.6)
        elif self.type == 2:    #低电量用户 
            fedality = random.uniform(0.1, 0.2)
        return fedality
              
    # 该方法是用来判断self.contract和other_person.contract是否相同，如果相同则pass，如果不同，则需要调用用户效用模型来判断两个合同哪个更优
    def communicate_contract(self, other_person):
        if self.contract_number != other_person.contract_number:
            selfid = self.unique_id
            self_contract = self.contract_number
            neighbor_contract = other_person.contract_number
            optimal_contract, whetherchanged = FindOptimalContract_retailor(selfid,self_contract,neighbor_contract)
            if whetherchanged == 1:
                self.contract_number = optimal_contract
                print('-------------------------')
                print(f"Agent {other_person.unique_id} talked to Agent {self.unique_id} to changed contract number from {self.old_contract} to {self.contract_number}")
                print('-------------------------')
                self.old_contract = self.contract_number
            else:
                pass
        else:
            pass
        
    def get_zone(self):
        return self.type


class ContractModel(Model):
    def __init__(self, num_people, width, height):
        self.num_people = num_people
        self.width = width
        self.height = height
        self.space = ContinuousSpace(width, height, True)
        self.schedule = RandomActivation(self)

        for i in range(self.num_people):
            person = Person(i, self)
            self.schedule.add(person)
            x, y = random.uniform(0, width), random.uniform(0, height)
            self.space.place_agent(person, (x, y))

    def step(self):
        self.schedule.step()

    def display_state(self):
        for agent in self.schedule.agents:
            print(f"Agent {agent.unique_id} at position {agent.pos} has contract number {agent.contract_number}")

    # store the data of customer and contract
    def store_data(self):
        round_data = []
        for agent in self.schedule.agents:
            round_data.append([agent.unique_id, agent.contract_number, agent.type]) #round_data的shape为(430, 3),其中包括用户id，合同编号，用户类型
        return round_data



def main():
    # SetPrice()
    iteration_time = 6 # 定义迭代的次数
    pickle_regulator_retailor()

    # modify one contract at a time
    contract_num = 1

    # read the set price data automation.csv, each row is a different set of dynamic price
    automation_price = pd.read_csv('automation.csv')
    # transfer the data to numpy array 
    automation_price = np.array(automation_price) # shape is (lenth_of_data, 3)
    lenth_of_data = len(automation_price) 

    # create a list to store the specific contract profit in each set of the automation_price data
    specific_contract_profit = []
    # create a list to store the specific contract number in each set of the automation_price data
    specific_contract_number = []
        
    for j in range(len(automation_price)):
        # each time modify one contract according to the automation_price
        modified_contract_pricei = automation_price[j]
        
        modify_contract_retailor_automation(contract_num, modified_contract_pricei)
    
        model = ContractModel(num_people=numberofpeople, width=40, height=40)
        customer_info = []
        # images = [] #save the plot as a gif file, 针对于动态显示的部分
        InitialMarketShare = []
        contract_price = []
        profit_list = []
       
        
        
        for i in range(iteration_time):  # Change this number to run more or fewer steps
            print(f"Step {i + 1}:")
            # Run the model one step
            model.step() 
            model.display_state()
            # round_data is the data of customer and contract in each iteration
            round_data = model.store_data()      
            # print(np.array(round_data).shape)
            #need to store the initial contract market share to calculate the market share change
            if i == 0:     
                InitialMarketShare = round_data
            else:
                pass 
            
            round_profit = Profit_retailor(round_data)
            # print(round_profit)
            profit_list.append(round_profit)
            # print(f"profit_list is {profit_list}")
            
            # contract self-modification step,该部分处理的结果与合同的自我修订有关
            # MarketShareWarning(contract_number,round_data, InitialMarketShare) 
            # store the data of customer and contract in each iteration to the customer_info list
            customer_info.append(round_data)
            
            # 读取合同价格pickle数据，并将其转化为ndarray
            contract_price.append(Contract_dynamic_price_retailor())
            print("\n")

        # transform the customer_info list to a ndarray
        customer_info = np.array(customer_info)
        CustomerPriceDynamic_retailor(contract_price)
        
        # transform the profit_list to a ndarray
        profit_list = np.array(profit_list).T # profit_list's shape is (contract_number, iteration_time)
        
        # reduce the dimension of the profit_list, just left one contract profit, which is the specific contract profit that we want
        specific_contract_profit_info = profit_list[contract_num-1,:] # the shape is (1, iteration_time), the first row is the specific contract profit,
                                                                        # and the column is under the set dynamic price, during the iteration time,the profit of the specific contract
        # print(specific_contract_profit_info)
        # print(specific_contract_profit_info.shape)
        
        # add the specific_contract_profit_info into the specific_contract_profit list 
        specific_contract_profit.append(specific_contract_profit_info) # after the iteration of the automation_price, the shape of the specific_contract_profit is (lenth_of_data, iteration_time),
                                                                        # which contains all the profit of the specific contract under the different dynamic price
        
        # print(customer_info)
        contract_market_number, contract_market_share, contractid_usertype_number, contractid_usertype_share = MultiagentDataProcess_retailor(contract_number, customer_info, numberofcluster=3)

        # in here, the contract_market_number is the ndarray which contains all the contracts market number in each iteration
        # find the specific contract market number in each iteration
        specific_contract_number_info = contract_market_number[contract_num-1,:] # the shape is (1, iteration_time), the first row is the specific contract market number
        specific_contract_number.append(specific_contract_number_info) # after the iteration of the automation_price, the shape of the specific_contract_number is (lenth_of_data, iteration_time),
        
    # transform the contract_price list to a ndarray
    contract_price = np.array(contract_price)
    
    # transform the specific_contract_profit list to a ndarray
    specific_contract_profit = np.array(specific_contract_profit) # the shape is (lenth_of_data, iteration_time)
    # print(specific_contract_profit.shape)
    # print(specific_contract_profit)
    # transform specific_contract_profit to a dataframe
    
    # concate the automation_price and the specific_contract_profit
    specific_contract_profit = np.concatenate((automation_price, specific_contract_profit), axis=1)
    # transform specific_contract_profit to a dataframe
    specific_contract_profit = pd.DataFrame(specific_contract_profit)
    # # drop the first column of the specific_contract_profit dataframe
    # specific_contract_profit = specific_contract_profit.drop(specific_contract_profit.columns[0], axis=1)
    # save the specific_contract_profit dataframe to a csv file
    specific_contract_profit.to_csv('specific_contract_profit.csv')
    
    # transform the specific_contract_number list to a ndarray
    specific_contract_number = np.array(specific_contract_number) # the shape is (lenth_of_data, iteration_time)
    # concate the automation_price and the specific_contract_number
    specific_contract_number = np.concatenate((automation_price, specific_contract_number), axis=1)
    # transform specific_contract_number to a dataframe
    specific_contract_number = pd.DataFrame(specific_contract_number)
    # # drop the first column of the specific_contract_number dataframe
    # specific_contract_number = specific_contract_number.drop(specific_contract_number.columns[0], axis=1)
    # save the specific_contract_number dataframe to a csv file
    specific_contract_number.to_csv('specific_contract_number.csv')

    
if __name__ == "__main__":
    customer_array = CustomerConsumption('customer_consumption_total.csv', numberofcluster=3) # 调用CustomerConsumption函数，获取用户的用电数据
    customer_info_array = LastIterationContract('customer_id_contract_data.csv')
    numberofpeople = len(customer_array) # 获取用户的数量 
    contract_number = 5 # 定义合同的数量         
    main()
