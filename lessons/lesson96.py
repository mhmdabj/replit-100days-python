from bs4 import BeautifulSoup

def scrape_links(html, keywords):
    soup = BeautifulSoup(html, "html.parser")
    myLinks = soup.find_all("span", {"class": "titleline"})
    results = []
    for link in myLinks:
        text = link.text
        textList = text.split()
        containsWord = False
        for word in textList:
            if word.lower() in keywords:
                containsWord= True
        if containsWord:
            results.append(text)
            myLink = link.find_all("a")
            if myLink:
                results.append(myLink[0]["href"])
    return results

if __name__ == "__main__":
    html = '''<span class="titleline"><a href="https://example.com">Replit launches new feature</a></span>'''
    print(scrape_links(html, ["replit", "python"])) 