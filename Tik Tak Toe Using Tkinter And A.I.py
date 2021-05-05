from tkinter import *
from tkinter import messagebox

def callback1(r,c):
    global player,count,states,b,stop_game
    if player=="X" and states[r][c]==0 and stop_game==False:
        b[r][c].configure(text="X",fg="black",bg="green")
        states[r][c]="X"
        player="O"
        count += 1
        check_for_winner()
        callback1(1,1)
        
    elif player=="O" and stop_game==False:
        def pc1():
            global count,player,states,b,stop_game
            if  states[1][1] == 0 and stop_game==False:
                b[1][1].configure(text="O",fg="green",bg="black")
                states[1][1] = "O"
                player = "X"
                count += 1
                check_for_winner()
            elif states[0][1] == "X" and states[0][2] == "X" and states[0][0]== 0 :
                b[0][0].configure(text="O",fg="green",bg="black")
                states[0][0] = "O"
                player = "X"
                count += 1
                check_for_winner()
            elif states[1][0] == "X" and states[2][0] == "X" and states[0][0]== 0 :
                b[0][0].configure(text="O",fg="green",bg="black")
                states[0][0] = "O"
                player = "X"
                count += 1
                check_for_winner()
            elif states[0][0] == "X" and states[1][1] == "X" and states[2][2] == 0 :
                b[2][2].configure(text="O",fg="green",bg="black")
                states[2][2] = "O"
                player = "X"
                count += 1
                check_for_winner()
            elif states[2][2] == "X" and states[1][1] == "X" and states[0][0]==0:
                b[0][0].configure(text="O",fg="green",bg="black")
                states[0][0] = "O"
                player = "X"
                count += 1
                check_for_winner()
            elif states[2][0] == "X" and states[1][1] == "X" and states[0][2]==0 :
                b[0][2].configure(text="O",fg="green",bg="black")
                states[0][2] = "O"
                player = "X"
                count += 1
                check_for_winner()
            elif states[0][2] == "X" and states[1][1] == "X" and states[2][0]==0:
                b[2][0].configure(text="O",fg="green",bg="black")
                states[2][0] = "O"
                player = "X"
                count += 1
                check_for_winner()


                
            elif states[0][1] == "X" and states[1][1] == "X" and states[2][1]==0:
                b[2][1].configure(text="O",fg="green",bg="black")
                states[2][1] = "O"
                player = "X"
                count += 1
                check_for_winner()
            elif states[2][1] == "X" and states[1][1] == "X" and states[0][1]==0:
                b[0][1].configure(text="O",fg="green",bg="black")
                states[0][1] = "O"
                player = "X"
                count += 1
                check_for_winner()
            elif states[1][0] == "X" and states[1][1] == "X" and states[1][2]==0:
                b[1][2].configure(text="O",fg="green",bg="black")
                states[1][2] = "O"
                player = "X"
                count += 1
                check_for_winner()
            elif states[1][2] == "X" and states[1][1] == "X" and states[1][0]==0:
                b[1][0].configure(text="O",fg="green",bg="black")
                states[1][0] = "O"
                player = "X"
                count += 1
                check_for_winner()

                
            elif states[0][0]== "X" and stop_game==False:#00edge
                if states[0][2] == "X" and states[0][1] == 0  :
                    b[0][1].configure(text="O",fg="green",bg="black")
                    states[0][1] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[2][0] == "X" and states[1][0] == 0 :
                    b[1][0].configure(text="O",fg="green",bg="black")
                    states[1][0] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[0][2] == "X" and states[0][1] == 0 and states[0][0]=="X" :
                    b[0][1].configure(text="O",fg="green",bg="black")
                    states[0][1] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[2][0] == "X" and states[1][0] == 0 and states[0][0]=="X":
                    b[1][0].configure(text="O",fg="green",bg="black")
                    states[1][0] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[0][0] == "X" and states[0][1] == 0  and states[0][2]=="X":
                    b[0][1].configure(text="O",fg="green",bg="black")
                    states[0][1] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[2][2] == "X" and states[1][2] == 0 and states[0][2]=="X" :
                    b[1][2].configure(text="O",fg="green",bg="black")
                    states[1][2] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                
                

                elif states[0][0] == "X" and states[1][0] == 0 and states[2][0]=="X" :
                    b[1][0].configure(text="O",fg="green",bg="black")
                    states[1][0] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[2][2] == "X" and states[2][1] == 0 and states[2][0]=="X":
                    b[2][1].configure(text="O",fg="green",bg="black")
                    states[2][1] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[2][0] == "X" and states[2][1] == 0 and states[2][2]==0 :
                    b[2][1].configure(text="O",fg="green",bg="black")
                    states[2][1] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[0][2] == "X" and states[1][2] == 0 and states[2][2]==0:
                    b[1][2].configure(text="O",fg="green",bg="black")
                    states[1][2] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()




                elif states[0][0] == "X" and states[1][1] == "X" and states[2][2] == 0 :
                    b[2][2].configure(text="O",fg="green",bg="black")
                    states[2][2] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[2][2] == "X" and states[1][1] == "X" and states[0][0]==0:
                    b[0][0].configure(text="O",fg="green",bg="black")
                    states[0][0] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[2][0] == "X" and states[1][1] == "X" and states[0][2]==0 :
                    b[0][2].configure(text="O",fg="green",bg="black")
                    states[0][2] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[0][2] == "X" and states[1][1] == "X" and states[2][0]==0:
                    b[2][0].configure(text="O",fg="green",bg="black")
                    states[2][0] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()


                    
                elif states[0][1] == "X" and states[1][1] == "X" and states[2][1]==0:
                    b[2][1].configure(text="O",fg="green",bg="black")
                    states[2][1] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[2][1] == "X" and states[1][1] == "X" and states[0][1]==0:
                    b[0][1].configure(text="O",fg="green",bg="black")
                    states[0][1] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[1][0] == "X" and states[1][1] == "X" and states[1][2]==0:
                    b[1][2].configure(text="O",fg="green",bg="black")
                    states[1][2] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[1][2] == "X" and states[1][1] == "X" and states[1][0]==0:
                    b[1][0].configure(text="O",fg="green",bg="black")
                    states[1][0] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()

                
                
                elif states[0][2] == 0 and states[0][1] == "X" :
                    b[0][2].configure(text="O",fg="green",bg="black")
                    states[0][2] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[2][0] == 0 and states[1][0] == "X":
                    b[2][0].configure(text="O",fg="green",bg="black")
                    states[2][0] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[0][1] == 0 and states[0][2] == "X":
                    b[0][1].configure(text="O",fg="green",bg="black")
                    states[0][1] = "O"
                    player="X"
                    count += 1
                    check_for_winner()
                elif states[1][0]==0 and states[2][0] == "X":
                    b[1][0].configure(text="O",fg="green",bg="black")
                    states[1][0] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()

                elif states[2][0]==0 :
                    b[2][0].configure(text="O",fg="green",bg="black")
                    states[2][0] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[0][2]==0 :
                    b[0][2].configure(text="O",fg="green",bg="black")
                    states[0][2] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                
                elif states[2][2]== "X" and stop_game==False:#22edge
                    if states[2][0] == 0 and states[2][1] == "X" :
                        b[2][0].configure(text="O",fg="green",bg="black")
                        states[2][0] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[2][0] == "X" and states[2][1] == 0:
                        b[2][1].configure(text="O",fg="green",bg="black")
                        states[2][1] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[0][2] == 0 and states[1][2] == "X":
                        b[0][2].configure(text="O",fg="green",bg="black")
                        states[0][2] = "O"
                        player="X"
                        count += 1
                        check_for_winner()
                    elif states[0][2]=="X" and states[1][2] == 0:
                        b[1][2].configure(text="O",fg="green",bg="black")
                        states[1][2] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[0][0] == 0:
                        b[0][0].configure(text="O",fg="green",bg="black")
                        states[0][0] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[0][2] == 0:
                        b[0][2].configure(text="O",fg="green",bg="black")
                        states[0][2] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[2][0] == 0:
                        b[2][0].configure(text="O",fg="green",bg="black")
                        states[2][0] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[2][2] == 0:
                        b[2][2].configure(text="O",fg="green",bg="black")
                        states[2][2] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                elif states[1][0] == "X":#10middle
                    if states[1][2] == 0:
                        b[1][2].configure(text="O",fg="green",bg="black")
                        states[1][2] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    
                    elif states[0][0] == 0:
                        b[0][0].configure(text="O",fg="green",bg="black")
                        states[0][0] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[2][0] == 0:
                        b[2][0].configure(text="O",fg="green",bg="black")
                        states[2][0] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[0][2] == 0:
                        b[0][2].configure(text="O",fg="green",bg="black")
                        states[0][2] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[2][2] == 0:
                        b[2][2].configure(text="O",fg="green",bg="black")
                        states[2][2] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[0][1] == 0:
                        b[0][1].configure(text="O",fg="green",bg="black")
                        states[0][1] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[2][1] == 0:
                        b[2][1].configure(text="O",fg="green",bg="black")
                        states[2][1] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                elif states[1][2] == "X":#12middle
                    if states[1][0] == 0:
                        b[1][0].configure(text="O",fg="green",bg="black")
                        states[1][0] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    
                    elif states[0][2] == 0:
                        b[0][2].configure(text="O",fg="green",bg="black")
                        states[0][2] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[2][2] == 0:
                        b[2][2].configure(text="O",fg="green",bg="black")
                        states[2][2] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[0][0] == 0:
                        b[0][0].configure(text="O",fg="green",bg="black")
                        states[0][0] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[2][0] == 0:
                        b[2][0].configure(text="O",fg="green",bg="black")
                        states[2][0] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[0][1] == 0:
                        b[0][1].configure(text="O",fg="green",bg="black")
                        states[0][1] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[2][1] == 0:
                        b[2][1].configure(text="O",fg="green",bg="black")
                        states[2][1] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                elif states[0][1] == "X":#01middle
                    if states[2][1] == 0:
                        b[2][1].configure(text="O",fg="green",bg="black")
                        states[2][1] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    
                    elif states[0][0] == 0:
                        b[0][0].configure(text="O",fg="green",bg="black")
                        states[0][0] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[0][2] == 0:
                        b[0][2].configure(text="O",fg="green",bg="black")
                        states[0][2] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[2][0] == 0:
                        b[2][0].configure(text="O",fg="green",bg="black")
                        states[2][0] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[2][2] == 0:
                        b[2][2].configure(text="O",fg="green",bg="black")
                        states[2][2] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[1][0] == 0:
                        b[1][0].configure(text="O",fg="green",bg="black")
                        states[1][0] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[1][2] == 0:
                        b[1][2].configure(text="O",fg="green",bg="black")
                        states[1][2] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                elif states[2][1] == "X":#21middle
                    if states[0][1] == 0:
                        b[0][1].configure(text="O",fg="green",bg="black")
                        states[0][1] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    
                    elif states[2][0] == 0:
                        b[2][0].configure(text="O",fg="green",bg="black")
                        states[2][0] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[2][2] == 0:
                        b[2][2].configure(text="O",fg="green",bg="black")
                        states[2][2] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[0][0] == 0:
                        b[0][0].configure(text="O",fg="green",bg="black")
                        states[0][0] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[0][2] == 0:
                        b[0][2].configure(text="O",fg="green",bg="black")
                        states[0][2] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[1][0] == 0:
                        b[1][0].configure(text="O",fg="green",bg="black")
                        states[1][0] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[1][2] == 0:
                        b[1][2].configure(text="O",fg="green",bg="black")
                        states[1][2] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()

                    
                    
                
            elif states[0][2]== "X" and stop_game==False:#02edge
                if states[0][0] == "X" and states[0][1] == 0  :
                    b[0][1].configure(text="O",fg="green",bg="black")
                    states[0][1] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[2][2] == "X" and states[1][2] == 0 :
                    b[1][2].configure(text="O",fg="green",bg="black")
                    states[1][2] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()


                elif states[0][2] == "X" and states[0][1] == 0 and states[0][0]=="X" :
                    b[0][1].configure(text="O",fg="green",bg="black")
                    states[0][1] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[2][0] == "X" and states[1][0] == 0 and states[0][0]=="X":
                    b[1][0].configure(text="O",fg="green",bg="black")
                    states[1][0] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[0][0] == "X" and states[0][1] == 0  and states[0][2]=="X":
                    b[0][1].configure(text="O",fg="green",bg="black")
                    states[0][1] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[2][2] == "X" and states[1][2] == 0 and states[0][2]=="X" :
                    b[1][2].configure(text="O",fg="green",bg="black")
                    states[1][2] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()

                elif states[0][0] == "X" and states[1][0] == 0 and states[2][0]=="X" :
                    b[1][0].configure(text="O",fg="green",bg="black")
                    states[1][0] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[2][2] == "X" and states[2][1] == 0 and states[2][0]=="X":
                    b[2][1].configure(text="O",fg="green",bg="black")
                    states[2][1] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[2][0] == "X" and states[2][1] == 0 and states[2][2]==0 :
                    b[2][1].configure(text="O",fg="green",bg="black")
                    states[2][1] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[0][2] == "X" and states[1][2] == 0 and states[2][2]==0:
                    b[1][2].configure(text="O",fg="green",bg="black")
                    states[1][2] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()




                elif states[0][0] == "X" and states[1][1] == "X" and states[2][2] == 0 :
                    b[2][2].configure(text="O",fg="green",bg="black")
                    states[2][2] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[2][2] == "X" and states[1][1] == "X" and states[0][0]==0:
                    b[0][0].configure(text="O",fg="green",bg="black")
                    states[0][0] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[2][0] == "X" and states[1][1] == "X" and states[0][2]==0 :
                    b[0][2].configure(text="O",fg="green",bg="black")
                    states[0][2] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[0][2] == "X" and states[1][1] == "X" and states[2][0]==0:
                    b[2][0].configure(text="O",fg="green",bg="black")
                    states[2][0] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()


                    
                elif states[0][1] == "X" and states[1][1] == "X" and states[2][1]==0:
                    b[2][1].configure(text="O",fg="green",bg="black")
                    states[2][1] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[2][1] == "X" and states[1][1] == "X" and states[0][1]==0:
                    b[0][1].configure(text="O",fg="green",bg="black")
                    states[0][1] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[1][0] == "X" and states[1][1] == "X" and states[1][2]==0:
                    b[1][2].configure(text="O",fg="green",bg="black")
                    states[1][2] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[1][2] == "X" and states[1][1] == "X" and states[1][0]==0:
                    b[1][0].configure(text="O",fg="green",bg="black")
                    states[1][0] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()

                
                
                elif states[0][0] == 0 and states[0][1] == "X" :
                    b[0][0].configure(text="O",fg="green",bg="black")
                    states[0][0] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[2][2] == 0 and states[1][2] == "X":
                    b[2][2].configure(text="O",fg="green",bg="black")
                    states[2][2] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[0][1] == 0 and states[0][0] == "X":
                    b[0][1].configure(text="O",fg="green",bg="black")
                    states[0][1] = "O"
                    player="X"
                    count += 1
                    check_for_winner()
                elif states[1][2]==0 and states[2][2] == "X":
                    b[1][2].configure(text="O",fg="green",bg="black")
                    states[1][2] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[0][0]==0 :
                    b[0][0].configure(text="O",fg="green",bg="black")
                    states[0][0] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[2][2]==0 :
                    b[2][2].configure(text="O",fg="green",bg="black")
                    states[2][2] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[2][0]== "X" and stop_game==False:#20edge
                    if states[0][0] == 0 and states[1][0] == "X" :
                        b[0][0].configure(text="O",fg="green",bg="black")
                        states[0][0] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[1][0] == 0 and states[0][0] == "X":
                        b[1][0].configure(text="O",fg="green",bg="black")
                        states[1][0] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[2][2] == 0 and states[2][1] == "X":
                        b[2][2].configure(text="O",fg="green",bg="black")
                        states[2][2] = "O"
                        player="X"
                        count += 1
                        check_for_winner()
                    elif states[2][1]==0 and states[2][2] == "X":
                        b[2][1].configure(text="O",fg="green",bg="black")
                        states[2][1] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[0][0] == 0:
                        b[0][0].configure(text="O",fg="green",bg="black")
                        states[0][0] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[0][2] == 0:
                        b[0][2].configure(text="O",fg="green",bg="black")
                        states[0][2] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[2][0] == 0:
                        b[2][0].configure(text="O",fg="green",bg="black")
                        states[2][0] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[2][2] == 0:
                        b[2][2].configure(text="O",fg="green",bg="black")
                        states[2][2] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                
                elif states[1][0] == "X":#10middle
                    if states[1][2] == 0:
                        b[1][2].configure(text="O",fg="green",bg="black")
                        states[1][2] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    
                    elif states[0][0] == 0:
                        b[0][0].configure(text="O",fg="green",bg="black")
                        states[0][0] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[2][0] == 0:
                        b[2][0].configure(text="O",fg="green",bg="black")
                        states[2][0] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[0][2] == 0:
                        b[0][2].configure(text="O",fg="green",bg="black")
                        states[0][2] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[2][2] == 0:
                        b[2][2].configure(text="O",fg="green",bg="black")
                        states[2][2] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[0][1] == 0:
                        b[0][1].configure(text="O",fg="green",bg="black")
                        states[0][1] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[2][1] == 0:
                        b[2][1].configure(text="O",fg="green",bg="black")
                        states[2][1] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                elif states[1][2] == "X":#12middle
                    if states[1][0] == 0:
                        b[1][0].configure(text="O",fg="green",bg="black")
                        states[1][0] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    
                    elif states[0][2] == 0:
                        b[0][2].configure(text="O",fg="green",bg="black")
                        states[0][2] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[2][2] == 0:
                        b[2][2].configure(text="O",fg="green",bg="black")
                        states[2][2] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[0][0] == 0:
                        b[0][0].configure(text="O",fg="green",bg="black")
                        states[0][0] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[2][0] == 0:
                        b[2][0].configure(text="O",fg="green",bg="black")
                        states[2][0] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[0][1] == 0:
                        b[0][1].configure(text="O",fg="green",bg="black")
                        states[0][1] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[2][1] == 0:
                        b[2][1].configure(text="O",fg="green",bg="black")
                        states[2][1] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                elif states[0][1] == "X":#01middle
                    if states[2][1] == 0:
                        b[2][1].configure(text="O",fg="green",bg="black")
                        states[2][1] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    
                    elif states[0][0] == 0:
                        b[0][0].configure(text="O",fg="green",bg="black")
                        states[0][0] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[0][2] == 0:
                        b[0][2].configure(text="O",fg="green",bg="black")
                        states[0][2] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[2][0] == 0:
                        b[2][0].configure(text="O",fg="green",bg="black")
                        states[2][0] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[2][2] == 0:
                        b[2][2].configure(text="O",fg="green",bg="black")
                        states[2][2] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[1][0] == 0:
                        b[1][0].configure(text="O",fg="green",bg="black")
                        states[1][0] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[1][2] == 0:
                        b[1][2].configure(text="O",fg="green",bg="black")
                        states[1][2] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                elif states[2][1] == "X":#21middle
                    if states[0][1] == 0:
                        b[0][1].configure(text="O",fg="green",bg="black")
                        states[0][1] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    
                    elif states[2][0] == 0:
                        b[2][0].configure(text="O",fg="green",bg="black")
                        states[2][0] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[2][2] == 0:
                        b[2][2].configure(text="O",fg="green",bg="black")
                        states[2][2] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[0][0] == 0:
                        b[0][0].configure(text="O",fg="green",bg="black")
                        states[0][0] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[0][2] == 0:
                        b[0][2].configure(text="O",fg="green",bg="black")
                        states[0][2] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[1][0] == 0:
                        b[1][0].configure(text="O",fg="green",bg="black")
                        states[1][0] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[1][2] == 0:
                        b[1][2].configure(text="O",fg="green",bg="black")
                        states[1][2] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()

            elif states[2][0]== "X" and stop_game==False:#20edge
                if states[0][0] == "X" and states[1][0] == 0  :
                    b[1][0].configure(text="O",fg="green",bg="black")
                    states[1][0] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[2][2] == "X" and states[2][1] == 0 :
                    b[2][1].configure(text="O",fg="green",bg="black")
                    states[2][1] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                

                elif states[0][2] == "X" and states[0][1] == 0 and states[0][0]=="X" :
                    b[0][1].configure(text="O",fg="green",bg="black")
                    states[0][1] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[2][0] == "X" and states[1][0] == 0 and states[0][0]=="X":
                    b[1][0].configure(text="O",fg="green",bg="black")
                    states[1][0] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[0][0] == "X" and states[0][1] == 0  and states[0][2]=="X":
                    b[0][1].configure(text="O",fg="green",bg="black")
                    states[0][1] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[2][2] == "X" and states[1][2] == 0 and states[0][2]=="X" :
                    b[1][2].configure(text="O",fg="green",bg="black")
                    states[1][2] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()

                elif states[0][0] == "X" and states[1][0] == 0 and states[2][0]=="X" :
                    b[1][0].configure(text="O",fg="green",bg="black")
                    states[1][0] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[2][2] == "X" and states[2][1] == 0 and states[2][0]=="X":
                    b[2][1].configure(text="O",fg="green",bg="black")
                    states[2][1] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[2][0] == "X" and states[2][1] == 0 and states[2][2]==0 :
                    b[2][1].configure(text="O",fg="green",bg="black")
                    states[2][1] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[0][2] == "X" and states[1][2] == 0 and states[2][2]==0:
                    b[1][2].configure(text="O",fg="green",bg="black")
                    states[1][2] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()




                elif states[0][0] == "X" and states[1][1] == "X" and states[2][2] == 0 :
                    b[2][2].configure(text="O",fg="green",bg="black")
                    states[2][2] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[2][2] == "X" and states[1][1] == "X" and states[0][0]==0:
                    b[0][0].configure(text="O",fg="green",bg="black")
                    states[0][0] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[2][0] == "X" and states[1][1] == "X" and states[0][2]==0 :
                    b[0][2].configure(text="O",fg="green",bg="black")
                    states[0][2] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[0][2] == "X" and states[1][1] == "X" and states[2][0]==0:
                    b[2][0].configure(text="O",fg="green",bg="black")
                    states[2][0] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()


                    
                elif states[0][1] == "X" and states[1][1] == "X" and states[2][1]==0:
                    b[2][1].configure(text="O",fg="green",bg="black")
                    states[2][1] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[2][1] == "X" and states[1][1] == "X" and states[0][1]==0:
                    b[0][1].configure(text="O",fg="green",bg="black")
                    states[0][1] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[1][0] == "X" and states[1][1] == "X" and states[1][2]==0:
                    b[1][2].configure(text="O",fg="green",bg="black")
                    states[1][2] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[1][2] == "X" and states[1][1] == "X" and states[1][0]==0:
                    b[1][0].configure(text="O",fg="green",bg="black")
                    states[1][0] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()

                


                elif states[0][0] == 0 and states[1][0] == "X" :
                    b[0][0].configure(text="O",fg="green",bg="black")
                    states[0][0] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[1][0] == 0 and states[0][0] == "X":
                    b[1][0].configure(text="O",fg="green",bg="black")
                    states[1][0] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[2][2] == 0 and states[2][1] == "X":
                    b[2][2].configure(text="O",fg="green",bg="black")
                    states[2][2] = "O"
                    player="X"
                    count += 1
                    check_for_winner()
                elif states[2][1]==0 and states[2][2] == "X":
                    b[2][1].configure(text="O",fg="green",bg="black")
                    states[2][1] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[0][0]==0 :
                    b[0][0].configure(text="O",fg="green",bg="black")
                    states[0][0] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[2][2]==0 :
                    b[2][2].configure(text="O",fg="green",bg="black")
                    states[2][2] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[0][2]== "X" and stop_game==False:#02edge
                    if states[0][0] == 0 and states[0][1] == "X" :
                        b[0][0].configure(text="O",fg="green",bg="black")
                        states[0][0] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[2][2] == 0 and states[1][2] == "X":
                        b[2][2].configure(text="O",fg="green",bg="black")
                        states[2][2] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[0][1] == 0 and states[0][0] == "X":
                        b[0][1].configure(text="O",fg="green",bg="black")
                        states[0][1] = "O"
                        player="X"
                        count += 1
                        check_for_winner()
                    elif states[1][2]==0 and states[2][2] == "X":
                        b[1][2].configure(text="O",fg="green",bg="black")
                        states[1][2] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[0][0] == 0:
                        b[0][0].configure(text="O",fg="green",bg="black")
                        states[0][0] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[0][2] == 0:
                        b[0][2].configure(text="O",fg="green",bg="black")
                        states[0][2] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[2][0] == 0:
                        b[2][0].configure(text="O",fg="green",bg="black")
                        states[2][0] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[2][2] == 0:
                        b[2][2].configure(text="O",fg="green",bg="black")
                        states[2][2] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                elif states[1][0] == "X":#10middle
                    if states[1][2] == 0:
                        b[1][2].configure(text="O",fg="green",bg="black")
                        states[1][2] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    
                    elif states[0][0] == 0:
                        b[0][0].configure(text="O",fg="green",bg="black")
                        states[0][0] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[2][0] == 0:
                        b[2][0].configure(text="O",fg="green",bg="black")
                        states[2][0] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[0][2] == 0:
                        b[0][2].configure(text="O",fg="green",bg="black")
                        states[0][2] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[2][2] == 0:
                        b[2][2].configure(text="O",fg="green",bg="black")
                        states[2][2] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[0][1] == 0:
                        b[0][1].configure(text="O",fg="green",bg="black")
                        states[0][1] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[2][1] == 0:
                        b[2][1].configure(text="O",fg="green",bg="black")
                        states[2][1] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                elif states[1][2] == "X":#12middle
                    if states[1][0] == 0:
                        b[1][0].configure(text="O",fg="green",bg="black")
                        states[1][0] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    
                    elif states[0][2] == 0:
                        b[0][2].configure(text="O",fg="green",bg="black")
                        states[0][2] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[2][2] == 0:
                        b[2][2].configure(text="O",fg="green",bg="black")
                        states[2][2] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[0][0] == 0:
                        b[0][0].configure(text="O",fg="green",bg="black")
                        states[0][0] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[2][0] == 0:
                        b[2][0].configure(text="O",fg="green",bg="black")
                        states[2][0] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[0][1] == 0:
                        b[0][1].configure(text="O",fg="green",bg="black")
                        states[0][1] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[2][1] == 0:
                        b[2][1].configure(text="O",fg="green",bg="black")
                        states[2][1] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                elif states[0][1] == "X":#01middle
                    if states[2][1] == 0:
                        b[2][1].configure(text="O",fg="green",bg="black")
                        states[2][1] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    
                    elif states[0][0] == 0:
                        b[0][0].configure(text="O",fg="green",bg="black")
                        states[0][0] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[0][2] == 0:
                        b[0][2].configure(text="O",fg="green",bg="black")
                        states[0][2] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[2][0] == 0:
                        b[2][0].configure(text="O",fg="green",bg="black")
                        states[2][0] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[2][2] == 0:
                        b[2][2].configure(text="O",fg="green",bg="black")
                        states[2][2] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[1][0] == 0:
                        b[1][0].configure(text="O",fg="green",bg="black")
                        states[1][0] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[1][2] == 0:
                        b[1][2].configure(text="O",fg="green",bg="black")
                        states[1][2] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                elif states[2][1] == "X":#21middle
                    if states[0][1] == 0:
                        b[0][1].configure(text="O",fg="green",bg="black")
                        states[0][1] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    
                    elif states[2][0] == 0:
                        b[2][0].configure(text="O",fg="green",bg="black")
                        states[2][0] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[2][2] == 0:
                        b[2][2].configure(text="O",fg="green",bg="black")
                        states[2][2] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[0][0] == 0:
                        b[0][0].configure(text="O",fg="green",bg="black")
                        states[0][0] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[0][2] == 0:
                        b[0][2].configure(text="O",fg="green",bg="black")
                        states[0][2] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[1][0] == 0:
                        b[1][0].configure(text="O",fg="green",bg="black")
                        states[1][0] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[1][2] == 0:
                        b[1][2].configure(text="O",fg="green",bg="black")
                        states[1][2] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()



            elif states[2][2]== "X" and stop_game==False:#22edge
                if states[2][0] == "X" and states[2][1] == 0  :
                    b[2][1].configure(text="O",fg="green",bg="black")
                    states[2][1] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[0][2] == "X" and states[1][2] == 0 :
                    b[1][2].configure(text="O",fg="green",bg="black")
                    states[1][2] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()



                elif states[0][2] == "X" and states[0][1] == 0 and states[0][0]=="X" :
                    b[0][1].configure(text="O",fg="green",bg="black")
                    states[0][1] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[2][0] == "X" and states[1][0] == 0 and states[0][0]=="X":
                    b[1][0].configure(text="O",fg="green",bg="black")
                    states[1][0] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[0][0] == "X" and states[0][1] == 0  and states[0][2]=="X":
                    b[0][1].configure(text="O",fg="green",bg="black")
                    states[0][1] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[2][2] == "X" and states[1][2] == 0 and states[0][2]=="X" :
                    b[1][2].configure(text="O",fg="green",bg="black")
                    states[1][2] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()

                elif states[0][0] == "X" and states[1][0] == 0 and states[2][0]=="X" :
                    b[1][0].configure(text="O",fg="green",bg="black")
                    states[1][0] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[2][2] == "X" and states[2][1] == 0 and states[2][0]=="X":
                    b[2][1].configure(text="O",fg="green",bg="black")
                    states[2][1] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[2][0] == "X" and states[2][1] == 0 and states[2][2]==0 :
                    b[2][1].configure(text="O",fg="green",bg="black")
                    states[2][1] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[0][2] == "X" and states[1][2] == 0 and states[2][2]==0:
                    b[1][2].configure(text="O",fg="green",bg="black")
                    states[1][2] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()




                elif states[0][0] == "X" and states[1][1] == "X" and states[2][2] == 0 :
                    b[2][2].configure(text="O",fg="green",bg="black")
                    states[2][2] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[2][2] == "X" and states[1][1] == "X" and states[0][0]==0:
                    b[0][0].configure(text="O",fg="green",bg="black")
                    states[0][0] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[2][0] == "X" and states[1][1] == "X" and states[0][2]==0 :
                    b[0][2].configure(text="O",fg="green",bg="black")
                    states[0][2] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[0][2] == "X" and states[1][1] == "X" and states[2][0]==0:
                    b[2][0].configure(text="O",fg="green",bg="black")
                    states[2][0] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()


                    
                elif states[0][1] == "X" and states[1][1] == "X" and states[2][1]==0:
                    b[2][1].configure(text="O",fg="green",bg="black")
                    states[2][1] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[2][1] == "X" and states[1][1] == "X" and states[0][1]==0:
                    b[0][1].configure(text="O",fg="green",bg="black")
                    states[0][1] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[1][0] == "X" and states[1][1] == "X" and states[1][2]==0:
                    b[1][2].configure(text="O",fg="green",bg="black")
                    states[1][2] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[1][2] == "X" and states[1][1] == "X" and states[1][0]==0:
                    b[1][0].configure(text="O",fg="green",bg="black")
                    states[1][0] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()


                

                elif states[2][0] == 0 and states[2][1] == "X" :
                    b[2][0].configure(text="O",fg="green",bg="black")
                    states[2][0] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[2][0] == "X" and states[2][1] == 0:
                    b[2][1].configure(text="O",fg="green",bg="black")
                    states[2][1] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[0][2] == 0 and states[1][2] == "X":
                    b[0][2].configure(text="O",fg="green",bg="black")
                    states[0][2] = "O"
                    player="X"
                    count += 1
                    check_for_winner()
                elif states[0][2]=="X" and states[1][2] == 0:
                    b[1][2].configure(text="O",fg="green",bg="black")
                    states[1][2] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[2][0]==0 :
                    b[2][0].configure(text="O",fg="green",bg="black")
                    states[2][0] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[0][2]==0 :
                    b[0][2].configure(text="O",fg="green",bg="black")
                    states[0][2] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[0][0]== "X" and stop_game==False:#00edge
                    if states[0][2] == 0 and states[0][1] == "X" :
                        b[0][2].configure(text="O",fg="green",bg="black")
                        states[0][2] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[2][0] == 0 and states[1][0] == "X":
                        b[2][0].configure(text="O",fg="green",bg="black")
                        states[2][0] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[0][1] == 0 and states[0][2] == "X":
                        b[0][1].configure(text="O",fg="green",bg="black")
                        states[0][1] = "O"
                        player="X"
                        count += 1
                        check_for_winner()
                    elif states[1][0]==0 and states[2][0] == "X":
                        b[1][0].configure(text="O",fg="green",bg="black")
                        states[1][0] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[0][0] == 0:
                        b[0][0].configure(text="O",fg="green",bg="black")
                        states[0][0] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[0][2] == 0:
                        b[0][2].configure(text="O",fg="green",bg="black")
                        states[0][2] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[2][0] == 0:
                        b[2][0].configure(text="O",fg="green",bg="black")
                        states[2][0] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[2][2] == 0:
                        b[2][2].configure(text="O",fg="green",bg="black")
                        states[2][2] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    
                elif states[1][0] == "X":#10middle
                    if states[1][2] == 0:
                        b[1][2].configure(text="O",fg="green",bg="black")
                        states[1][2] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    
                    elif states[0][0] == 0:
                        b[0][0].configure(text="O",fg="green",bg="black")
                        states[0][0] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[2][0] == 0:
                        b[2][0].configure(text="O",fg="green",bg="black")
                        states[2][0] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[0][2] == 0:
                        b[0][2].configure(text="O",fg="green",bg="black")
                        states[0][2] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[2][2] == 0:
                        b[2][2].configure(text="O",fg="green",bg="black")
                        states[2][2] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[0][1] == 0:
                        b[0][1].configure(text="O",fg="green",bg="black")
                        states[0][1] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[2][1] == 0:
                        b[2][1].configure(text="O",fg="green",bg="black")
                        states[2][1] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                elif states[1][2] == "X":#12middle
                    if states[1][0] == 0:
                        b[1][0].configure(text="O",fg="green",bg="black")
                        states[1][0] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    
                    elif states[0][2] == 0:
                        b[0][2].configure(text="O",fg="green",bg="black")
                        states[0][2] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[2][2] == 0:
                        b[2][2].configure(text="O",fg="green",bg="black")
                        states[2][2] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[0][0] == 0:
                        b[0][0].configure(text="O",fg="green",bg="black")
                        states[0][0] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[2][0] == 0:
                        b[2][0].configure(text="O",fg="green",bg="black")
                        states[2][0] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[0][1] == 0:
                        b[0][1].configure(text="O",fg="green",bg="black")
                        states[0][1] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[2][1] == 0:
                        b[2][1].configure(text="O",fg="green",bg="black")
                        states[2][1] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                elif states[0][1] == "X":#01middle
                    if states[2][1] == 0:
                        b[2][1].configure(text="O",fg="green",bg="black")
                        states[2][1] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    
                    elif states[0][0] == 0:
                        b[0][0].configure(text="O",fg="green",bg="black")
                        states[0][0] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[0][2] == 0:
                        b[0][2].configure(text="O",fg="green",bg="black")
                        states[0][2] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[2][0] == 0:
                        b[2][0].configure(text="O",fg="green",bg="black")
                        states[2][0] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[2][2] == 0:
                        b[2][2].configure(text="O",fg="green",bg="black")
                        states[2][2] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[1][0] == 0:
                        b[1][0].configure(text="O",fg="green",bg="black")
                        states[1][0] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[1][2] == 0:
                        b[1][2].configure(text="O",fg="green",bg="black")
                        states[1][2] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                elif states[2][1] == "X":#21middle
                    if states[0][1] == 0:
                        b[0][1].configure(text="O",fg="green",bg="black")
                        states[0][1] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    
                    elif states[2][0] == 0:
                        b[2][0].configure(text="O",fg="green",bg="black")
                        states[2][0] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[2][2] == 0:
                        b[2][2].configure(text="O",fg="green",bg="black")
                        states[2][2] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[0][0] == 0:
                        b[0][0].configure(text="O",fg="green",bg="black")
                        states[0][0] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[0][2] == 0:
                        b[0][2].configure(text="O",fg="green",bg="black")
                        states[0][2] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[1][0] == 0:
                        b[1][0].configure(text="O",fg="green",bg="black")
                        states[1][0] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                    elif states[1][2] == 0:
                        b[1][2].configure(text="O",fg="green",bg="black")
                        states[1][2] = "O"
                        player = "X"
                        count += 1
                        check_for_winner()
                
            elif states[1][0] == "X":#10middle
                if states[1][2] == 0:
                    b[1][2].configure(text="O",fg="green",bg="black")
                    states[1][2] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                
                elif states[0][0] == 0:
                    b[0][0].configure(text="O",fg="green",bg="black")
                    states[0][0] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[2][0] == 0:
                    b[2][0].configure(text="O",fg="green",bg="black")
                    states[2][0] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[0][2] == 0:
                    b[0][2].configure(text="O",fg="green",bg="black")
                    states[0][2] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[2][2] == 0:
                    b[2][2].configure(text="O",fg="green",bg="black")
                    states[2][2] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[0][1] == 0:
                    b[0][1].configure(text="O",fg="green",bg="black")
                    states[0][1] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[2][1] == 0:
                    b[2][1].configure(text="O",fg="green",bg="black")
                    states[2][1] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
            elif states[1][2] == "X":#12middle
                if states[1][0] == 0:
                    b[1][0].configure(text="O",fg="green",bg="black")
                    states[1][0] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                
                elif states[0][2] == 0:
                    b[0][2].configure(text="O",fg="green",bg="black")
                    states[0][2] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[2][2] == 0:
                    b[2][2].configure(text="O",fg="green",bg="black")
                    states[2][2] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[0][0] == 0:
                    b[0][0].configure(text="O",fg="green",bg="black")
                    states[0][0] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[2][0] == 0:
                    b[2][0].configure(text="O",fg="green",bg="black")
                    states[2][0] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[0][1] == 0:
                    b[0][1].configure(text="O",fg="green",bg="black")
                    states[0][1] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[2][1] == 0:
                    b[2][1].configure(text="O",fg="green",bg="black")
                    states[2][1] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
            elif states[0][1] == "X":#01middle
                if states[2][1] == 0:
                    b[2][1].configure(text="O",fg="green",bg="black")
                    states[2][1] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                
                elif states[0][0] == 0:
                    b[0][0].configure(text="O",fg="green",bg="black")
                    states[0][0] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[0][2] == 0:
                    b[0][2].configure(text="O",fg="green",bg="black")
                    states[0][2] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[2][0] == 0:
                    b[2][0].configure(text="O",fg="green",bg="black")
                    states[2][0] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[2][2] == 0:
                    b[2][2].configure(text="O",fg="green",bg="black")
                    states[2][2] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[1][0] == 0:
                    b[1][0].configure(text="O",fg="green",bg="black")
                    states[1][0] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[1][2] == 0:
                    b[1][2].configure(text="O",fg="green",bg="black")
                    states[1][2] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
            elif states[2][1] == "X":#21middle
                if states[0][1] == 0:
                    b[0][1].configure(text="O",fg="green",bg="black")
                    states[0][1] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                
                elif states[2][0] == 0:
                    b[2][0].configure(text="O",fg="green",bg="black")
                    states[2][0] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[2][2] == 0:
                    b[2][2].configure(text="O",fg="green",bg="black")
                    states[2][2] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[0][0] == 0:
                    b[0][0].configure(text="O",fg="green",bg="black")
                    states[0][0] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[0][2] == 0:
                    b[0][2].configure(text="O",fg="green",bg="black")
                    states[0][2] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[1][0] == 0:
                    b[1][0].configure(text="O",fg="green",bg="black")
                    states[1][0] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[1][2] == 0:
                    b[1][2].configure(text="O",fg="green",bg="black")
                    states[1][2] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()



        
                
            

            elif states[1][1] == "X" :
                
                if states[0][0] == 0:
                    b[0][0].configure(text="O",fg="green",bg="black")
                    states[0][0] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[2][0] == 0:
                    b[2][0].configure(text="O",fg="green",bg="black")
                    states[2][0] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[0][2] == 0:
                    b[0][2].configure(text="O",fg="green",bg="black")
                    states[0][2] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[2][2] == 0:
                    b[2][2].configure(text="O",fg="green",bg="black")
                    states[2][2] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[0][1] == 0:
                    b[0][1].configure(text="O",fg="green",bg="black")
                    states[0][1] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[2][1] == 0:
                    b[2][1].configure(text="O",fg="green",bg="black")
                    states[2][1] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[1][2] == 0:
                    b[1][2].configure(text="O",fg="green",bg="black")
                    states[1][2] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                elif states[1][0] == 0:
                    b[1][0].configure(text="O",fg="green",bg="black")
                    states[1][0] = "O"
                    player = "X"
                    count += 1
                    check_for_winner()
                
            else:
                messagebox.showerror("Tic Tac Toe","hey that box has already been selected")
            
        
        pc1()
        
    else:
        messagebox.showerror("Tic Tac Toe","hey that box has already been selected")
    



def pc():
    global b,states,player,stop_game,count
    b=[[0,0,0],[0,0,0],[0,0,0]]
    states=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            b[i][j]=Button(font=("Arial",60),width=4,bg="powder blue",command=lambda r=i,c=j: callback1(r,c))
            b[i][j].grid(row=i,column=j)
    player="X"
    stop_game=False
    count=0
    messagebox.showinfo("Tic Tac Toe","Now you are playing with Computer")
    messagebox.showinfo("Tic Tac Toe","Player one is User   and   Player two is computer")
    sp.set("Computer")


def callback(r,c):
    global player,count
    if player=="X" and states[r][c]==0 and stop_game==False:
        b[r][c].configure(text="X",fg="black",bg="green")
        states[r][c]="X"
        player="O"
        count += 1
        check_for_winner()
    elif player=="O" and states[r][c]==0 and stop_game==False:
        b[r][c].configure(text="O",fg="green",bg="black")
        states[r][c]="O"
        player="X"
        count += 1
        check_for_winner()
    else:
        messagebox.showerror("Tic Tac Toc","hey that box has already been selected")

def check_for_winner():
    global stop_game
    p1=fp.get()
    p2=sp.get()
    if p1 == "":
        p1 = "player1"
    if p2 == "":
        p2 = "player2"
    for i in range(3):
        if states[i][0]==states[i][1]==states[i][2]!=0:
            b[i][0].config(bg="grey")
            b[i][1].config(bg="grey")
            b[i][2].config(bg="grey")
            stop_game=True
            disable()
            if player=="O":
                messagebox.showinfo("Tic Tac Toe","Congratulations! {} Wins".format(p1))
                break
            else:
                messagebox.showinfo("TiC Tac Toe","Congratulations! {} Wins".format(p2))
                break
    for i in range(3):
            if states[0][i]==states[1][i]==states[2][i]!=0:
                b[0][i].config(bg="grey")
                b[1][i].config(bg="grey")
                b[2][i].config(bg="grey")
                stop_game=True
                disable()
                if player=="O":
                    messagebox.showinfo("Tic Tac Toe","Congratulations! {} Wins".format(p1))
                    break
                else:
                    messagebox.showinfo("Tic Tac Toe","Congratulations! {} Wins".format(p2))
                    break
            if states[0][0]==states[1][1]==states[2][2]!=0:
                b[0][0].config(bg="grey")
                b[1][1].config(bg="grey")
                b[2][2].config(bg="grey")
                stop_game=True
                disable()
                if player=="O":
                    messagebox.showinfo("Tic Tac Toe","Congratulations! {} Wins".format(p1))
                    break
                else:
                    messagebox.showinfo("TiC Tac Toe","Congratulations! {} Wins".format(p2))
                    break
            if states[2][0]==states[1][1]==states[0][2]!=0:
                b[2][0].config(bg="grey")
                b[1][1].config(bg="grey")
                b[0][2].config(bg="grey")
                stop_game=True
                disable()
                if player=="O":
                    messagebox.showinfo("Tic Tac Toe","Congratulations! {} Wins".format(p1))
                    break
                else:
                    messagebox.showinfo("TiC Tac Toe","Congratulations! {} Wins".format(p2))
                    break
            if count==9 and stop_game==False:
                messagebox.showinfo("Tic Tac Toe","Its a Tie! no one wins")
                disable()
                break
def disable():
    for i in range(3):
        for j in range(3):
            b[i][j].config(state=DISABLED)
                    
def reset():
    global b,states,player,stop_game,count
    b=[[0,0,0],[0,0,0],[0,0,0]]
    states=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            b[i][j]=Button(font=("Arial",60),width=4,bg="powder blue",command=lambda r=i,c=j: callback(r,c))
            b[i][j].grid(row=i,column=j)
    player="X"
    stop_game=False
    count=0
    sp.set("")
    
        
   
root=Tk()
root.title("TIC TAC TOE *cid")
fp=StringVar()
sp=StringVar()

def abt():
    messagebox.showinfo("Tic Tac Toe","Tic-tac-toe (American English), noughts and crosses (Commonwealth English), or Xs and Os is a paper-and-pencil game for two players, X and O, who take turns marking the spaces in a 3×3 grid. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is the winner.Synonym(s): Noughts and crosses; Xs and OsGenre(s): Paper-and-pencil gamePlayers: 2")

b=[[0,0,0],[0,0,0],[0,0,0]]
states=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        b[i][j]=Button(font=("Arial",60),width=4,bg="powder blue",command=lambda r=i,c=j: callback(r,c))
        b[i][j].grid(row=i,column=j)
player="X"
stop_game=False
count=0

    
    
def close_window():
    root.destroy()
    exit()
#to create player one and player two
label1=Label(root,text="Player One:",font=("Arial",20),bg="red",fg="white",relief="solid",width=12)
label1.grid(row=7,column=0)
entry1=Entry(root,textvar=fp)
entry1.grid(row=7,column=1,columnspan=8)
label2=Label(root,text="Player Two:",font=("Arial",20),bg="red",fg="white",relief="solid",width=12)
label2.grid(row=10,column=0)
entry2=Entry(root,textvar=sp)
entry2.grid(row=10,column=1,columnspan=8)
#to create menu bar
menu=Menu(root)
root.config(menu=menu)
submenu1=Menu(root)
submenu3=Menu(root)
menu.add_cascade(label="File",menu=submenu1)
submenu1.add_command(label="Restart",command=reset)
submenu1.add_command(label="Play with pc",command=pc)
submenu2=Menu(root)
menu.add_cascade(label="Options",menu=submenu2)
submenu2.add_command(label="About",command=abt)
menu.add_cascade(label="To exit",menu=submenu3)
submenu3.add_command(label="Exit",command=close_window)
root.mainloop()
    
    
