def lesson10(myBill, numberOfPeople, tip):
    totalBill = (myBill + ((myBill * tip) / 100)) / numberOfPeople
    roundBill = round(totalBill , 2)
    print("You all owe", roundBill)

# Example usage for testing
if __name__ == "__main__":
    lesson10(100, 4, 10)
    lesson10(200, 5, 15) 