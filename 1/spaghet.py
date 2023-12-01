import os

f = open(os.path.dirname(os.path.realpath(__file__)) + "\input.txt", "r")
Lines = f.readlines()

sum = 0

#part 1
valid_digits = {  
  "1":1,
  "2":2,
  "3":3,
  "4":4,
  "5":5,
  "6":6,
  "7":7,
  "8":8,
  "9":9,
  "0":0
}

""" part2
valid_digits = {  
  "one": 1,
  "two": 2,
  "three": 3,
  "four": 4,
  "five": 5,
  "six": 6,
  "seven": 7,
  "eight": 8,
  "nine": 9,
  "1":1,
  "2":2,
  "3":3,
  "4":4,
  "5":5,
  "6":6,
  "7":7,
  "8":8,
  "9":9,
  "0":0
}
"""
for l in Lines:
    occurences = {}
    for k in valid_digits:
        if k in l:
            res = [i for i in range(len(l)) if l.startswith(k, i)]
            for i in res:
                occurences[i] = str(valid_digits[k])

    keys = list(occurences.keys())
    keys.sort()

    if len(keys) == 1:
        sum += int(occurences[keys[0]] + occurences[keys[0]])
    else:
        firstandlast = keys[::len(keys)-1]
        sum += int(occurences[firstandlast[0]] + occurences[firstandlast[1]])

print(sum)

f.close()