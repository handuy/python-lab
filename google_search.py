import webbrowser, sys, requests, bs4, re

if len(sys.argv) == 1:
    print("need search keyword")
    sys.exit(1)

searchList = []

i = 1
while i < len(sys.argv):
  searchList.append(sys.argv[i])
  i = i + 1

searchStr = ' '.join(searchList)

googleLink = "https://google.com.vn/search?q={name}".format(name=searchStr)

webbrowser.open_new_tab(googleLink)

res = requests.get(googleLink, verify=False)
res.raise_for_status()

newSoup = bs4.BeautifulSoup(res.text, "html.parser")
elems = newSoup.find_all("a")
# elems = newSoup.select('[ved]')

for i in elems:
    print(i.encode("UTF-8"))
    # print(i.get("href"))


