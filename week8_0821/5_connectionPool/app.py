import mysql.connector
import mysql.connector.pooling

# Configuration for MySQL database
DB_CONFIG = {
    'user': "root",
    'password': 'admin',
    'host': '127.0.0.1',
    'database': 'website',
}

conpool = mysql.connector.pooling.MySQLConnectionPool(pool_name="mypool",
                                                      pool_size = 3,
                                                      **DB_CONFIG)

def connect_to_db():
    try:
        con = conpool.get_connection();
        cursor = con.cursor(dictionary=True)
        query = "SELECT * FROM member"
        cursor.execute(query)
        result = cursor.fetchall()
        print(result)
        print("Retrived successfully!")
        con.close()
    except Exception as e:
        print(e)

connect_to_db()