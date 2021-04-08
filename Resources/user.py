from flask_restful import Resource, reqparse
from Models.user import UserModel

atributtes = reqparse.RequestParser()
atributtes.add_argument("nome", type=str, required=True, help="User's name ")
atributtes.add_argument("sobrenome", type=str, required=True, help="User's last name")
atributtes.add_argument("email", type=str, required=True, help="User's email")
atributtes.add_argument("senha", type=str, required=True, help="User's password")
atributtes.add_argument("nascimento", type=str, required=True, help="User's birthday")
atributtes.add_argument("telefone", type=str, required=True, help="User's phone number")

login_atributtes = reqparse.RequestParser()
login_atributtes.add_argument("email", type=str, required=True, help="User's email")
login_atributtes.add_argument("senha", type=str, required=True, help="User's password")

class UserRegister(Resource):

	def post(self):
		args = atributtes.parse_args()
		user = UserModel(**args)
		user.save_user()
		return {"message": "User created successfully!"}, 201

class UserLogin(Resource):

	def post(self):
		args = login_atributtes.parse_args()

		result = UserModel.find_by_email(email=args['email'])
		if result:
			return {'message': 'user logged in!'}
		return {"message": "User not founded..."}, 404