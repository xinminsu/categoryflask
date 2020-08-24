from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from fontTools import unicode
from category import tbCategory,ftCategory

app = Flask(__name__)
api = Api(app)

# Todo
# shows a single todo item and lets you delete a todo item
class category(Resource):
    def get(self,name):
        cname = tbCategory(name)
        if cname  == "":
            return ftCategory(name)
        else:
            return cname

##
## Actually setup the Api resource routing here
##
api.add_resource(category, '/category/<name>')


if __name__ == '__main__':
    app.run(debug=True)