import random 
list1=[1,2,3]
computer=random.choice(list1)
me=int(input("enter a integer from 1 to 3"))

if (computer==1) :
    if me==1:
        print("computer choses ROCK")
        print("i chooses ROCK")
    elif me==2:
        print("computer choses ROCK")
        print("i chooses paper")
    elif me==3:
        print("computer choses ROCK")
        print("i chooses sissor")
    
elif computer==2:
    if me==1:
        print("computer choses PAPER")
        print("i chooses ROCK")
    elif me==2:
        print("computer choses PAPER")
        print("i chooses PAPER")
    elif me==3:
        print("computer choses PAPER")
        print("i chooses sissor")    
        
elif computer==3:
    if me==1:
        print("computer choses SISSOR")
        print("i chooses ROCK")
    elif me==2:
        print("computer choses SISSOR")
        print("i chooses PAPER")
    elif me==3:
        print("computer choses SISSOR")
        print("i chooses SISSOR")  
a=[[None,1,2,3],
   [1,"D","W","L"],
   [2,"L","D","W"],
  [3,"W","L","D"]]
b=a[computer][me]
#print(b)
if b=="W":
    print("you won")
elif b=="L":
    print("you lose, computer wins")
else:
    print("no one win, match draw")

