from flask import Flask
from flask_restful import Api
from sql_alchemy import db
from Resources.cats import Cats, Cat

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'

@app.before_first_request
def cria_banco():
    db.create_all()

api.add_resource(Cats, "/cats")
api.add_resource(Cat, "/cats/<int:cat_id>")

if __name__ == "__main__":
	db.init_app(app)
	app.run(debug=True)