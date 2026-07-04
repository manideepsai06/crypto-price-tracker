from fetch import fetch_data

previous_price=dict()

def transform_data():
  #initiated list 
  processed_list = []
  
  #stored fetched data
  raw_data=fetch_data()
  
  #this function calculates the price change by using previously pulled price of coins
  def calculate_pct(coin):
    if coin in previous_price:
      current = raw_data[coin]['Price']
      previous = previous_price[coin]['Price']
      pct=((current-previous)/previous)*100
    else:
      pct=0
    previous_price[coin]=raw_data[coin]
    return pct
  
  #this loop adds all the values of fetched data dictonary into a list
  for i in raw_data:
    raw_data[i]["pct"]=calculate_pct(i)
    processed_list.append(raw_data[i])
  return processed_list

if __name__=="__main__":
  n=transform_data()
  print(n)

  


  


