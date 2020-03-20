from flask import Flask, render_template, url_for
import subprocess
from form import UrlForm

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
        return out
    return render_template('index.html', title="Scan", form=form)

if __name__ == "__main__":
    app.run(debug=True)
