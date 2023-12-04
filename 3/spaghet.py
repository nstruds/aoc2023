import os
import re

f = open(os.path.dirname(os.path.realpath(__file__)) + "\\input.txt", "r")
Lines = f.read().split('\n')
f.close()

counter = 0
sum = 0

numbersAlreadyAdded = {}

def is_standalone_number(number, string, index):
  startIndex = index
  endIndex = index+(len(str(number))-1)
  isstandalone = True

  if startIndex != 0:
      if string[startIndex-1].isdigit():
        isstandalone = False

  if endIndex < len(string)-1:
      if string[endIndex+1].isdigit():
        isstandalone = False

  return isstandalone
"""part1
for i, l in enumerate(Lines):
    symbolIndex = []
    for index, c in enumerate(l):
        if not c.isdigit() and c != ".":
            symbolIndex.append(index)

    numbersInPrevLine = []
    numbersinNextLine = []
    numbersInCurrentLine = []

    prevLine = ""
    nextLine = ""

    if i > 0:
        prevLine = Lines[i-1]
        numbersInPrevLine = re.findall(r'\b\d+\b', prevLine)
    if i < len(Lines)-1:
        nextLine = Lines[i+1]
        numbersinNextLine = re.findall(r'\b\d+\b', nextLine)

    numbersInCurrentLine = re.findall(r'\b\d+\b', l)
    if len(symbolIndex) > 0:

        if len(numbersInPrevLine) > 0:
            for n in numbersInPrevLine:
                indeces = [i for i in range(len(prevLine)) if prevLine.startswith(str(n), i)]
                for x in indeces:
                    for s in symbolIndex:
                        if (s >= x-1 and s <= (x + len(str(n)))):
                            if is_standalone_number(n, prevLine, x):
                                numbersAlreadyAdded[(str(i-1) + "-" + str(x))] = n

        if len(numbersInCurrentLine) > 0:
            for n in numbersInCurrentLine:
                indeces = [i for i in range(len(l)) if l.startswith(str(n), i)]
                for x in indeces:
                    for s in symbolIndex:
                        if (s >= x-1 and s <= (x + len(str(n)))):
                            if is_standalone_number(n, l, x):
                                numbersAlreadyAdded[(str(i) + "-" + str(x))] = n    

        if len(numbersinNextLine) > 0:
            for n in numbersinNextLine:
                indeces = [i for i in range(len(nextLine)) if nextLine.startswith(str(n), i)]
                for x in indeces:
                    for s in symbolIndex:
                        if (s >= x-1 and s <= (x + len(str(n)))):
                            if is_standalone_number(n, nextLine, x):
                                numbersAlreadyAdded[(str(i+1) + "-" + str(x))] = n   
    counter += 1

dics = {}

for d in numbersAlreadyAdded:
    sum += int(numbersAlreadyAdded[d])
    line = int(d.split("-")[0]) + 1

    if line not in dics.keys():
        dics[line] = []
    dics[line].append(numbersAlreadyAdded[d])

print(dict(sorted(dics.items())))

print(sum)
"""

digitsDict = {}

for i, l in enumerate(Lines):
    numbersInCurrentLine = re.findall(r'\b\d+\b', l)
    for n in numbersInCurrentLine:
        indeces = [i for i in range(len(l)) if l.startswith(str(n), i)]
        for x in indeces:
            if is_standalone_number(n, l, x):
                digitsDict[(str(i) + "," + str(x))] = n
    counter += 1

added = {}

for i, l in enumerate(Lines):
    symbolIndex = []
    for index, c in enumerate(l):
        if c == "*":
            symbolIndex.append(index)
    
    if len(symbolIndex) > 0:
        for s in symbolIndex:
            added[(str(i) + "," + str(s))] = []
            for d in digitsDict:
                dindex = int(d.split(",")[1])
                if str(d).startswith(str(i-1)+",") or str(d).startswith(str(i)+",") or str(d).startswith(str(i+1)+","):
                    if (s >= dindex-1 and s <= (dindex + len(str(digitsDict[d])))):
                        added[(str(i) + "," + str(s))].append(digitsDict[d])

gearRatioSum = 0

for a in added:
    if len(added[a]) == 2:
        gearRatioSum += int(added[a][0]) * int(added[a][1])


print(gearRatioSum)

