"""
Command Pattern
"""

# Imports

from abc import ABCMeta, abstractmethod


# Class

class Order(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass

class BuyStockOrder(Order):
    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.buy()

class SellStockOrder(Order):
    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.sell()

class StockTrade:
    def buy(self):
        print("You will buy stocks")

    def sell(self):
        print("You will sell stocks")

class Agent:
    def __init__(self):
        self.__order_queue = []

    def place_order(self, order):
        self.__order_queue.append(order)
        order.execute()


# Main

if __name__ == "__main__":
    # Client
    stock = StockTrade()
    buy_stock = BuyStockOrder(stock)
    sell_stock = SellStockOrder(stock)

    # Agent
    agent = Agent()
    agent.place_order(buy_stock)
    agent.place_order(sell_stock)
