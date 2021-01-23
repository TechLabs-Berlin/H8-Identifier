from flask import Flask, request
from flask_restful import Resource, Api\

app = Flask(__name__)
api = Api(app)

class Classifier(Resource):
    def get(self):
        return {'about': 'string'}

    def post(self):
        some_json = request.get_json()
        return {'you sent': some_json}, 201

api.add_resource(Classifier, '/')

if __name__ == '__main__':
    app.run(debug=True)

