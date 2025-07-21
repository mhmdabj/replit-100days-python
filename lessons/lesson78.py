def reflection_page(pageNumber, myReflections, template):
    page = template
    page = page.replace("{day}", str(pageNumber))
    page = page.replace("{link}", myReflections[pageNumber]["link"])
    page = page.replace("{reflection}", myReflections[pageNumber]["Reflection"])
    return page

if __name__ == "__main__":
    myReflections = {
        "75": {"link" : "https://replit.com/@replit/Day-75-Solution", "Reflection" : "Was a bit of a head scratcher, but I got there in the end. Even if I was a bit lazy with the css 😭"},
        "76": {"link" : "https://replit.com/@replit/Day-76-Solution", "Reflection" : "Oh. Easy. Done. Boom"}
    }
    template = '''<html>\n  <head>\n    <title>Day {day} Reflection</title>\n  </head>\n  <body>\n    <h1>Day {day} Reflection</h1>\n    <p><a href="{link}">See my code here</a></p>\n    <p>{reflection}</p>\n  </body>\n</html>'''
    print(reflection_page("75", myReflections, template)) 