import configparser 
from pprint import pprint
from binance.client import Client

# methods = {
#   'futures_allOrders' : ['get','v1', 'allOrders']
# }

# def future_request(client, method):
#   print(methods[method][2])
#   return client._request_futures_api(methods[method][0], methods[method][2])

# def _request_futures_api(self, method, path, signed=False, **kwargs):
#     uri = self._create_futures_api_uri(path)

#     return self._request(method, uri, signed, True, **kwargs)

#MY HELPERS
def get_all_open_orders(client, typ,**kwargs):
  if typ == 'futures':
    return client.futures_account_trades()

  return client._get('openOrders', True, data=kwargs)

# GET KEYs
configParser = configparser.RawConfigParser()   
configFilePath = r'config.cfg'
configParser.read(configFilePath)

API_KEY = configParser.get('KEYS', 'API_KEY')
API_SECRET = configParser.get('KEYS', 'API_SECRET')

print('API_KEY : ' + API_KEY)
print('SECRET : ' + API_SECRET)

# GET CLIENT
client = Client(API_KEY, API_SECRET)

# get market depth
# futures_account_balance = client.futures_account_balance()
# pprint(futures_account_balance)
futures_account = client.futures_account()
pprint(futures_account)
# print(len(future_orders), ' trades')




