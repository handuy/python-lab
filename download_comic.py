import requests, bs4

page = 10
while page >= 0:
    comicLink = ""
    if page == 0:
        comicLink = "https://xkcd.com/"
    else:
        comicLink = "https://xkcd.com/{pageNum}".format(pageNum=page)

    res = requests.get(comicLink, verify=False)
    res.raise_for_status()

    newSoup = bs4.BeautifulSoup(res.text, "html.parser")
    img = newSoup.find_all("img")
    # elems = newSoup.select('[ved]')
    comicSrc = "imgs.xkcd.com/comics"

    for i in img:
        fullLink = i.get("src")
        if comicSrc in fullLink:
            subStrIndex = fullLink.find(comicSrc)
            downloadLink = "https://{link}".format(link=fullLink[subStrIndex:])
            imgDownload = requests.get( downloadLink, verify=False )
            fileName = fullLink.split("/")[-1]
            comicFile = open(fileName, "wb")
            for chunk in imgDownload.iter_content(100000):
                comicFile.write(chunk)

            comicFile.close()
    
    page = page - 1


