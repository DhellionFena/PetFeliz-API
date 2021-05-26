import requests

BASE = 'http://127.0.0.1:5000'

user_cadastro = {
	"nome": "Antônio César",
	"sobrenome": "Nunes de Azevedo Filho",
	"email": "antonio@hotmail.com",
	"senha": "123456",
	"nascimento": "2001-04-08",
	"telefone": '988221235'
}

user_login = {
	"email": "antonio@hotmail.com",
	"senha": "123456",
}

create_pet = {
	"nome": "Melissa",
	"idade": 10,
	"imagem": "",
	"motivoAdocao": "Nao eh pra adotar",
	"historico": "Divindade de oberon",
	"user_id": 1
}


response = requests.post(BASE + '/pets', create_pet)
print(response)
