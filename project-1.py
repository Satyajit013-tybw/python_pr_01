import random
computer=random.choice([-1,0,1])
youstr=input("Enter your choice: ")
youDict={"r":-1,"p":0,"s":1}
reverseDict={-1:"rock",0:"paper",1:"scissor"}
you=youDict[youstr]
print(f"Computer chose {reverseDict[computer]}\nyour choice is {reverseDict[you]}")
if you==computer:
    print("It's a tie")
else:
 if(you==1 and computer==0):
  print("You win")
 elif(you==-1 and computer==0): 
  print("Computer wins")
 elif(you==0 and computer==1):
  print("Computer wins")
 elif(you==-1 and computer==1):
  print("You win")
 elif(you==0 and computer==-1):
  print("You win")
 elif(you==1 and computer==-1):
  print("Computer wins")
 else:
  print("Invalid input")
