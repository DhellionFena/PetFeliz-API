from flask_restful import Resource, reqparse
from Models.cats import CatModel

atributtes = reqparse.RequestParser()
atributtes.add_argument("name", type=str, required=True,help="Cat's name ")
atributtes.add_argument("age", type=int, required=True,help="Cat's age")
atributtes.add_argument("gender", type=str, required=True,help="Cat's gender")

class Cats(Resource):

	#get all cats
	def get(self):
		result = [cat.json() for cat in CatModel.query.all()]
		return result

	def post(self):
		args = atributtes.parse_args()
		cat = CatModel(**args)
		cat.save_cat()
		return {"message": "Cat created successfully!"}, 201

class Cat(Resource):

	def get(self, cat_id):
		result = CatModel.find_by_id(id=cat_id)
		if result:
			return result.json()
		return {"message": "Cat not founded..."}, 404