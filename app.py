from flask import Flask
from views.index import index_blueprint
#from views.todo import todo_blueprint

app = Flask(__name__)


app.register_blueprint(index_blueprint)
#app.register_blueprint(todo_blueprint)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)






"""
from flask import Flask
from flask_restx import Resource, Api
from todo import Todo
#from views.index import index_blueprint

#application = Flask(__name__)
#application.register_blueprint(index_blueprint)



app = Flask(__name__)
api = Api(app,
    version='0.1',
    title="cf's API Server",
    description="cf's Todo API Server!",
    terms_url="/",
    contact="daeny2@clouflake.com",
    license="MIT")

api.add_namespace(Todo, '/todos')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
"""