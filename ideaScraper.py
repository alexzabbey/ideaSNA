#! python3

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
import pickle
import sqlite3


def getPage(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup


def getLinks(url, selector):
    linkList = []
    for l in getPage(url).select(selector):
        linkList.append(l.get('href')[27:-1])
    return linkList


def getIdeas():
    letterLinks = getLinks(alphabetAddress, "a.letter")
    print('got all links to letter pages')
    entryLinks = []
    for link in letterLinks:
        entryLinks.extend(getLinks(urljoin(alphabetAddress, link),
                          "h3.entry-title a"))
    print('got full list of idea links')
    with open('outfile', 'wb') as fp:
        pickle.dump(entryLinks, fp)


def scrapeIdeaName(page, lang='e'):
    if lang == 'h':
        return page.select("div#idea-titles h1")[0].string.strip()
    else:
        return page.select("div#idea-titles h2")[0].string.strip()


def writeNodes():
    with open('outfile', 'rb') as fp:
        entryLinks = pickle.load(fp)
    for i in range(len(entryLinks)):
        print('getting stuff from', urljoin(ideaAddress, entryLinks[i]))
        page = getPage(urljoin(ideaAddress, entryLinks[i]))
        c.execute("INSERT INTO nodes VALUES (?, ?, ?, ?);",
                  (i, entryLinks[i][27:-1],
                   scrapeIdeaName(page, 'h'), scrapeIdeaName(page)))


def createQuery(num):
    whereUrl = " page_url = ?"
    if num == 0:
        return None
    else:
        return "SELECT Id FROM nodes WHERE" + (whereUrl + " or") * \
            (num - 1) + whereUrl + ";"


def writeEdges():
    c.execute("SELECT Id, page_url FROM nodes;")
    for row in c.fetchall():
        c.execute("SELECT * FROM edges WHERE source = ?", (row[0],))
        d = c.fetchall()
        if len(d) == 0:
            print(row[1])
            print(row[0])
            internalLinks = getLinks(urljoin(ideaAddress, row[1]),
                                     "#post-content a.internal-link")
            print(internalLinks)
            query = createQuery(len(internalLinks))
            c.execute(query, tuple(internalLinks))
            internalLinksIds = c.fetchall()
            for num in internalLinksIds:
                c.execute("INSERT INTO edges VALUES (?, ?);", (row[0], num[0]))
                print(num[0])
            db.commit()
    db.close()


os.chdir("C://Users//Alex//Documents//Py//ideaScraper")
baseAddress = "http://haraayonot.com/"
alphabetAddress = urljoin(baseAddress, "alphabetic-ideas")
ideaAddress = urljoin(baseAddress, "idea/")
db = sqlite3.connect("C:\\Sqlite\\ideaSNA.db")
c = db.cursor()

getIdeas()
writeNodes()
writeEdges()

db.close()
