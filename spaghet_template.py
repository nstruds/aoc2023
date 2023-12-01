import os

f = open(os.path.dirname(os.path.realpath(__file__)) + "\input.txt", "r")
content = f.read()

print(content)

f.close()