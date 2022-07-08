import requests

res = requests.get("http://info.cern.ch/hypertext/WWW/TheProject.html")
res.raise_for_status()

htmlFile = open("download.html", "wb")

for chunk in res.iter_content(100000):
    htmlFile.write(chunk)

htmlFile.close()