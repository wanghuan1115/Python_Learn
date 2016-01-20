from app import app
import sqlite3

# 初始数据:
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)