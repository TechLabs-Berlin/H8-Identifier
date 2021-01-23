from flask import Flask, render_template, request, redirect
from backend import generate_output, get_id_from_url

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        vid_url = request.form["vid_url"]
        id = get_id_from_url(vid_url)
        return redirect(f'/result/{id}')
    else:
        return render_template('/index.html')


@app.route('/result/<id>')
def result(id):
    result = generate_output(id)
    return render_template('result.html', output=result)

@app.error('/error')
def error():
    render_template('error.html')
