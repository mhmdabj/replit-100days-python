import datetime

class Diary:
    def __init__(self, shelf):
        self.shelf = shelf
    def set_password(self, password):
        self.shelf['password'] = password
    def add_secret(self, entry):
        timestamp = datetime.datetime.now().isoformat()
        secrets = self.shelf.get('secrets', [])
        secrets.append({'timestamp': timestamp, 'entry': entry})
        self.shelf['secrets'] = secrets
        print("Secret saved!")
    def view_entries(self):
        secrets = self.shelf.get('secrets', [])
        if not secrets:
            print("No entries found.")
            return
        index = len(secrets) - 1
        while index >= 0:
            print(f"\n[{secrets[index]['timestamp']}]\n{secrets[index]['entry']}")
            index -= 1

if __name__ == "__main__":
    class DummyShelf(dict): pass
    shelf = DummyShelf()
    diary = Diary(shelf)
    diary.set_password("testpass")
    diary.add_secret("My first secret!")
    diary.add_secret("Another secret!")
    diary.view_entries() 