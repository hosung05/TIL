from iexfinance.stocks import Stock
import pprint

pp = pprint.PrettyPrinter()
TOKEN ='pk_935931b54f044ce386d87df582ff6da8'

aapl = Stock('FB', token=TOKEN)
data = aapl.get_quote()
# pp.pprint(aapl.get_quote())
print(data['companyName'],data['latestPrice'])