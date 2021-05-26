from sql_alchemy import db

class UserModel(db.Model):
	__tablename__ = 'user'

	id = db.Column(db.Integer, primary_key=True)
	nome = db.Column(db.String(40), nullable=False)
	sobrenome = db.Column(db.String(120), nullable=False)
	email = db.Column(db.String(80), nullable=False)
	senha = db.Column(db.String(40), nullable=False)
	nascimento = db.Column(db.DateTime, nullable=False)
	telefone = db.Column(db.String(15), nullable=False)

	pets = db.relationship('PetModel', back_populates="user")

	def __init__(self, nome, sobrenome, email, senha, nascimento, telefone):
		self.nome = nome
		self.sobrenome = sobrenome
		self.email = email
		self.senha = senha #TODO: falta por hash
		self.nascimento = nascimento
		self.telefone = telefone

	def __repr__(self):
		return f"User(nome = {nome})"

	def json(self):
		data = {
		'id': self.id,
		'nome': self.nome,
		'sobrenome': self.sobrenome,
		'email': self.email,
		'nascimento': str(self.nascimento),
		'telefone': self.telefone
		}
		return data

	def save_user(self):
		db.session.add(self)
		db.session.commit()

	def delete_user(self):
		db.session.delete(self)
		db.session.commit()

	@classmethod
	def find_by_email(cls, email):
		user = cls.query.filter_by(email=email).first()
		if user:
			return user
		return None