from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
  vid_url = request.form["vid_url"]

  return render_template('index.html', url=vid_url)


