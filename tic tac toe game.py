from tkinter import Tk,ttk,Button
from tkinter import messagebox
from random import randint
import random

p1 = []
p2 = []
mov = 0

def SetLayout(id,player_symbol):
    if id==1:
        b1.config(text= player_symbol)
        b1.state(['disabled'])
    elif id==2:
        b2.config(text= player_symbol)
        b2.state(['disabled'])
    elif id==3:
        b3.config(text= player_symbol)
        b3.state(['disabled'])
    elif id==4:
        b4.config(text= player_symbol)
        b4.state(['disabled'])
    elif id==5:
        b5.config(text= player_symbol)
        b5.state(['disabled'])
    elif id==6:
        b6.config(text= player_symbol)
        b6.state(['disabled'])
    elif id==7:
        b7.config(text= player_symbol)
        b7.state(['disabled'])
    elif id==8:
        b8.config(text= player_symbol)
        b8.state(['disabled'])
    elif id==9:
        b9.config(text= player_symbol)
        b9.state(['disabled'])

def CheckWinner():
    global mov 
    winner = -1

    if(1 in p1) and (2 in p1) and (3 in p1):
        winner = 1
    if(1 in p2) and (2 in p2) and (3 in p2):
        winner = 2

    if(4 in p1) and (5 in p1) and (6 in p1):
        winner = 1
    if(4 in p2) and (5 in p2) and (6 in p2):
        winner = 2

    if(7 in p1) and (8 in p1) and (9 in p1):
        winner = 1
    if(7 in p2) and (8 in p2) and (9 in p2):
        winner = 2

    if(1 in p1) and (4 in p1) and (7 in p1):
        winner = 1
    if(1 in p2) and (4 in p2) and (7 in p2):
        winner = 2

    if(2 in p1) and (5 in p1) and (8 in p1):
        winner = 1
    if(2 in p2) and (5 in p2) and (8 in p2):
        winner = 2

    if(3 in p1) and (6 in p1) and ( 9 in p1):
        winner = 1
    if(3 in p2) and (6 in p2) and (9 in p2):
        winner = 2

    if(1 in p1) and (5 in p1) and ( 9 in p1):
        winner = 1
    if(1 in p2) and (5 in p2) and (9 in p2):
        winner = 2

    if(3 in p1) and (5 in p1) and ( 7 in p1):
        winner = 1
    if(3 in p2) and (5 in p2) and (7 in p2):
        winner = 2

    if winner ==1:
        messagebox.showinfo(title="Congratulations.", message="You Win")
        return True
    elif winner ==2:
        messagebox.showinfo(title="Congratulations.",message="You Lost")
        return True
    elif mov ==9:
        messagebox.showinfo(title="Draw", 
            message="It's a Draw!!")
        return True

def ButtonClick(id):
    global ActivePlayer
    global p1,p2
    global mov
    SetLayout(id,"X")
    p2.append(id)
    mov +=1
    root.title("Tic Tac Toe : Player 1")
    if CheckWinner():
        returns
    
def Playerclick(id):
    global mov,p1
    SetLayout(id,"O")
    p1.append(id)
    mov +=1
    if CheckWinner():
        return
    AutoPlay(id)

def AutoPlay(id):
    global mov,p1,p2
    if mov==8:
        for i in range(1,10):
            if i not in p1 and i not in p2:
                ButtonClick(i)
                return
    if(1 == id):
        b=[]
        if 2 not in p1 and 2 not in p2:
            b.append(2)
        if 4 not in p1 and 4 not in p2:
            b.append(4)
        if 5 not in p1 and 5 not in p2:
            b.append(5)
        if 3 not in p1 and 3 not in p2:
            b.append(3)
        if 7 not in p1 and 7 not in p2:
            b.append(7)
        if 9 not in p1 and 9 not in p2:
            b.append(9)
        if b==[]:
            for i in range(1,10):
                if i not in p1 and i not in p2:
                    b.append(i)
        index=random.choice(b)
        ButtonClick(index)
        return
    if(2 == id):
        b=[]
        if 1 not in p1 and 1 not in p2:
            b.append(1)
        if 5 not in p1 and 5 not in p2:
            b.append(5)
        if 5 not in p1 and 5 not in p2:
            b.append(5)
        if 3 not in p1 and 3 not in p2:
            b.append(3)
        if 8 not in p1 and 8 not in p2:
            b.append(8)
        if b==[]:
            print(id)
            for i in range(1,10):
                if i not in p1 and i not in p2:
                    b.append(i)
        index=random.choice(b)
        ButtonClick(index)
        return
    if(3 == id):
        b=[]
        if 2 not in p1 and 2 not in p2:
            b.append(2)
        if 1 not in p1 and 1 not in p2:
            b.append(1)
        if 5 not in p1 and 5 not in p2:
            b.append(5)
        if 6 not in p1 and 6 not in p2:
            b.append(6)
        if 9 not in p1 and 9 not in p2:
            b.append(9)
        if b==[]:
            for i in range(1,10):
                if i not in p1 and i not in p2:
                    b.append(i)
        index=random.choice(b)
        ButtonClick(index)
        return

    if(4 == id):
        b=[]
        if 1 not in p1 and 1 not in p2:
            b.append(1)
        if 6 not in p1 and 6 not in p2:
            b.append(6)
        if 5 not in p1 and 5 not in p2:
            b.append(5)
        if 7 not in p1 and 7 not in p2:
            b.append(7)
        if b==[]:
            for i in range(1,10):
                if i not in p1 and i not in p2:
                    b.append(i)
        index=random.choice(b)
        ButtonClick(index)
        return
    if(5 == id):
        b=[]
        if 1 not in p1 and 1 not in p2:
            b.append(1)
        if 8 not in p1 and 8 not in p2:
            b.append(8)
        if 9 not in p1 and 9 not in p2:
            b.append(9)
        if 2 not in p1 and 2 not in p2:
            b.append(2)
        if 4 not in p1 and 4 not in p2:
            b.append(4)
        if 6 not in p1 and 6 not in p2:
            b.append(6)
        if 3 not in p1 and 3 not in p2:
            b.append(3)
        if 7 not in p1 and 7 not in p2:
            b.append(7)
        if b==[]:
            for i in range(1,10):
                if i not in p1 and i not in p2:
                    b.append(i)
        index=random.choice(b)
        ButtonClick(index)
        return
    if(6 == id):
        b=[]
        if 4 not in p1 and 4 not in p2:
            b.append(4)
        if 5 not in p1 and 5 not in p2:
            b.append(5)
        if 3 not in p1 and 3 not in p2:
            b.append(3)
        if 9 not in p1 and 9 not in p2:
            b.append(9)
        if b==[]:
            for i in range(1,10):
                if i not in p1 and i not in p2:
                    b.append(i)
        index=random.choice(b)
        ButtonClick(index)
        return
    if(7 == id):
        b=[]
        if 1 not in p1 and 1 not in p2:
           b.append(1)
        if 4 not in p1 and 4 not in p2:
            b.append(4)
        if 5 not in p1 and 5 not in p2:
           b.append(5)
        if 3 not in p1 and 3 not in p2:
            b.append(3)
        if 9 not in p1 and 9 not in p2:
           b.append(9)
        if 8 not in p1 and 8 not in p2:
            b.append(8)
        if b==[]:
            for i in range(1,10):
                if i not in p1 and i not in p2:
                    b.append(i)
        index=random.choice(b)
        ButtonClick(index)
        return
    if 8 == id:
        b=[]
        if 2 not in p1 and 2 not in p2:
           b.append(2)
        if 5 not in p1 and 5 not in p2:
           b.append(5)
        if 7 not in p1 and 7 not in p2:
            b.append(7)
        if 9 not in p1 and 9 not in p2:
           b.append(9)
        if b==[]:
            for i in range(1,10):
                if i not in p1 and i not in p2:
                    b.append(i)
        index=random.choice(b)
        ButtonClick(index)
        return
    if 9 == id:
        b=[]
        if 1 not in p1 and 1 not in p2:
           b.append(1)
        if 7 not in p1 and 7 not in p2:
            b.append(7)
        if 5 not in p1 and 5 not in p2:
           b.append(5)
        if 3 not in p1 and 3 not in p2:
            b.append(3)
        if 8 not in p1 and 8 not in p2:
            b.append(8)
        if 6 not in p1 and 6 not in p2:
            b.append(6)
        if b==[]:
            for i in range(1,10):
                if i not in p1 and i not in p2:
                    b.append(i)
        index=random.choice(b)
        ButtonClick(index)
        return


def EnableAll():
    b1.config(text= " ")
    b1.state(['!disabled'])
    b2.config(text= " ")
    b2.state(['!disabled'])
    b3.config(text= " ")
    b3.state(['!disabled'])
    b4.config(text= " ")
    b4.state(['!disabled'])
    b5.config(text= " ")
    b5.state(['!disabled'])
    b6.config(text= " ")
    b6.state(['!disabled'])
    b7.config(text= " ")
    b7.state(['!disabled'])
    b8.config(text= " ")
    b8.state(['!disabled'])
    b9.config(text= " ")
    b9.state(['!disabled'])


def Restart():
    global p1,p2,mov,ActivePlayer
    p1.clear(); p2.clear()
    mov=0
    ActivePlayer =1
    root.title("Tic Tac Toe : Player 1")
    EnableAll()




root = Tk()
root.title("Tic Tac toe : Player 1")
st = ttk.Style()
st.configure("my.TButton", font=('Chiller',30,'bold'),background='Red')

b1 = ttk.Button(root, text=" ", style="my.TButton")
b1.grid(row=1, column=0, sticky="nwse", ipadx=50,ipady=50)
b1.config(command = lambda : Playerclick(1))


b2 = ttk.Button(root, text=" ",style ="my.TButton")
b2.grid(row=1, column=1, sticky="snew", ipadx=50, ipady=50)
b2.config(command = lambda : Playerclick(2))

b3= ttk.Button(root, text=" ",style="my.TButton")
b3.grid(row=1, column=2, sticky="snew", ipadx=50,
        ipady=50)
b3.config(command = lambda : Playerclick(3))

b4 = ttk.Button(root, text=" ",style="my.TButton")
b4.grid(row=2, column=0, sticky="snew", ipadx=50,
        ipady=50)
b4.config(command = lambda : Playerclick(4))

b5 = ttk.Button(root, text=" ",style="my.TButton")
b5.grid(row=2, column=1, sticky="snew", ipadx=50,
        ipady=50)
b5.config(command = lambda : Playerclick(5))

b6 = ttk.Button(root, text=" ",style="my.TButton")
b6.grid(row=2, column=2, sticky="snew", ipadx=50,
        ipady=50)
b6.config(command = lambda : Playerclick(6))

b7 = ttk.Button(root, text=" ",style="my.TButton")
b7.grid(row=3, column=0, sticky="snew", ipadx=50,
        ipady=50)
b7.config(command = lambda : Playerclick(7))

b8 = ttk.Button(root, text=" ",style="my.TButton")
b8.grid(row=3, column=1, sticky="snew", ipadx=50,
        ipady=50)
b8.config(command = lambda : Playerclick(8))

b9 = ttk.Button(root, text=" ",style="my.TButton")
b9.grid(row=3, column=2, sticky="snew", ipadx=50,
        ipady=50)
b9.config(command = lambda : Playerclick(9))

Button(text="New Game..", font=('Courier new', 22, 'bold'), bg='blue', fg='Red',
            border=5, width=4,command = lambda :Restart()).grid(row=0, column=1, sticky="we")
root.resizable(0,0)
root.mainloop()
