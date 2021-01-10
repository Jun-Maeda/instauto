import sqlite3
import os
from dotenv import load_dotenv
# .envファイルの内容を読み込みます
load_dotenv()


dbname = os.environ["DBNAME"]
conn = sqlite3.connect(dbname)
cur = conn.cursor()

# instagramContentsというtableを作成してみる
cur.execute(
    'CREATE TABLE instagramContents(id INTEGER PRIMARY KEY AUTOINCREMENT, post_content STRING);')
conn.commit()
conn.close()
