def lesson19(price, years=10):
    for counter in range(years):
        price += (price * 5) / 100
        print(round(price, 2))

if __name__ == "__main__":
    lesson19(1000, 10) 