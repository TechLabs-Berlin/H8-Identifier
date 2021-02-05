import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect
from .pipeline import generate_output
from .yt_request import get_id_from_url, get_title_and_description


def create_app(test_config=None):

    load_dotenv()
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

        title = result["title"]
        description = result["description"][0:200]
        chanel_title = result["chanel_title"]
        number_of_comments = result["number_of_comments"]
        percent_hate = result["percent_hate"]
        views = result["views"]
        shared = result["shared"]
        comments = result["comments"]

        comments_per_view = round((number_of_comments/views) * 100, 1)

        return render_template('result.html',
                               id=id,
                               title=title,
                               description=description,
                               chanel_title=chanel_title,
                               number_of_comments=number_of_comments,
                               percent_hate=percent_hate,
                               views=views,
                               shared=shared,
                               comments=comments,
                               comments_per_view=comments_per_view)

    @app.route('/error')
    def error():
        return render_template('error.html')

    @app.route('/about')
    def about():
        return render_template('about.html')

    return app
