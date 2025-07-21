def print_dict_values(d):
    for value in d.values():
        print(value)

def print_dict_items(d):
    for name, value in d.items():
        print(f"{name}:{value}")

def fill_website_info(name, url, desc, rating):
    website = {"name": name, "url": url, "desc": desc, "rating": rating}
    print()
    for k, v in website.items():
        print(f"{k}: {v}")
    return website

if __name__ == "__main__":
    d = {"name": "Ian", "health": 219, "strength": 199, "equipped": "Axe"}
    print_dict_values(d)
    print_dict_items(d)
    fill_website_info("TestSite", "https://test.com", "A test site", "5") 