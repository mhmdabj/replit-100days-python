import datetime

def flask_home_page():
    today = datetime.date.today()
    page = f"""<html><body>
  <p><a href = "/home">Go home</a></p>
  </body>
  </html>"""
    return page

def flask_home():
    today = datetime.date.today()
    page = f"""<html>
  <head>
    <title>David's World Of Baldies</title>
  </head>
  <body>
  <h1>Dave's World of Baldies</h1> 
  <h2>Welcome to our website!</h2>
  <h2>{today}</h2>
  <p>We all know that throughout history some of the greatest have been Baldies, let's see the epicness of their heads bereft of hair.</p>
  <h2>Gallery of Baldies</h2>
  <p>Here are some of the legends of the bald world.</p>
  <img src=\"static/images/picard.jpg\" width = 30%>
  <p><a href = \"https://memory-alpha.fandom.com/wiki/Star_Trek:_Picard\">Captain Jean Luc Picard: Baldest Star Trek captain, and legend.</a></p>
  <ul>
    <li>Beautiful bald man</li>
    <li>Calm and cool under pressure</li>
    <li>All the Picard memes</li>
  </ul>
  <p><a href = \"page2.html\">Go to page 2</a></p>
</body>
</html>
  """
    return page

if __name__ == "__main__":
    print(flask_home_page())
    print(flask_home()) 