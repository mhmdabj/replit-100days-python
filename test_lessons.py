import unittest
from io import StringIO
import sys

from lessons import lesson01, lesson02, lesson03, lesson04, lesson05, lesson06, lesson07, lesson08, lesson09, lesson10, lesson11, lesson12, lesson13, lesson14, lesson15, lesson16, lesson17, lesson18, lesson19, lesson20, lesson21, lesson22, lesson23, lesson24, lesson25, lesson26, lesson27, lesson28, lesson29, lesson30, lesson31, lesson32, lesson33, lesson34, lesson35, lesson36, lesson37, lesson38, lesson39, lesson40, lesson41, lesson42, lesson43, lesson44, lesson45, lesson46, lesson47, lesson48, lesson49, lesson50, lesson51, lesson52, lesson53, lesson54, lesson55, lesson56, lesson57, lesson58, lesson59, lesson60, lesson61, lesson62, lesson63, lesson64, lesson65, lesson70, lesson71, lesson72, lesson76, lesson78, lesson80, lesson81, lesson82, lesson83, lesson84, lesson85, lesson86, lesson87, lesson88, lesson90, lesson91, lesson92, lesson93, lesson94, lesson95, lesson96, lesson97, lesson98, lesson99, lesson100

def capture_output(func, *args, **kwargs):
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        func(*args, **kwargs)
        return sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout

class TestLessons(unittest.TestCase):
    def test_lesson01(self):
        output = capture_output(lesson01.lesson1)
        self.assertIn("September 20, 2029", output)
        self.assertIn("I am si", output)

    def test_lesson02(self):
        output = capture_output(lesson02.lesson2, "Alice")
        self.assertIn("Alice", output)

    def test_lesson03(self):
        output = capture_output(lesson03.lesson3, "Bob", "Pizza")
        self.assertIn("Bob is going to be chowing down on Pizza very soon!", output)

    def test_lesson04(self):
        output = capture_output(lesson04.lesson4, "Alice", "Bob", "fly", "Paris", "Pizza")
        self.assertIn("Hello  Alice ! Your ability to fly will make sure you never have to look at Bob again.", output)

    def test_lesson05(self):
        output = capture_output(lesson05.lesson5, "David")
        self.assertIn("Welcome Dude!", output)
        output2 = capture_output(lesson05.lesson5, "Alice")
        self.assertIn("Who on earth are you?!", output2)

    def test_lesson06(self):
        self.assertIn("Welcome to your page", capture_output(lesson06.lesson6, "admin", "admin"))
        self.assertIn("Welcome user", capture_output(lesson06.lesson6, "user", "user"))
        self.assertIn("Welcome guest", capture_output(lesson06.lesson6, "guest", "guest"))
        self.assertIn("Wrong username or password", capture_output(lesson06.lesson6, "foo", "bar"))

    def test_lesson07(self):
        self.assertIn("That's my favorite character too!", capture_output(lesson07.lesson7, "The Matrix", "Neo"))
        self.assertIn("That's a cool character!", capture_output(lesson07.lesson7, "The Matrix", "Trinity"))
        self.assertIn("That's my favorite character too!", capture_output(lesson07.lesson7, "The Notebook", "Allison"))
        self.assertIn("That's a cool character!", capture_output(lesson07.lesson7, "The Notebook", "Noah"))
        self.assertIn("That's a cool movie!", capture_output(lesson07.lesson7, "Inception", "Cobb"))

    def test_lesson08(self):
        self.assertIn("Hello Abuja", capture_output(lesson08.lesson8, "Abuj", "Monday"))
        self.assertIn("friday time for gamming", capture_output(lesson08.lesson8, "hadi", "Friday"))
        self.assertIn("Invalid name or day", capture_output(lesson08.lesson8, "Alice", "Sunday"))

    def test_lesson09(self):
        self.assertIn("Traditionalists yooo", capture_output(lesson09.lesson9, 1930))
        self.assertIn("Baby Boomers", capture_output(lesson09.lesson9, 1950))
        self.assertIn("Generation X", capture_output(lesson09.lesson9, 1970))
        self.assertIn("Millenials", capture_output(lesson09.lesson9, 1990))
        self.assertIn("Generation Z", capture_output(lesson09.lesson9, 2000))
        self.assertIn("Year out of range", capture_output(lesson09.lesson9, 2020))

    def test_lesson10(self):
        self.assertIn("You all owe", capture_output(lesson10.lesson10, 100, 4, 10))
        self.assertIn("You all owe", capture_output(lesson10.lesson10, 200, 5, 15))

    def test_lesson11(self):
        self.assertIn("Number of seconds in a year are", capture_output(lesson11.lesson11, 365))
        self.assertIn("Number of seconds in a leap year are", capture_output(lesson11.lesson11, 366))

    def test_lesson12(self):
        self.assertEqual(lesson12.lesson12(), "Debugging code - nothing hard lol")

    def test_lesson13(self):
        self.assertIn("A+", capture_output(lesson13.lesson13, "Alice", 100, 95))
        self.assertIn("U", capture_output(lesson13.lesson13, "Bob", 100, 45))

    def test_lesson14(self):
        self.assertIn("p1 won", capture_output(lesson14.lesson14, "R", "S"))
        self.assertIn("p2 won", capture_output(lesson14.lesson14, "P", "S"))
        self.assertIn("tie", capture_output(lesson14.lesson14, "S", "S"))
        self.assertIn("gg", capture_output(lesson14.lesson14, "X", "R"))

    def test_lesson15(self):
        output = capture_output(lesson15.lesson15, [("Cow", "no"), ("cat", "yes")])
        self.assertIn("A cow goes moo.", output)
        self.assertIn("meow", output)

    def test_lesson16(self):
        output = capture_output(lesson16.lesson16, ["take", "give"])
        self.assertIn("Nope, try again.", output)
        self.assertIn("Well done! It only took you 2 attempts.", output)

    def test_lesson17(self):
        moves = [("R", "S"), ("P", "R"), ("S", "P"), ("R", "P"), ("P", "S")]
        output = capture_output(lesson17.lesson17, moves)
        self.assertIn("Game over, PLAYER 1 WON", output)

    def test_lesson18(self):
        output = capture_output(lesson18.lesson18, 50, [10, 100, 50])
        self.assertIn("Too low", output)
        self.assertIn("Too high", output)
        self.assertIn("correct", output)
        self.assertIn("It took you 2 to get it correct", output)

    def test_lesson19(self):
        output = capture_output(lesson19.lesson19, 1000, 3)
        self.assertIn("1050.0", output)
        self.assertIn("1102.5", output)
        self.assertIn("1157.62", output)

    def test_lesson20(self):
        output = capture_output(lesson20.lesson20, 1, 10, 2)
        self.assertIn("Hello World!", output)
        self.assertIn("1", output)
        self.assertIn("3", output)
        self.assertIn("5", output)
        self.assertIn("7", output)
        self.assertIn("9", output)

    def test_lesson21(self):
        output = capture_output(lesson21.lesson21, 2, [2,4,6,8,10,12,14,16,18,20])
        self.assertIn("You scored 10 out of 10.", output)
        output2 = capture_output(lesson21.lesson21, 3, [3,6,9,12,15,18,21,24,27,0])
        self.assertIn("You scored 9 out of 10.", output2)

    def test_lesson22(self):
        output = capture_output(lesson22.lesson22, 42, [10, 100, 42])
        self.assertIn("Too low fanta", output)
        self.assertIn("Too high light", output)
        self.assertIn("Correct 😁", output)
        self.assertIn("It took you 3 guesses to get the number correct.", output)

    def test_lesson23(self):
        output = capture_output(lesson23.rollDice)
        self.assertIn("You rolled", output)
        login_output = capture_output(lesson23.login, [("abuj", "wrong"), ("abuj", "lol")])
        self.assertIn("Welcome to your website!", login_output)
        self.assertIn("Whoops! I don't recognize that username or password. Try again!", login_output)

    def test_lesson24(self):
        output = capture_output(lesson24.rollDice, 6, ["y", "n"])
        self.assertIn("Your rolled", output)
        self.assertIn("Goodbye!", output)

    def test_lesson25(self):
        pin = lesson25.pinPicker(4, seed=42)
        self.assertEqual(len(pin), 4)
        self.assertTrue(pin.isdigit())
        stats_output = capture_output(lesson25.character_stats, ["Alice", "Bob", "Charlie"], 42)
        self.assertIn("Their health is:", stats_output)

    def test_lesson26(self):
        output = capture_output(lesson26.lesson26, [1, 2])
        self.assertIn("Welcome", output)
        self.assertIn("Playing sound...", output)
        self.assertIn("Paused.", output)
        self.assertIn("Exiting...", output)

    def test_lesson27(self):
        output = capture_output(lesson27.lesson27, [("Alice", "Elf"), ("Bob", "Orc")], 42)
        self.assertIn("HEALTH:", output)
        self.assertIn("STRENGTH:", output)
        self.assertIn("May your name go down in Legend...", output)

    def test_lesson28(self):
        output = capture_output(lesson28.lesson28, "Alice", "Elf", "Bob", "Orc", 42)
        self.assertIn("BATTLE TIME", output)
        self.assertTrue("has died!" in output or "destroyed" in output)

    def test_lesson29(self):
        output = capture_output(lesson29.print_numbers)
        self.assertIn("0, 1, 2, 3, 4, 5", output)
        self.assertIn("99", output)
        self.assertIn("mhmd", lesson29.color("mhmd", "red"))

    def test_lesson30(self):
        output = capture_output(lesson30.format_examples)
        self.assertIn("This is Katie", output)
        self.assertIn("Day 30 of 30", output)
        thoughts = [f"thought {i}" for i in range(1, 31)]
        ex_output = capture_output(lesson30.exercise, thoughts)
        self.assertIn("You thought day 1 was thought 1", ex_output)
        self.assertIn("30 Days Down - What did you think?", ex_output)

    def test_lesson31(self):
        output = capture_output(lesson31.print_music_app)
        self.assertIn("Music App", output)
        output2 = capture_output(lesson31.print_armbook)
        self.assertIn("ARMBOOK", output2)

    def test_lesson32(self):
        output = capture_output(lesson32.random_greeting, 42)
        self.assertIn(", Welcome to heaven", output)

    def test_lesson33(self):
        output = capture_output(lesson33.simulate_todo, [("add", "Task1"), ("add", "Task2"), ("view", None), ("remove", "Task1"), ("view", None)])
        self.assertIn("Task1", output)
        self.assertIn("Task2", output)
        self.assertIn("is removed", output)

    def test_lesson34(self):
        output = capture_output(lesson34.simulate_spammer, [("add", "a@example.com"), ("add", "b@example.com"), ("show", None), ("spam", 2), ("remove", "a@example.com"), ("show", None)])
        self.assertIn("listofEmail", output)
        self.assertIn("Spam Email 1by1", output)

    def test_lesson35(self):
        output = capture_output(lesson35.simulate_manager, [("add", "Task1"), ("add", "Task2"), ("view", None), ("edit", "Task1", "Task1-Edited"), ("remove", "Task2", True), ("clear", None)])
        self.assertIn("Added: Task1", output)
        self.assertIn("Your List is clear", output)

    def test_lesson36(self):
        output = capture_output(lesson36.add_names, [("alice", "smith"), ("bob ", " jones"), ("alice", "smith")])
        self.assertIn("Alice Smith", output)
        self.assertIn("Bob Jones", output)
        self.assertIn("ERROR: Duplicate name", output)

    def test_lesson37(self):
        self.assertIn("Davmor Joiff", lesson37.his_star_wars_name(["David", "Morgan", "Jones", "Cardiff"]))

    def test_lesson38(self):
        output2 = capture_output(lesson38.color_sentence, "Abcdefg")
        self.assertIn("A\x1b[34mbcdef\x1b[32mg\n", output2)

    def test_lesson39(self):
        output = capture_output(lesson39.hangman, "apple", ["a", "p", "l", "e"])
        self.assertIn("You won with", output)
        output2 = capture_output(lesson39.hangman, "pear", ["x", "y", "z", "p", "e", "a", "r"])
        self.assertTrue("You won with" in output2 or "You ran out of lives!" in output2)

    def test_lesson40(self):
        output = capture_output(lesson40.update_user)
        self.assertIn("The legendary David", output)
        output2 = capture_output(lesson40.contact_card, "Alice", "2000-01-01", "1234567890", "alice@example.com", "123 Main St")
        self.assertIn("Hi Alice", output2)

    def test_lesson41(self):
        d = {"name": "Ian", "health": 219, "strength": 199, "equipped": "Axe"}
        output = capture_output(lesson41.print_dict_values, d)
        self.assertIn("Ian", output)
        output2 = capture_output(lesson41.print_dict_items, d)
        self.assertIn("name:Ian", output2)
        website = lesson41.fill_website_info("TestSite", "https://test.com", "A test site", "5")
        self.assertEqual(website["name"], "TestSite")

    def test_lesson42(self):
        output = capture_output(lesson42.fill_beast_dic, "dragon", "Fire", "Roar", "100", "50")
        self.assertIn("Beast Name", output)
        self.assertIn("Fire", output)

    def test_lesson43(self):
        output = capture_output(lesson43.generate_bingo_card, 42)
        self.assertIn("BINGO", output)

    def test_lesson44(self):
        output = capture_output(lesson44.bingo_marking, 42, [1,2,3,4,5,6,7,8])
        self.assertIn("Bingo", output)
        self.assertIn("X", output)

    def test_lesson45(self):
        output = capture_output(lesson45.simulate_life_organizer, [("add", "Task1", "Tomorrow", "High"), ("add", "Task2", "Next Week", "Low"), ("view", "all"), ("edit", "Task1", "name", "Task1-Edited"), ("remove", "Task2"), ("print",)])
        self.assertIn("Task1", output)
        self.assertIn("removed successfully", output)

    def test_lesson46(self):
        game = lesson46.ClueGame()
        game.add("Alice", "Library", "Candlestick")
        output = capture_output(game.prettyPrint)
        self.assertIn("Alice", output)
        m = lesson46.Mokedex()
        m.add("Pikachu", "Electric", "Thunderbolt", "35", "55")
        output2 = capture_output(m.prettyPrint)
        self.assertIn("Pikachu", output2)

    def test_lesson47(self):
        game = lesson47.TopTrumps()
        game.add_card("David", 178, 99, 80, 99)
        game.add_card("Spock", 200, 50, 50, 0)
        output = capture_output(game.compare_stats, "David", "Spock", "Intelligence")
        self.assertIn("David", output)
        self.assertIn("Spock", output)

    def test_lesson48(self):
        from io import StringIO
        f = StringIO()
        lesson48.add_scores_interactive(f, [("AB", 100), ("CD", 200)])
        self.assertIn("AB", f.getvalue())
        self.assertIn("CD", f.getvalue())

    def test_lesson49(self):
        from io import StringIO
        f = StringIO("AB 100\nCD 200\n")
        text, max_number = lesson49.find_leader(f)
        self.assertEqual(text, "CD")
        self.assertEqual(max_number, 200)

    def test_lesson50(self):
        from io import StringIO
        f = StringIO()
        lesson50.add_idea(f, "Build a rocket")
        lesson50.add_idea(f, "Learn Python")
        f.seek(0)
        idea = lesson50.get_random_idea(f, seed=42)
        self.assertIn(idea, ["Build", "a", "rocket", "Learn", "Python"])

    def test_lesson51(self):
        from io import StringIO
        f = StringIO("[]")
        org = lesson51.LifeOrganizer51()
        org.load(f)
        org.add("Task1", "Tomorrow", "High")
        org.save(f)
        self.assertIn("Task1", f.getvalue())

    def test_lesson52(self):
        from io import StringIO
        f = StringIO("[]")
        orders = lesson52.PizzaOrders()
        orders.load(f)
        orders.add(2, 10, "Alice")
        orders.save(f)
        self.assertIn("Alice", f.getvalue())

    def test_lesson53(self):
        self.assertEqual(sorted(lesson53.remove_duplicates([1, 2, 2, 3, 4, 4, 5])), [1,2,3,4,5])

    def test_lesson54(self):
        from io import StringIO
        csv_content = "Net Total\n10\n20\n30\n"
        f = StringIO(csv_content)
        total = lesson54.csv_total(f, "Net Total")
        self.assertEqual(total, 60)
        csv_content2 = "Cost,Quantity\n5,2\n3,4\n"
        f2 = StringIO(csv_content2)
        total2 = lesson54.csv_total_mult(f2, "Cost", "Quantity")
        self.assertEqual(total2, 22)

    def test_lesson55(self):
        todo = lesson55.ToDoList55()
        todo.add("Task1", "Tomorrow", "High")
        output = capture_output(todo.view, "all")
        self.assertIn("Task1", output)

    def test_lesson56(self):
        csv_content = "Artist(s),Song\nQueen,Bohemian Rhapsody\nAdele,Hello\n"
        seen = lesson56.simulate_streamed_songs(csv_content)
        self.assertIn("Queen", seen)
        self.assertIn("Adele", seen)

    def test_lesson57(self):
        output = capture_output(lesson57.reverse, 4)
        self.assertIn("💯", output)
        self.assertIn("Done!", output)
        self.assertEqual(lesson57.factorial(5), 120)

    def test_lesson58(self):
        output = capture_output(lesson58.guessing_game, [50, 25, 75, 42], 42)
        self.assertIn("Just right!", output)
        self.assertIn("3 attempts", output)

    def test_lesson59(self):
        output = capture_output(lesson59.palindrome_iterative, "racecar")
        self.assertIn("is a palindrome", output)
        self.assertTrue(lesson59.palindrome_recursive("racecar"))
        output2 = capture_output(lesson59.palindrome_iterative, "hello")
        self.assertIn("not a palindrome", output2)
        self.assertFalse(lesson59.palindrome_recursive("hello"))

    def test_lesson60(self):
        output = capture_output(lesson60.print_date, 2022, 12, 7)
        self.assertIn("2022-12-07", output)

    def test_lesson61(self):
        class DummyShelf(dict): pass
        db = DummyShelf()
        app = lesson61.TweetApp(db)
        app.add_tweet("Alice", "Hello world!")
        app.add_tweet("Bob", "Second tweet!")
        output = capture_output(app.view_tweets)
        self.assertIn("Alice", output)
        self.assertIn("Bob", output)

    def test_lesson62(self):
        class DummyShelf(dict): pass
        shelf = DummyShelf()
        diary = lesson62.Diary(shelf)
        diary.set_password("testpass")
        diary.add_secret("My first secret!")
        diary.add_secret("Another secret!")
        output = capture_output(diary.view_entries)
        self.assertIn("My first secret!", output)
        self.assertIn("Another secret!", output)

    def test_lesson63(self):
        class MockModule:
            @staticmethod
            def countdown():
                print("3, 2, 1, Go!")
        output = capture_output(lesson63.import_and_countdown, MockModule)
        self.assertIn("Countdown", output)
        self.assertIn("3, 2, 1, Go!", output)

    def test_lesson64(self):
        output = capture_output(lesson64.animal_example)
        self.assertIn("Moo", output)
        output2 = capture_output(lesson64.job_example)
        self.assertIn("Jobs Jobs Jobs", output2)

    def test_lesson65(self):
        output = capture_output(lesson65.character_example)
        self.assertIn("Player", output)
        self.assertIn("Orc", output)
        self.assertIn("Vampire", output)

    def test_lesson70(self):
        env = {'adminUsername': 'admin', 'adminPassword': 'adminpass', 'username': 'user', 'password': 'userpass'}
        self.assertEqual(lesson70.check_login('admin', 'adminpass', env), "admin")
        self.assertEqual(lesson70.check_login('user', 'userpass', env), "normy")
        self.assertIsNone(lesson70.check_login('foo', 'bar', env))

    def test_lesson71(self):
        sys = lesson71.LoginSystem()
        sys.add_user("david", "Baldy1")
        self.assertTrue(sys.login("david", "Baldy1"))
        self.assertFalse(sys.login("david", "wrong"))
        self.assertFalse(sys.login("bob", "Baldy1"))

    def test_lesson72(self):
        sys = lesson72.LoginSystem72()
        sys.add_user("david", "Baldy1")
        self.assertTrue(sys.login("david", "Baldy1"))
        self.assertFalse(sys.login("david", "wrong"))
        self.assertFalse(sys.login("bob", "Baldy1"))

    def test_lesson76(self):
        self.assertIn("Go home", lesson76.flask_home_page())
        self.assertIn("World of Baldies", lesson76.flask_home())

    def test_lesson78(self):
        myReflections = {"75": {"link": "https://replit.com/@replit/Day-75-Solution", "Reflection": "Test reflection"}}
        template = '<html><head><title>Day {day} Reflection</title></head><body><h1>Day {day} Reflection</h1><p><a href="{link}">See my code here</a></p><p>{reflection}</p></body></html>'
        page = lesson78.reflection_page("75", myReflections, template)
        self.assertIn("Test reflection", page)

    def test_lesson80(self):
        logins = {"david": {"email": "a@a.com", "password": "Baldy1"}}
        self.assertEqual(lesson80.flask_login("david", "a@a.com", "Baldy1", logins), "You are logged in")
        self.assertEqual(lesson80.flask_login("david", "a@a.com", "wrong", logins), "Username, email or password incorrect")

    def test_lesson81(self):
        self.assertEqual(lesson81.robot_detector("Yes", "2", "human food"), "You're a robot!")
        self.assertEqual(lesson81.robot_detector("No", "error123", "human food"), "You're a robot!")
        self.assertEqual(lesson81.robot_detector("No", "infinity", "synthetic oil"), "You're a robot!")
        self.assertEqual(lesson81.robot_detector("No", "infinity", "human food"), "Hi there fellow human")

    def test_lesson82(self):
        self.assertEqual(lesson82.language_greeting("eng"), "Hello, and welcome to our wonderful website!")
        self.assertEqual(lesson82.language_greeting("wel"), "Helo, a chroeso i'n gwefan wych!")
        self.assertEqual(lesson82.language_greeting("fr"), "Unsupported language")
        self.assertEqual(lesson82.language_greeting(""), "Nothing here")

    def test_lesson83(self):
        template = '<html><head><title>{title}</title></head><body><h1>{title}</h1><p>Date: {date}</p><p>{text}</p></body></html>'
        page = lesson83.blog_page("Hello World", "October 25th", "Here is my first blog entry.", template)
        self.assertIn("Hello World", page)
        self.assertIn("October 25th", page)

    def test_lesson84(self):
        auth = lesson84.AuthSystem84()
        self.assertEqual(auth.signup("david", "David", "Baldy1"), "Signup successful")
        self.assertEqual(auth.signup("david", "David", "Baldy1"), "User already exists")
        self.assertEqual(auth.login("david", "Baldy1"), "Hello David")
        self.assertEqual(auth.login("david", "wrong"), "Incorrect password")
        self.assertEqual(auth.login("bob", "Baldy1"), "User not found")

    def test_lesson85(self):
        auth = lesson85.AuthSystem85()
        self.assertEqual(auth.signup("david", "David", "Baldy1"), "Signup successful")
        self.assertEqual(auth.login("david", "Baldy1"), "Welcome David")
        self.assertEqual(auth.welcome(), "Hi there David")
        self.assertEqual(auth.logout(), "Logged out")
        self.assertEqual(auth.welcome(), "Not logged in")

    def test_lesson86(self):
        blog = lesson86.BlogSystem86()
        self.assertEqual(blog.login("david", "Baldy1"), "Login successful")
        self.assertEqual(blog.add_blog("First Post", "2024-01-01", "Hello World!"), "Blog added")
        self.assertIn("First Post", blog.get_blogs())
        self.assertEqual(blog.logout(), "Logged out")

    def test_lesson87(self):
        blog = lesson87.BlogSystem87("adminuser")
        self.assertEqual(blog.login("david", "Baldy1", "adminuser"), "Login successful (admin)")
        self.assertEqual(blog.add_blog("First Post", "2024-01-01", "Hello World!", "adminuser"), "Blog added")
        self.assertIn("First Post", blog.get_blogs())
        self.assertEqual(blog.logout(), "Logged out")

    def test_lesson88(self):
        blog = lesson88.BlogSystem88("123456")
        self.assertEqual(blog.login("david", "Baldy1", "123456"), "Login successful (admin)")
        self.assertEqual(blog.add_blog("First Post", "2024-01-01", "Hello World!", "123456"), "Blog added")
        self.assertIn("First Post", blog.get_blogs())
        self.assertEqual(blog.logout(), "Logged out")

    def test_lesson90(self):
        class MockResponse:
            def json(self):
                return {"results": [{"name": {"first": "John", "last": "Doe"}, "picture": {"medium": "http://example.com/image.jpg"}}]}
        class MockRequests:
            @staticmethod
            def get(url):
                return MockResponse()
        name, image = lesson90.get_random_user(MockRequests)
        self.assertEqual(name, "John Doe")
        self.assertEqual(image, "http://example.com/image.jpg")

    def test_lesson91(self):
        class MockResponse:
            def json(self):
                return {"joke": "Why did the chicken cross the road? To get to the other side!", "id": "abc123"}
        class MockRequests:
            @staticmethod
            def get(url, headers=None):
                return MockResponse()
        joke = lesson91.get_dad_joke(MockRequests)
        self.assertIn("chicken cross the road", joke)

    def test_lesson92(self):
        self.assertIn("Weather for London", lesson92.get_weather_stub("London"))

    def test_lesson93(self):
        tracks = lesson93.get_spotify_tracks_stub(1990)
        self.assertIn("Track 1 from 1990", tracks)

    def test_lesson94(self):
        self.assertIn("API Smash Battle", lesson94.api_smash_battle_stub())

    def test_lesson95(self):
        news, songs = lesson95.news_spotify_stub()
        self.assertIn("News summary 1", news)
        self.assertIn("Song 1", songs)

    def test_lesson96(self):
        html = '<span class="titleline"><a href="https://example.com">Replit launches new feature</a></span>'
        results = lesson96.scrape_links(html, ["replit", "python"])
        self.assertIn("Replit launches new feature", results[0])
        self.assertIn("https://example.com", results[1])

    def test_lesson97(self):
        self.assertIn("stubbed summary", lesson97.wiki_openai_summarizer_stub("https://en.wikipedia.org/wiki/Hair_loss"))

    def test_lesson98(self):
        self.assertIn("Email scheduler", lesson98.email_scheduler_stub())

    def test_lesson99(self):
        self.assertIn("Event scraper", lesson99.event_scraper_emailer_stub())

    def test_lesson100(self):
        self.assertIn("Price scraper", lesson100.price_scraper_notifier_stub())

if __name__ == "__main__":
    unittest.main() 