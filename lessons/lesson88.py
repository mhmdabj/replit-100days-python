class BlogSystem88:
    def __init__(self, adminUserId):
        self.db = {"user": {"username": "david", "password": "Baldy1"}}
        self.session = {}
        self.blogs = {}
        self.adminUserId = adminUserId
    def login(self, username, password, userid):
        if userid == self.adminUserId:
            self.session["user"] = True
            return "Login successful (admin)"
        if username == self.db["user"]["username"] and password == self.db["user"]["password"]:
            self.session["user"] = True
            return "Login successful"
        else:
            return "Login failed"
    def logout(self):
        self.session.clear()
        return "Logged out"
    def add_blog(self, title, date, body, userid):
        if userid != self.adminUserId:
            return "Not allowed"
        self.blogs[date] = {"title": title, "date": date, "body": body}
        return "Blog added"
    def get_blogs(self):
        content = ""
        for key in sorted(self.blogs.keys(), reverse=True):
            entry = self.blogs[key]
            content += f"<h2>{entry['title']}</h2><p>{entry['date']}</p><p>{entry['body']}</p>"
        return content

if __name__ == "__main__":
    blog = BlogSystem88("123456")
    print(blog.login("david", "Baldy1", "123456"))
    print(blog.add_blog("First Post", "2024-01-01", "Hello World!", "123456"))
    print(blog.get_blogs())
    print(blog.logout()) 