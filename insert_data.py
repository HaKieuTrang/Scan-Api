import mysql.connector
import datetime


def insert_data(file_path, out):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='clamav_scan',
                                             user='admin',
                                             password='Trang1234#')
        time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        mysql_insert_query = """INSERT INTO scan_info (path, time, result) 
                              VALUES (%s, %s, %s)"""
        cursor = connection.cursor()
        cursor.execute(mysql_insert_query, (file_path, time, out))
        connection.commit()
        cursor.close()

    except mysql.connector.Error as error:
        print("Failed to insert record into Scan Info table {}".format(error))
    finally:
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed")
