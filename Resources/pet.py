from flask_restful import Resource, reqparse
from Models.pet import PetModel

atributtes = reqparse.RequestParser()
atributtes.add_argument("name", type=str, required=True,help="Pet's name ")
atributtes.add_argument("age", type=int, required=True,help="Pet's age")
atributtes.add_argument("gender", type=str, required=True,help="Pet's gender")

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

	def get(self, pet_id):
		result = PetModel.find_by_id(id=pet_id)
		if result:
			return result.json()
		return {"message": "Cat not founded..."}, 404