import os

f = open(os.path.dirname(os.path.realpath(__file__)) + "\\input.txt", "r")
Lines = f.readlines()
f.close()

sumOfIds = 0
""" part 1
for l in Lines:
    parts = l.split(":")
    game = parts[0]
    sets = parts[1].split(";")
    gameIsPossible = True

    for s in sets:     
        if not gameIsPossible:
            continue

        cubes = s.split(",")
        for c in cubes:
            if not gameIsPossible:
                continue
            cubeParts = c.strip().split(" ")
            
            amount = int(cubeParts[0])
            color = cubeParts[1]

            if "red" in color:
                gameIsPossible = amount <= 12
            if "green" in color:
                gameIsPossible = amount <= 13
            if "blue" in color:
                gameIsPossible = amount <= 14

    if gameIsPossible:
        sumOfIds += int(game.replace("Game ", ""))

    if not gameIsPossible:
        print("")
       
print(sumOfIds)
"""

""" part 2 """
powerSumOfSets = 0

for l in Lines:
    parts = l.split(":")
    game = parts[0]
    sets = parts[1].split(";")

    highestRed = 0
    highestGreen = 0
    highestBlue = 0

    for s in sets:     
        cubes = s.split(",")
        for c in cubes:
            cubeParts = c.strip().split(" ")
            
            amount = int(cubeParts[0])
            color = cubeParts[1]

            if "red" in color and amount > highestRed:
                highestRed = amount
            if "green" in color and amount > highestGreen:
                highestGreen = amount
            if "blue" in color and amount > highestBlue:
                highestBlue = amount

    powerSumOfSets += (highestRed * highestGreen * highestBlue)

print(powerSumOfSets)
