import SendMail as mail
import Order as order

Ticker = 'AAPL' # Stock thicker, in this case Apple 
Exchange = 'SMART' # ExchangeId. Use SMART to automatically pick the best
Currency = 'EUR' # Currency you want to buy the stock in
trade = order.SendOrder(Ticker, Exchange, Currency)

mail.SendMail(Ticker, trade)







