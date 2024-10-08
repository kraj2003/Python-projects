def sum (a,b,c):
    return a+b+c
def printboard(Xstate,Zstate):
    zero='X' if Xstate[0] else ('O' if Zstate[0] else 0)
    one='X' if Xstate[1] else ('O' if Zstate[1] else 1)  
    two='X' if Xstate[2] else ('O' if Zstate[2] else 2)
    three='X' if Xstate[3] else ('O' if Zstate[3] else 3)
    four='X' if Xstate[4] else ('O' if Zstate[4] else 4)
    five='X' if Xstate[5] else ('O' if Zstate[5] else 5)
    six='X' if Xstate[6] else ('O' if Zstate[6] else 6)
    seven='X' if Xstate[7] else ('O' if Zstate[7] else 7)
    eight='X' if Xstate[8] else ('O' if Zstate[8] else 8)  
    print(f" {zero} |  {one}  |  {two}")
    print(f"---|-----|----")
    print(f" {three} | {four}   |  {five}")
    print(f"---|-----|----")
    print(f" {six} |  {seven} |  {eight}")
    print(f"---|-----|----")
# printboard()
def checkwin(xstate,zstate):
    xwins=[[0,1,2],[3,4,5],[6,7,8],[6,3,0],[7,4,1],[8,5,2],[0,4,8],[2,4,6]]
    for win in xwins:
        if(sum(xstate[win[0]],xstate[win[1]],xstate[win[2]])==3):
            print("x wins the match")
            return 1
        if(sum(zstate[win[0]],zstate[win[1]],zstate[win[2]])==3):
            print("owins the match")
            return 0
    return -1
if __name__ == "__main__":
    print("welcome to tic tac toe")
    xstate=[0,0,0,0,0,0,0,0,0]
    zstate=[0,0,0,0,0,0,0,0,0]
    turn=1 # i for the X and 0 for the O
    
    while(True):
        printboard(xstate,zstate)
        if turn==1:
            print("X's turn")
            value=int(input("enter a value:"))
            xstate[value]=1
            # printboard(xstate,zstate)
        else:
            print("Z's turn")
            value=int(input("enter a value"))
            zstate[value]=1
        check=checkwin(xstate,zstate)
        if(check!=-1):
            print("match over")
            break
        turn=1-turn