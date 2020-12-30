from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        vid_url = request.form["vid_url"]
        return render_template('index.html', vid_url=vid_url)
    else:
        return render_template('index.html')
