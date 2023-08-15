import mysql.connector as mydb

# Configuration for MySQL database
DB_CONFIG = {
    'user': "root",
    'password': 'admin',
    'host': '127.0.0.1',
    'database': 'website',
}

def check_username(username):
    con = mydb.connect(**DB_CONFIG)
    query = "SELECT * FROM member WHERE username=%s"
    cursor = con.cursor()
    cursor.execute(query,(username,))
    data = cursor.fetchall()
    cursor.close()
    con.close()
    return data

def create_member(name, username, password):
    try:
        con = mydb.connect(**DB_CONFIG)
        query = "INSERT INTO member(name, username, password) VALUES(%s, %s, %s)"
        cursor = con.cursor()
        cursor.execute(query,(name, username, password))
        con.commit()
        cursor.close()
        con.close()
        return True
    except mydb.IntegrityError as e:
        print(e)
        return False
        

def get_user_by_credentials(username, password):
    try:
        con = mydb.connect(**DB_CONFIG)
        query = "SELECT * FROM member WHERE username = %s and password = %s"
        cursor = con.cursor(dictionary = True)
        cursor.execute(query,(username,password))
        data = cursor.fetchone()
        cursor.close()
        con.close()
        return data
    except mydb.IntegrityError as e:
        print(e)
        return False
         

def get_messages():
    try:
        con = mydb.connect(**DB_CONFIG)
        query = "SELECT message.id, message.member_id, member.name, message.content FROM message LEFT JOIN member ON member.id = message.member_id"
        cursor = con.cursor(dictionary = True)
        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()
        con.close() 
        return data
    except mydb.Error as e:
        print(e)
        return False
        

def create_message(member_id, content):
    try:
        con = mydb.connect(**DB_CONFIG)
        query = "INSERT INTO message(member_id,content) VALUES(%s, %s)"
        cursor = con.cursor()
        cursor.execute(query,(member_id, content))
        con.commit()
        cursor.close()
        con.close()
        return True
    except mydb.IntegrityError as e:
        print(e)
        return False
        

def delete_message(message_id):
    con = mydb.connect(**DB_CONFIG)
    query = "DELETE FROM message WHERE id=%s"
    cursor = con.cursor(dictionary = True)
    cursor.execute(query,(message_id,))
    con.commit()
    cursor.close()
    con.close()

def get_user_by_username(username):
    try:
        con = mydb.connect(**DB_CONFIG)
        query = "SELECT id, name, username FROM member WHERE username = %s"
        cursor = con.cursor(dictionary = True)
        cursor.execute(query,(username,))
        data = cursor.fetchone()
        cursor.close()
        con.close()
        return data
    except mydb.Error as e:
        print(e)
        return None

def update_user_name(new_name,user_id):
    try:
        con = mydb.connect(**DB_CONFIG)
        query = "UPDATE member SET name = %s WHERE id = %s"
        cursor = con.cursor(dictionary = True)
        cursor.execute(query, (new_name, user_id))
        con.commit()
        cursor.close()
        con.close()
        return True
    except mydb.IntegrityError as e:
        print(e)
        return False