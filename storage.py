import sqlite3
processed_list=[{"symbol":"BTC","Price":100000,"Timestamp":"2026-01-01 00:00:00","pct":10},{"symbol":"ETH","Price":20000,"Timestamp":"2026-01-01 00:00:00","pct":20}]

def init_db():
  conn = sqlite3.connect("crypto.db")  # creates file if doesn't exist
  cur=conn.cursor() #cursor to execute commands

  #create table if not exists
  cur.execute("CREATE TABLE IF NOT EXISTS cryptoPrices(symbol,price,timestamp,pct)")
  conn.commit()
  conn.close()
  return None

def store_data(processed_list):
  conn = sqlite3.connect("crypto.db")  # creates file if doesn't exist
  cur=conn.cursor() #cursor to execute commands

  for item in processed_list:
    cur.execute("INSERT INTO cryptoPrices VALUES(?,?,?,?)",(item["symbol"],item["Price"],item["Timestamp"],item["pct"]))
  cur.execute("SELECT * FROM cryptoPrices")
  res=cur.fetchall()
  print(res)
  conn.commit()
  conn.close()

  return None


if __name__=="__main__":
  init_db()
  store_data(processed_list)

