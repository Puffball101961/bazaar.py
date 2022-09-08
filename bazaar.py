import requests

class Bazaar:
    def __init__(self):
        self.cachedData = []
    
    def updateValues(self):
        res = requests.get("https://api.hypixel.net/skyblock/bazaar").json()['products']
        self.cachedData = res 
    
    def parseItem(self, item):
        pass
    
    def buyOrders(self, item): # Buy Orders for 'item'
        pass

    def sellOrders(self, item): # Sell Orders for 'item'
        pass

    def price(self, item): # Buy/Sell Price of 'item'
        pass

    def volume(self, item): # Trading Volume of 'item'
        pass

    def orderCount(self, item): # Number of Buy/Sell orders open for 'item'
        pass

        

    
