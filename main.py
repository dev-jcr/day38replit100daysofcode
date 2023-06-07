
def colorChange(color)
  if letter.lower()=="b":
    print('\033[34m', end='')
  elif letter.lower()== "y":
    print('\033[33m', end='')
  elif letter.lower()== "p":
    print('\033[35m', end='')
  elif letter.lower()=="g":
    print('\033[32m', end='')
  elif letter.lower()=="r":
    print('\033[31m', end='')

sentence = input("Write a sentence:")
for letter in sentence:
  colorChange(letter.lower())
  print(letter, end="")
print()

