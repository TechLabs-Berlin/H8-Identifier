from flask import Flask, render_template, request, redirect
""" from .backend import get_id_from_url, get_vid_data, generate_output, get_title_and_description """

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        vid_url = request.form["vid_url"]
        id = get_id_from_url(vid_url)

        if id == -1:
            return redirect('/error')
        else:
            return redirect(f'/result/{id}')
    else:
        return render_template('/index.html')


@app.route('/result/<id>')
def result(id):
    result = generate_output(id)
    title, description = get_title_and_description(id)
    return render_template('result.html', id=id, title=title, description=description, result=result)


@app.route('/error')
def error():
    return render_template('error.html')
