import requests

#getting coins data to get required data from them
url = "https://api.coinpaprika.com/v1/coins"
response = requests.get(url)
coins=response.json()

#symbols which we need to get id from coin data from api
symb=["BTC", "ETH", "BNB", "SOL", "XRP"] 

#getting required ids from cons data
ids=[]
for i in coins:
  if(i["symbol"] in symb):
    ids.append(i["id"])


#function to get coins data using coinpaprika api
def fetch1(coinname):
  url = "https://api.coinpaprika.com/v1/tickers/"+coinname
  resp=requests.get(url)
  if resp.status_code == 404:
    return None
  fin=resp.json()["quotes"]["USD"]["price"]
  print(f"the price of {coinname} is {fin:0.0f}")

for i in ids:
  fetch1(i)


  