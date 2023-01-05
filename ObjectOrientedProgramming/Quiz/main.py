from extra import enter as input, typing as print
import requests

key = "VcKaIsdASSM8NtyyaPgEqzioQmt9gYJQkGViQsLt"

def getQuestions():
	url = "https://quizapi.io/api/v1/questions"
	data = requests.get(url, {
		"apiKey": key,
		"limit": 10
	})
	return data.json()

datas = getQuestions()
print(datas, 1)