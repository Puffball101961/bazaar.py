## bazaar.py
A Python Wrapper for the Hypixel Skyblock Bazaar

![Version](https://img.shields.io/pypi/v/bazaarpy)
![License](https://img.shields.io/pypi/l/bazaarpy)
[![Downloads](https://static.pepy.tech/personalized-badge/bazaarpy?period=total&units=international_system&left_color=grey&right_color=brightgreen&left_text=Downloads)](https://pepy.tech/project/bazaarpy)

## Important Note: 
This project has been put on an indefinite hold for lack of time and changes to the Hypixel API.

## Installation

    pip install bazaarpy

## Usage
This code will import the library, setup the Bazaar class and refresh the data from the API.

    from bazaarpy import bazaar as bz
    baz = bz.Bazaar()
    baz.updateValues() 
    
When querying an item, you must use its Product ID or similar name, as defined in items.json

**Available Functions:**
* updateValues() Fetches new data from the Hypixel API. Do not spam this function or Hypixel may blacklist your IP address.
* buyOrders(*item*) Gets the current Buy Orders for an item
* sellOrders(*item*) Gets the current Sell Orders for an item
* price(*item*) Gets the Buy and Sell price for an item
* volume(*item*) Gets the Buy and Sell volume for an item
* orderCount(*item*) Gets the number of Buy and Sell orders currently open for an item

## Examples
Fetch the Buy Price of a red gift and print it to the screen.

    from bazaarpy import bazaar as bz
    baz = bz.Bazaar()
    baz.updateValues()    
    buyPrice = baz.price("red gift")['buyPrice']   
    print(str(buyPrice))
