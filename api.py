from urllib import request
from flask import Flask, render_template, request, url_for
import subprocess
from form import Choose
from tkinter import filedialog, Tk
from insert_data import insert_data
from select_data import select_data

app = Flask(__name__)
app.config['SECRET_KEY'] = '5eb8738961b3e9b9d1f636d240b6ca4a'


@app.route('/', methods=['GET', 'POST'])
def index():
    form = Choose()
    if request.method == 'POST':
        if 'scan_file' in request.form:
            root = Tk()
            root.withdraw()
            file_path = filedialog.askopenfilename(title='Select a file', parent=root)
            if file_path:
                dir1 = 'clamscan ' + file_path
                process = subprocess.Popen(dir1,
                                           stdout=subprocess.PIPE,
                                           stderr=subprocess.PIPE,
                                           shell=True)
                stdout, stderr = process.communicate()
                out = stdout.decode('utf-8')
                insert_data(file_path, out)
                return render_template('index.html', title="Scan", form=form, data=out)
        elif 'scan_folder' in request.form:
            root = Tk()
            root.withdraw()
            folder_path = filedialog.askdirectory(title='Select a folder', parent=root)
            if folder_path:
                dir2 = 'clamscan ' + folder_path
                process = subprocess.Popen(dir2,
                                           stdout=subprocess.PIPE,
                                           stderr=subprocess.PIPE,
                                           shell=True)
                stdout, stderr = process.communicate()
                out = stdout.decode('utf-8')
                insert_data(folder_path, out)
                return render_template('index.html', title="Scan", form=form, data=out)
        elif 'show_history' in request.form:
            data = select_data()
            return render_template('scan_history.html', title='Scan History', data=data)
    return render_template('index.html', title="Scan", form=form)


if __name__ == "__main__":
    app.run(debug=True)
