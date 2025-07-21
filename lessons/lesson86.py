class BlogSystem86:
    def __init__(self):
        self.db = {"user": {"username": "david", "password": "Baldy1"}}
        self.session = {}
        self.blogs = {}
    def login(self, username, password):
        if username == self.db["user"]["username"] and password == self.db["user"]["password"]:
            self.session["user"] = True
            return "Login successful"
        else:
            return "Login failed"
    def logout(self):
        self.session.clear()
        return "Logged out"
    def add_blog(self, title, date, body):
        self.blogs[date] = {"title": title, "date": date, "body": body}
        return "Blog added"
    def get_blogs(self):
        content = ""
        for key in sorted(self.blogs.keys(), reverse=True):
            entry = self.blogs[key]
            content += f"<h2>{entry['title']}</h2><p>{entry['date']}</p><p>{entry['body']}</p>"
        return content

if __name__ == "__main__":
    blog = BlogSystem86()
    print(blog.login("david", "Baldy1"))
    print(blog.add_blog("First Post", "2024-01-01", "Hello World!"))
    print(blog.get_blogs())
    print(blog.logout()) 