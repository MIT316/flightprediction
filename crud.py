import mysql.connector

try:
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='9033170512'
    )
    mycursor = conn.cursor()
    print('Connection established')
except mysql.connector.Error as err:
    print(f'Connection error: {err}')
