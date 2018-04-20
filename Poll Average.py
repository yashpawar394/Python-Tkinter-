NumSib = {}
Total = 0

while True:
  
  Start = input("Type your name or quit").lower()
  
  if len(Start) < 1:
    print("Please type a name or quit!")
    continue
  
  if Start != "quit":
    pass
  else:
    break
  
  if Start in NumSib:
    print("That name is already taken! Please type another name!")
    continue
  
  while True:
    SibNum = input("How many siblings do you have?")
    try:
      SibNum = int(SibNum)
      break
    except:
      print("Please type a number!")
      continue
    
  NumSib[Start] = SibNum
  
for i in NumSib:
  Total += NumSib[i]

if len(NumSib) != 0:
  print "The average number of siblings is:", (Total/(len(NumSib))), "Siblings"
  print(NumSib)
