import requests 
import time

def fetch_data():
  url = "https://api.coinpaprika.com/v1/tickers"
  try:
    response = requests.get(url).json()
  except Exception as e:
    print(f"Something went wrong: {e}")
    return None

  dictonary=dict()

  lis=["BTC", "ETH", "BNB", "SOL", "XRP"]

  for i in range(len(response)):
    if(response[i]["symbol"] in lis):
      print(response[i]["symbol"])
      dictonary[response[i]["symbol"]]=response[i]["quotes"]["USD"]["price"]
  return dictonary

print(fetch_data())