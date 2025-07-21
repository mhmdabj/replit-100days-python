import datetime
import uuid

class TweetApp:
    def __init__(self, db):
        self.db = db
    def add_tweet(self, name, tweet):
        record = {"name": name, "tweet": tweet, "timestamp": datetime.datetime.now()}
        self.db[str(uuid.uuid4())] = record
        print("✅ Tweet saved!")
    def view_tweets(self):
        tweets = list(self.db.values())
        tweets.sort(key=lambda t: t["timestamp"])
        total = len(tweets)
        if total == 0:
            print("No tweets found.")
            return
        index = 0
        while index < total:
            for t in tweets[index:index + 10]:
                ts = t["timestamp"].strftime("%Y-%m-%d %H:%M:%S")
                print(f"{ts} | @{t['name']}: {t['tweet']}")
            index += 10
            if index < total:
                break
            else:
                print("\n✅ End of tweets.")
                break

if __name__ == "__main__":
    class DummyShelf(dict): pass
    db = DummyShelf()
    app = TweetApp(db)
    app.add_tweet("Alice", "Hello world!")
    app.add_tweet("Bob", "Second tweet!")
    app.view_tweets() 