from bs4 import BeautifulSoup
import requests
import json

def search(title):
	res = requests.get(f"https://www.ultimate-guitar.com/search.php?search_type=title&value={title}").text
	bs = BeautifulSoup(res, "lxml")
	div = bs.find("div", class_="js-store")["data-content"]
	_json = json.loads(div)
	results = _json["store"]["page"]["data"]["results"]
	i = 0
	while results[i].get("id") is None:
		i += 1
	return results[i]

def chords(link):
	res = requests.get(link).text
	bs = BeautifulSoup(res, "lxml")
	div = bs.find("div", class_="js-store")["data-content"]
	json_ = json.loads(div)
	data = json_["store"]["page"]["data"]["tab_view"]["wiki_tab"]["content"]
	p = data.replace("[ch]", "").replace("[/ch]", "").replace("[tab]", "").replace("[/tab]", "")
	return p

def info(title):
	data = search(title)
	chrds = chords(data["tab_url"])
	result = {
		"title": data["song_name"],
		"singer": data["artist_name"],
		"chords": chrds
	}
	return result

title = input("Enter a song title: ")
print(info(title))