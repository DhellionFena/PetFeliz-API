from sql_alchemy import db

class CatModel(db.Model):
	__tablename__ = 'cats'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(40), nullable=False)
	age = db.Column(db.Integer, nullable=False)
	gender = db.Column(db.Enum("M", "F"), nullable=False)

	def __init__(self, name, age, gender):
		self.name = name
		self.age = age
		self.gender = gender

	def __repr__(self):
		return f"Cat(name = {name}, age = {age}, gender = {gender})"

	def json(self):
		data = {
		'id': self.id,
		'name': self.name,
		'age': self.age,
		'gender': self.gender
		}
		return data

	def save_cat(self):
		db.session.add(self)
		db.session.commit()

	def delete_cat(self):
		db.session.delete(self)
		db.session.commit()

	@classmethod
	def find_by_id(cls, id):
		cat = cls.query.filter_by(id=id).first()
		if cat:
			return cat
		return None