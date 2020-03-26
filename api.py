from flask import Flask, render_template, url_for
import subprocess
from form import UrlForm
import mysql.connector
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '5eb8738961b3e9b9d1f636d240b6ca4a'


@app.route('/', methods=['GET', 'POST'])
def index():
    form = UrlForm()
    if form.validate_on_submit():
        dir = 'clamscan /' + form.url.data
        process = subprocess.Popen(dir,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                                   shell=True
                                   )
        stdout, stderr = process.communicate()
        out = stdout.decode('utf-8')
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='clamav_scan',
                                                 user='admin',
                                                 password='Trang1234#')
            time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            mySql_insert_query = """INSERT INTO scan_info (path, time, result) 
                                VALUES (%s, %s, %s)"""
            cursor = connection.cursor()
            cursor.execute(mySql_insert_query, (form.url.data, time, out))
            connection.commit()
            cursor.close()

        except mysql.connector.Error as error:
            message = "Failed to insert record into Scan Info table {}".format(error)
            return message
        finally:
            if (connection.is_connected()):
                connection.close()
        return out
    return render_template('index.html', title="Scan", form=form)


if __name__ == "__main__":
    app.run(debug=True)
