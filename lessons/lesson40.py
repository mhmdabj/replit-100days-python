def update_user():
    myUser = {"name": "David", "age": 128}
    print(myUser["name"])
    myUser["name"] = "The legendary David"
    print(myUser)
    return myUser

def contact_card(name, date, phone, email, address):
    database = {
        "name": name.strip(),
        "date": date.strip(),
        "phone": phone.strip(),
        "email": email.strip(),
        "address": address.strip()
    }
    print(f"Hi {database['name']}. Our dictionary says that you were born on {database['date']}, we can call you on {database['phone']},email {database['email']}, or write to {database['address']} ")
    return database

if __name__ == "__main__":
    update_user()
    contact_card("Alice", "2000-01-01", "1234567890", "alice@example.com", "123 Main St") 