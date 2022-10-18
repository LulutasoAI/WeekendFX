import pandas_datareader as pdr
import pandas as pd
from datetime import date,timedelta,datetime
import time
from matplotlib import pyplot as plt
from typing import List, Dict
import os 

class WeekendFX():
    def __init__(self) -> None:
        pass 

    def get_current_price(self, symbol:str, logout:bool = True):
        #currency_candidates = "BTC-USD","BTC-JPY"
        today = date.today()
        yesterday = today - timedelta(days=1)
        price_data = pdr.get_data_yahoo([symbol], 
                          start=yesterday, 
                          end=today)['Close']
        price = round(price_data[symbol][-1],3)
        if logout:
            print("The latest {} price : {}".format(symbol, price))
            #print(price_data)
        return price
    
    def to_csv(self,to_chart:Dict[str,List[float]], title:str):
        df = pd.DataFrame(to_chart)
        datetime_string = datetime.now().strftime('%Y_%m_%d_%H%M%S')
        df.to_csv(title+"_"+datetime_string+".csv")
        
    
if __name__ == ("__main__"):
    weekendFX = WeekendFX()
    time_count = 0
    
    to_chart = {"prices" :[]}
    while True:
        BTC_USD_price = weekendFX.get_current_price("BTC-USD",True)
        BTC_JPY_price = weekendFX.get_current_price("BTC-JPY",True)
        USD_JPY_rate = round((BTC_JPY_price/BTC_USD_price),3)
        print(USD_JPY_rate)
        to_chart["prices"].append(USD_JPY_rate)
        time_count += 1 
        if time_count%60 == 0:
            weekendFX.to_csv(to_chart,"USDJPY")
        time.sleep(10)
