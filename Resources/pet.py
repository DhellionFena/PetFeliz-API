from flask_restful import Resource, reqparse
from Models.pet import PetModel
from sqlalchemy import text
from sql_alchemy import db

atributtes = reqparse.RequestParser()
atributtes.add_argument("nome", type=str, required=True,help="Pet's name ")
atributtes.add_argument("idade", type=int, required=True,help="Pet's age")
atributtes.add_argument("imagem", type=str, required=True,help="Pet's image")
atributtes.add_argument("motivoAdocao", type=str,help="Pet's gender")
atributtes.add_argument("historico", type=str,help="Pet's history")
atributtes.add_argument("user_id", type=int, required=True,help="Pet's gender")

class Pets(Resource):

	#get all cats
	def get(self):
		result = [pet.json() for pet in PetModel.query.all()]
		return result

	def post(self):
		args = atributtes.parse_args()
		pet = PetModel(**args)
		pet.save_pet()
		return {"message": "Pet created successfully!"}, 201

class Pet(Resource):

	#retorna dados de 1 pet
	def get(self, pet_id):
		pet = PetModel.find_by_id(id=pet_id)

		query = f"SELECT * FROM user WHERE user.id = {pet.user_id}"
		sql = text(query)
		result = db.engine.execute(sql)
		for r in result:
			result_dict = dict(r.items())
		if result_dict:
			return {"pet": pet.json(), "owner": result_dict}
		return {"message": "Pet not founded..."}, 404


class UserPets(Resource):

	#retorna lista de pets de um usuario
	def get(self, user_id):
		query = f"SELECT * FROM pet WHERE pet.user_id = {user_id}"
		sql = text(query)
		result = db.engine.execute(sql)

		lista = list()
		for r in result:
			result_dict = dict(r.items())
			lista.append(result_dict.copy())
		if result_dict:
			return lista
		return {"message": "Pet not founded..."}, 404