import os

f = open(os.path.dirname(os.path.realpath(__file__)) + "\\input.txt", "r")
Lines = f.read().split('\n')
f.close()

"""part1
cardPointsSum = 0

for i,l in enumerate(Lines):
    cardPoints = 0
    cardParts = l.split(":")
    numbers = cardParts[1].split("|")

    winningNumbers = numbers[0].strip().split(" ")
    myNumbers = numbers[1].strip().split(" ")

    myWinningNumbers = list(filter(None, set(winningNumbers).intersection(set(myNumbers))))

    for w in myWinningNumbers:
        if cardPoints == 0:
            cardPoints = 1
            continue
        cardPoints *= 2

    cardPointsSum += cardPoints
    #print((cardParts[0], cardPoints))

print(cardPointsSum)
"""

"""part2"""
cardCopies = {}

for i,l in enumerate(Lines): 
    cardParts = l.split(":")
    numbers = cardParts[1].split("|")

    cardNumber = i+1

    if not cardNumber in cardCopies.keys():
        cardCopies[cardNumber] = 1
    else:
        cardCopies[cardNumber] += 1

    winningNumbers = numbers[0].strip().split(" ")
    myNumbers = numbers[1].strip().split(" ")

    myWinningNumbers = list(filter(None, set(winningNumbers).intersection(set(myNumbers))))
    winningNumbersCount = len(myWinningNumbers)

    for x in range(1, winningNumbersCount+1):
        cardCopyNumber = cardNumber+x
        if not cardCopyNumber in cardCopies.keys():
            cardCopies[cardCopyNumber] = 1*cardCopies[cardNumber]
        else:
            cardCopies[cardCopyNumber] += 1*cardCopies[cardNumber]

print(sum(cardCopies.values()))
