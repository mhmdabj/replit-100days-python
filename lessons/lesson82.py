def language_greeting(lang):
    if not lang:
        return "Nothing here"
    if lang == "eng":
        return "Hello, and welcome to our wonderful website!"
    elif lang == "wel":
        return "Helo, a chroeso i'n gwefan wych!"
    else:
        return "Unsupported language"

if __name__ == "__main__":
    print(language_greeting("eng"))
    print(language_greeting("wel"))
    print(language_greeting("fr"))
    print(language_greeting("")) 