import ast

NumSib = {} # Dictionary
Total = 0

try:
  file = open("poll.txt", "r")
  filetext = file.read()
  NumSib = ast.literal_eval(filetext)
  file.close()
except:
  NumSib = {}



while True:
  
  Start = input("Type your name or quit").lower() # Key
  
  if len(Start) < 1:
    print("Please type a name or quit!")
    continue
  
  if Start == "quit":
    break
  
  if Start in NumSib:
    print("That name is already taken! Please type another name!")
    continue
  
  while True:
    SibNum = input("How many siblings do you have?") #Value
    try:
      SibNum = int(SibNum)
      break
    except:
      print("Please type a number!")
      continue
    
  NumSib[Start] = SibNum
  
  file = open("poll.txt", "w")
  file.write(str(NumSib))
  file.close()

for i in NumSib:
  Total += NumSib[i]

if len(NumSib) != 0:
  print( ("Average"), (Total/(len(NumSib))), "Siblings")
  print(NumSib)
  
