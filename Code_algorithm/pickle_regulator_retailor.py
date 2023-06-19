# 该函数用来将regulator中的pickle文件保存下来，这样能够使得在运行retailor的时候，每次都可以调用相同的pickle文件，而不用每次都重新训练

import pickle
import pandas as pd
import numpy as np

def pickle_regulator_retailor():
    # 读取regulator中的pickle文件
    with open('contract_price.pickle', 'rb') as f:
        # load the model
        regulator_price = pickle.load(f)  
        
    # save to contract_price_retailor.pickle
    with open('contract_price_retailor.pickle', 'wb') as f:
        pickle.dump(regulator_price, f)
        
    # read the static_price.pickle
    with open('static_price.pickle', 'rb') as f:
        static_price = pickle.load(f)
        
    # save to static_price_retailor.pickle
    with open('static_price_retailor.pickle', 'wb') as f:
        pickle.dump(static_price, f)