import mysql.connector

connection = mysql.connector.connect(host='localhost',
                                     database='clamav_scan',
                                     user='admin',
                                     password='Trang1234#')


def select_data_scan():
    mysql_select_query = """SELECT * FROM scan_info"""
    cursor = connection.cursor()
    cursor.execute(mysql_select_query)
    data = cursor.fetchall()
    connection.commit()
    cursor.close()
    return data


def select_data_signatures():
    mysql_select_query = """SELECT * FROM clamscan_signatures"""
    cursor = connection.cursor()
    cursor.execute(mysql_select_query)
    data = cursor.fetchall()
    connection.commit()
    cursor.close()
    return data
