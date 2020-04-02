import mysql.connector
from mysql.connector import Error


def select_data():
    connection = mysql.connector.connect(host='localhost',
                                         database='clamav_scan',
                                         user='admin',
                                         password='Trang1234#')

    mysql_select_query = """SELECT * FROM scan_info"""
    cursor = connection.cursor()
    cursor.execute(mysql_select_query)
    data = cursor.fetchall()
    connection.commit()
    cursor.close()
    return data
