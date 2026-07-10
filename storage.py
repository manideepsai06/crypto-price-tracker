import sqlite3

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
  conn.commit()
  conn.close()

  return None


if __name__=="__main__":
  init_db()
  store_data(processed_list)

