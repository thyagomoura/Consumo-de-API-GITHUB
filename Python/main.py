import requests
import json

class Repositorios():

	def request_api(self):
		resposta = requests.get(f'https://api.github.com/users/thyagomoura/repos')

		if resposta.status_code == 200:
			return resposta.json()
		else:
			return resposta.status_code

	def listagem(self):
		dados_api = self.request_api()
		if type(dados_api) is not int:
			for i in range(len(dados_api)):
				print(dados_api[i]['name'])
		else:
			print(dados_api)

reps = Repositorios()
reps.listagem()