from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from fontTools import unicode
from category import preCategory,tbCategory,tbfcCategory,baseCategory,basefcCategory,ftCategory

app = Flask(__name__)
api = Api(app)

# Todo
# shows a single todo item and lets you delete a todo item
class category(Resource):
    def get(self,name):
        prename = preCategory(name)
        if prename  == "":
            tbname = tbCategory(name)
            if tbname  == "":
                tbfcname = tbfcCategory(name)
                if tbfcname == "":
                    basename = baseCategory(name)
                    if basename == "":
                        return  ftCategory(name)
                    else:
                        return basename
                else:
                    return tbfcname
            else:
                return tbname
        else:
            return prename

##
## Actually setup the Api resource routing here
##
api.add_resource(category, '/category/<name>')


if __name__ == '__main__':
    app.run(debug=True)