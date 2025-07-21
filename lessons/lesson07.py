def lesson7(movie, favoritecharacter):
    if(movie == "The Matrix"):
        if(favoritecharacter == "Neo"):
            print("That's my favorite character too!")
        else:
            print("That's a cool character!")
    elif(movie == "The Notebook"):
        if(favoritecharacter == "Allison"):
            print("That's my favorite character too!")
        else:
            print("That's a cool character!")
    else:
        print("That's a cool movie!")

# Example usage for testing
if __name__ == "__main__":
    lesson7("The Matrix", "Neo")
    lesson7("The Matrix", "Trinity")
    lesson7("The Notebook", "Allison")
    lesson7("The Notebook", "Noah")
    lesson7("Inception", "Cobb") 