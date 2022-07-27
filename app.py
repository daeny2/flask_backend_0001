from flask import Flask
from views.index import index_blueprint

app = Flask(__name__)

app.register_blueprint(index_blueprint)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)