import requests
import json

class Bazaar:
    def __init__(self):
        self.cachedData = []
    
    def updateValues(self):
        res = requests.get("https://api.hypixel.net/skyblock/bazaar").json()['products']
        self.cachedData = res 
    
    def parseItem(self, item):
        items = open('items.json').read()
        items = json.loads(items)

        # Check if the item argument is a valid name in items.json
        for i in range(len(items['items'])):
            itm = items['items'][i]
            kl = list(itm.keys())
            vl = list(itm.values())
            try:
                pos = vl.index(item)
                pid = kl[pos]
                return pid
            except ValueError:
                pass

        # If the item is not an item name, check if it is a productID
        for i in range(len(items['items'])):
            itm = items['items'][i]
            kl = list(itm.keys())
            vl = list(itm.values())
            try:
                pos = kl.index(item)
                pid = kl[pos]
                return pid
            except ValueError:
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

        

print(Bazaar.parseItem(Bazaar(), 'RED_GIFT'))
