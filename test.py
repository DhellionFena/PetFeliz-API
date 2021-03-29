import requests

BASE = 'http://127.0.0.1:5000/'

test = {
	"name": "Cake",
	"age": 8,
	"gender": "M"
}


#response = requests.post(BASE + 'cat/1', test)
response = requests.get(BASE + 'cats/3')
print(response.json())
