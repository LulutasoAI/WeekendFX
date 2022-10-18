from DollarYen import WeekendFX
import time 

class DailyFX(WeekendFX):
    def __init__(self) -> None:
        super().__init__()
        self.symbol = "USDJPY=X"

    def get_USDJPY_price(self):
        USDJPY_price = self.get_current_price(self.symbol, True)
        return round(USDJPY_price,3)
        
    def main(self):
        self.buy_or_sell = int(input("buy? or sell? 0,or 1"))
        self.position_price = float(input("at where did you take position? in float"))
        self.position_amount = int(input("How much position did you take? amount = n*10000"))
        while True:
            USDJPY_price = self.get_USDJPY_price()
            print(USDJPY_price)
            if not self.buy_or_sell: 
                diff = self.position_price - USDJPY_price
            else:
                diff = USDJPY_price - self.position_price
            profit = diff * self.position_amount*10000
            print("profit now : {}".format(round(profit,0)))
            time.sleep(10)


if __name__ == ("__main__"):
    daily_FX = DailyFX()
    daily_FX.main()
