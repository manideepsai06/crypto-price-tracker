import requests 
from datetime import datetime

def fetch_data():
  url = "https://api.coinpaprika.com/v1/tickers"
  try:
    out=requests.get(url)
    response = out.json()
  except Exception as e:
    print(f"Something went wrong: {e}")
    print(f"Status Code: {out.status_code}")
    return None

  dictonary=dict()

  lis=["BTC", "ETH", "BNB", "SOL", "XRP"]#list of coins which we need data for 
  Todays_dt=str(datetime.now())#extracting exact timestamp when the data is fetched
  
  #this loop checks whether listed coin is there or not from api response
  #if its available then key will be created with symbol and another dictonary with all the details will be loaded
  #example : 'BTC': {'symbol': 'BTC', 'Price': 65801.69323884316, 'Timestamp': '2026-06-17 09:38:40.828977'}
  for i in range(len(response)):
    if(response[i]["symbol"] in lis):
      first_Dict=dict()
      first_Dict["symbol"]=response[i]["symbol"]
      first_Dict["Price"]=round(response[i]["quotes"]["USD"]["price"],3)
      first_Dict["Timestamp"]=Todays_dt
      dictonary[response[i]["symbol"]]=first_Dict
  return dictonary

def main():
  print(fetch_data())

if __name__ == "__main__":
  # This code will NO LONGER run when imported into your second file
  main()