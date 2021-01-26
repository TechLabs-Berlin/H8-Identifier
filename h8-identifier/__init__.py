import os
from flask import Flask, render_template, request, redirect
from .pipeline import generate_output
from .helper import get_id_from_url, get_title_and_description


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

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
