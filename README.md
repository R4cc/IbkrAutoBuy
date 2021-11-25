# IbkrAutoBuy
## Summary:
This is a python script that automatically buys a given stock and sends a mail via SMTP

## Initial Configuration
You first ***have*** to configure the following variables:
### Start.py
- "Ticker" - What stock to buy
- "Exchange" - What exchange to use (SMART for aut)
- "Currency" - The currency the stock is in (At the given exchange)

### SendMail.py
- "sender_email" - SMTP mail to use
- "reviever_email" - Email reciever
- "port" - For SSL 
- "password" - The SMTP Mail Password
### Order.py
Inside of the ib.Connect() You have to configure 3 variables:
- IP of the IB Gateway or TWS (API Interface)
- The Port that is configured in the IB Gateway of TWS API Settings
- Client ID(leave at 1 if you don't use multiuser)
Order Specifications:
- "quantity" - The quantity of the order
- "orderType" - type of the order (BUY or SEL) 

After you have correctly configured these variables you should be able to buy the specified stock by executing the "Start.py" file. 

