def blog_page(title, date, text, template):
    page = template
    page = page.replace("{title}", title)
    page = page.replace("{date}", date)
    page = page.replace("{text}", text)
    return page

if __name__ == "__main__":
    template = '''<html>\n  <head>\n    <title>{title}</title>\n  </head>\n  <body>\n    <h1>{title}</h1>\n    <p>Date: {date}</p>\n    <p>{text}</p>\n  </body>\n</html>'''
    print(blog_page("Hello World", "October 25th", "Here is my first blog entry.", template))
    print(blog_page("Bye World", "October 25th", "Here is my last blog entry.", template)) 