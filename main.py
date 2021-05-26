from flask import Flask
from flask_restful import Api
from sql_alchemy import db
from Resources.user import UserRegister, UserLogin, Users
from Resources.pet import Pets, Pet, UserPets

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'

@app.before_first_request
def cria_banco():
    db.create_all()

api.add_resource(Pets, "/pets")
api.add_resource(UserPets, "/pets/<int:user_id>")
api.add_resource(Pet, "/pet/<int:pet_id>")

api.add_resource(UserRegister, "/cadastro")
api.add_resource(UserLogin, "/login")
api.add_resource(Users, "/users")


db.init_app(app)
if __name__ == "__main__":
	app.run(debug=True)