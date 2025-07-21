def lesson13(name, maxScore, selfScore):
    scorePercentage = 100 / (maxScore / selfScore)
    roundScore = round(scorePercentage, 2)
    if roundScore < 50:
        print("U")
    elif roundScore <= 59 and roundScore >= 50:
        print("D")
    elif roundScore <= 69 and roundScore >= 60:
        print("C")
    elif roundScore <= 79 and roundScore >= 70:
        print("B")
    elif roundScore <= 89 and roundScore >= 80:
        print("A")
    elif roundScore <= 100 and roundScore >= 90:
        print("A+")
    else:
        print("emhiha")

if __name__ == "__main__":
    lesson13("Alice", 100, 95)
    lesson13("Bob", 100, 45) 