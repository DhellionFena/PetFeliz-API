from flask import Flask
from flask_restful import Api
from sql_alchemy import db
from Resources.pet import Pets, Pet

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'

@app.before_first_request
def cria_banco():
    db.create_all()

api.add_resource(Pets, "/pets")
api.add_resource(Pet, "/pets/<int:cat_id>")

if __name__ == "__main__":
	db.init_app(app)
	app.run(debug=True)