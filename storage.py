from transform import transform_data
import sqlite3
conn = sqlite3.connect("crypto.db")  # creates file if doesn't exist
cur=conn.cursor()

def init_db():
  n=transform_data()
  cur.execute("CREATE TABLE IF NOT EXISTS cryptoPrices(symbol,price,timestamp,pct)")
  data=(n[0]["symbol"],n[0]["Price"],n[0]["Timestamp"],n[0]["pct"])
  cur.execute("INSERT INTO cryptoPrices VALUES(?,?,?,?)",data)
  conn.commit()
  cur.execute("SELECT * FROM cryptoPrices")
  res=cur.fetchall()
  conn.close()
  return res
if __name__=="__main__":
  print(init_db())