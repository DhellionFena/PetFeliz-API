from sql_alchemy import db

class PetModel(db.Model):
	__tablename__ = 'pet'

	id = db.Column(db.Integer, primary_key=True)
	nome = db.Column(db.String(40), nullable=False)
	idade = db.Column(db.Integer, nullable=False)
	imagem = db.Column(db.String(80), nullable=False)
	motivoAdocao = db.Column(db.String(40), nullable=False)
	historico = db.Column(db.DateTime, nullable=False)

	user_id = Column(Integer, ForeignKey('user.id'))
	user = db.relationship('UserModel', back_populates="pets")

	def __init__(self, nome, idade, imagem, motivoAdocao, historico, user_id):
		self.nome = nome
		self.idade = idade
		self.imagem = imagem
		self.motivoAdocao = motivoAdocao
		self.historico = historico
		self.user_id = user_id

	def __repr__(self):
		return f"Pet(nome = {nome})"

	def json(self):
		data = {
		'id': self.id,
		'nome': self.nome,
		'idade': self.idade,
		'imagem': self.imagem,
		'motivoAdocao': self.motivoAdocao,
		'historico': self.historico,
		'user_id': self.user_id
		}
		return data

	def save_pet(self):
		db.session.add(self)
		db.session.commit()

	def delete_pet(self):
		db.session.delete(self)
		db.session.commit()

	@classmethod
	def find_by_id(cls, id):
		pet = cls.query.filter_by(id=id).first()
		if pet:
			return pet
		return None