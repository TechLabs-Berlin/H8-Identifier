from flask import Flask, render_template, request
from backend import generate_output

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        vid_url = request.form["vid_url"]
        output = generate_output(vid_url)
        return render_template('index.html', output=output)
    else:
        return render_template('index.html')
