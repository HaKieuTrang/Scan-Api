from urllib import request
from flask import Flask, render_template, request, url_for
import subprocess
from form import Choose
from tkinter import filedialog, Tk
from insert_data import insert_data
from select_data import select_data_scan, select_data_signatures
from get_files import list_file_hard_drive

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
                dir1 = 'clamscan --remove=yes ' + file_path
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
                dir2 = 'clamscan --remove=yes -r ' + folder_path
                process = subprocess.Popen(dir2,
                                           stdout=subprocess.PIPE,
                                           stderr=subprocess.PIPE,
                                           shell=True)
                stdout, stderr = process.communicate()
                out = stdout.decode('utf-8')
                insert_data(folder_path, out)
                return render_template('index.html', title="Scan", form=form, data=out)
        elif 'scan_hard_drive' in request.form:
            # list_files = list_file_hard_drive()
            # count_files = len(list_files)
            # for file in list_files:
            hard_drive_path = '/media'
            dir3 = 'clamscan --remove=yes -r ' + hard_drive_path
            process = subprocess.Popen(dir3,
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE,
                                       shell=True)
            stdout, stderr = process.communicate()
            out = stdout.decode('utf-8')
            insert_data(dir, out)
            return render_template('index.html', title="Scan", form=form, data=out)
        elif 'show_history' in request.form:
            data = select_data_scan()
            return render_template('scan_history.html', title='Scan History', data=data)
        elif 'update_signatures' in request.form:
            write_file = 'echo '
            signatures = select_data_signatures()
            content = '"'
            for row in signatures:
                content = content + row[1] + '\n'
            content = content.rstrip("\n")
            write_file = write_file + content + '"' + ' >> signatures.ndb'
            create_file = 'mkdir /home/hatrang/clamscan && cd /home/hatrang/clamscan && touch signatures.ndb && ' + write_file
            process = subprocess.Popen(create_file,
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE,
                                       shell=True)
            return render_template('index.html', title="Scan", form=form, data='update')
    return render_template('index.html', title="Scan", form=form)


if __name__ == "__main__":
    app.run(debug=True)
