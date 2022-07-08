import requests, bs4

res = requests.get("http://info.cern.ch/hypertext/WWW/TheProject.html")
res.raise_for_status()

newSoup = bs4.BeautifulSoup(res.text, "html.parser")
elems = newSoup.select("a")
print("type: ", type(elems))
print(len(elems))

for i in elems:
    print(i)