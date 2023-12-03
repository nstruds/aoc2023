number = '795'
string = '...992.....#......=...../........701................508...*..578........................259...331.................795..945........79........'
index = 114


def is_standalone_number(number, string, index):
  startIndex = index
  endIndex = index+(len(str(number))-1)

  isStandalone = True

  if startIndex != 0:
      if string[startIndex-1].isdigit():
        return False

  if endIndex < len(string)-1:
      if string[endIndex+1].isdigit():
        return False

  return isStandalone

print(is_standalone_number(number,string,index))