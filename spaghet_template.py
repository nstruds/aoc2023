import os

f = open(os.path.dirname(os.path.realpath(__file__)) + "\\input.txt", "r")
Lines = f.read().split('\n')
f.close()

print(Lines)
