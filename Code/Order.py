import ib_insync as sync

def SendOrder(Ticker, Exchange, Currency):
    
    ib = sync.IB()
    ib.connect(
        '127.0.0.1', # IP of IB Gateway or TWS (API Interface)
        7496, # Port that is specified in IB Gateway or TWS settings
        clientId=1 # ID of User (leave at 1 if you don't use multiaccount)
        )
    quantity = 1 # Quantity of the given stock to buy
    stock = sync.Stock(Ticker, Exchange, Currency)
    orderType = 'BUY' # Buy or Sell

    order = sync.order.MarketOrder('BUY', Quantity) # This executes a Market order 
                                                    # for limit order look in the official documentation for the lib
    
    ib.placeOrder(stock, order) # Execurte order 
    return trade
