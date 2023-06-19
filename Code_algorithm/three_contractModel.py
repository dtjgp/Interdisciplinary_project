import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from CustomerConsumption import CustomerConsumption
import pickle

class ElectricityContract:
    
    def __init__(self,price,fixed_price, contract_number):
        self.xlist = np.arange(0,48,1)
        self.contract_number = contract_number

        # 确定2022年的非周天的假期天数
        self.t_holiday = 15 # 按照F3电价
        # 确定2022年的周数
        self.weeknumber = 52
        self.t_sunday = self.weeknumber # 周天的天数=52
        # 计算2022年非假期的周六天数
        self.t_saturday = self.weeknumber - 1  # t_F2_saturday=51
        # 计算2022年周一到周五，非假期的天数
        self.t_workday = 365 - self.t_holiday - self.t_sunday - self.t_saturday  # t_F1=247

        # t_F1
        self.t_F1 = self.t_workday 
        # t_F2
        self.t_F2_workday =self.t_workday # t_F2_workday=247
        self.t_F2_saturday = self.t_saturday # t_F2_saturday=51
        # t_F3
        self.t_F3_workday = self.t_workday # t_F3_workday=247
        self.t_F3_saturday = self.t_saturday # t_F3_saturday=51
        self.t_F3_holiday = self.t_holiday # t_F3_holiday=9
        self.t_F3_sunday = self.t_sunday # t_F3_sunday=52


        # 对于分段电价，需要选取出不同的时段所占的时间
        # F1时段：
        self.timeslot_F1 = self.xlist[16:37] # 8:00-19:00 for weekday
        # F2时段：
        self.timeslot_F2_workday_morning = self.xlist[14:16] #7:00-8:00 for weekday morning
        self.timeslot_F2_workday_night = self.xlist[37:45] # 19:00-23:00 for weekday night
        self.timeslot_F2_saturday = self.xlist[14:45] # 7:00-23:00 for saturday
        # F3时段：
        self.timeslot_F3_morning = self.xlist[0:14] # 0:00-7:00 for everyday morning
        self.timeslot_F3_night = self.xlist[45:48] # 23:00-24:00 for everyday night

        # 电价
        self.F1_price = price[0]
        self.F2_price = price[1]
        self.F3_price = price[2]
        self.fixed_price = fixed_price


    def calculate_total_usage(self, customer_array):
        
        self.customer_array = customer_array
        
        consumption = np.zeros((len(self.customer_array), 1))
        for i in range(len(self.customer_array)):

            customer_i = self.customer_array[i]

            #计算周日和假期用电费用 (F3_price * customer_i一天用电量*假期和周日天数)
            t_F3 = self.t_F3_holiday + self.t_F3_sunday
            consumption_SundayHoliday = np.sum(customer_i) * t_F3 * self.F3_price

            #计算周六用电费用(（F2_price*customer_i在F2时段的用电量+F3_price*customer_i在F3时段的用电量）*周六天数)
            consumption_Saturday_F2 = np.sum(customer_i[self.timeslot_F2_saturday]) * self.F2_price
            consumption_Saturday_F3 = np.sum(customer_i[self.timeslot_F3_morning])+ np.sum(customer_i[self.timeslot_F3_night]) * self.F3_price
            consumption_Saturday = (consumption_Saturday_F2 + consumption_Saturday_F3) * self.t_F2_saturday

            #计算周一到周五用电费用(（F1_price*customer_i在F1时段的用电量+F2_price*customer_i在F2时段的用电量+F3_price*customer_i在F3时段的用电量）*周一到周五天数)
            consumption_workday_F1 = np.sum(customer_i[self.timeslot_F1]) * self.F1_price
            consumption_workday_F2 = np.sum(customer_i[self.timeslot_F2_workday_morning]) * self.F2_price + np.sum(customer_i[self.timeslot_F2_workday_night]) * self.F2_price
            consumption_workday_F3 = np.sum(customer_i[self.timeslot_F3_morning]) * self.F3_price + np.sum(customer_i[self.timeslot_F3_night]) * self.F3_price
            consumption_workday = (consumption_workday_F1 + consumption_workday_F2 + consumption_workday_F3) * self.t_F1

            #计算总用电费用
            consumption[i] = consumption_SundayHoliday + consumption_Saturday + consumption_workday + self.fixed_price
        self.consumption = np.around(consumption, decimals=2)
        return self.consumption
    
    # def set_contract_number(self, price):
    #     self.price = price

if __name__ == '__main__': 

    # contract1_price = [0.446, 0.446, 0.446]
    # contract2_price = [0.498824, 0.412275, 0.412275]
    # contract3_price = [0.4082, 0.3641, 0.2815]
    # contract4_price = [0.4209, 0.4209, 0.4209]
    # contract5_price = [0.3478, 0.3478, 0.3478]
    # contract_price_list = [contract1_price, contract2_price, contract3_price, contract4_price, contract5_price]
    # #change to np.array
    # contract_price_list = np.array(contract_price_list)
    # open the pickle file
    with open("contract_price.pickle", "rb") as p:
        contract_price_list = pickle.load(p)
        
    # print(contract_price_list)
    contract1_price = contract_price_list[0]
    contract2_price = contract_price_list[1]
    contract3_price = contract_price_list[2]
    contract4_price = contract_price_list[3]
    contract5_price = contract_price_list[4]
    

    ContractModel1 = ElectricityContract(contract1_price, 143.05, 1)
    ContractModel2 = ElectricityContract(contract2_price, 93.5, 2)
    ContractModel3 = ElectricityContract(contract3_price, 182.07, 3)
    ContractModel4 = ElectricityContract(contract4_price, 168.716, 4)
    ContractModel5 = ElectricityContract(contract5_price, 218.54, 5)
    
    # 读取数据
    customer_data = CustomerConsumption('customer_consumption_total.csv')
    customer_array = customer_data[:, :-1]
    
    contract1_consumption = ContractModel1.calculate_total_usage(customer_array)
    contract2_consumption = ContractModel2.calculate_total_usage(customer_array)
    contract3_consumption = ContractModel3.calculate_total_usage(customer_array)
    contract4_consumption = ContractModel4.calculate_total_usage(customer_array)
    contract5_consumption = ContractModel5.calculate_total_usage(customer_array)
    
    # 合并数据
    consumption = np.hstack((contract1_consumption, contract2_consumption, contract3_consumption, contract4_consumption, contract5_consumption))
    #转换成DataFrame
    consumption = pd.DataFrame(consumption, columns=['contract1_consumption', 'contract2_consumption', 'contract3_consumption', 'contract4_consumption', 'contract5_consumption'])
    #保存数据
    consumption.to_csv('contracts_fee_total_test_new.csv', index=False)
    
    
