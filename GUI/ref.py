#v1.33

from threading import Thread
from tkinter import *
import tkinter.messagebox
import random
from time import sleep

debug = True
game, game1 = 1, 1
tk = Tk()
tk.title("Tic Tac Toe Game PBR")
tk.iconbitmap("index.ico")
tk.geometry("1014x500+450+152")
tk.resizable(0, 0)
pa = StringVar()
playerb = StringVar()
p1 = StringVar()
p2 = StringVar()

bclick = True
flag = 0
win = False

moves_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]


# TODO: prolog

def learn():
    def local_learn():
        global moves_list, win, editArea, game1
        with open("games.csv", "r") as fd:
            for x in fd.readlines():
                reset()
                win = False
                x = x.strip("\n")
                move = x.split(", ")
                txtOutput.insert(END, str(game1) + "." + " ")
                for y in range(len(move)):
                    mov = move[y][0]
                    play = move[y][1].upper()
                    txtOutput.insert(END, str(mov) + str(play) + " ")
                    if not win:
                        btnClick(button_list[moves_list.index(mov)], play)
                txtOutput.insert(END, "\n")
                txtOutput.see(END)
                game1 += 1
                sleep(0.01)

    c = Thread(target=local_learn)
    c.start()


def generate():
    reset()
    lista = []
    index = random.randint(2, 5)
    for _ in range(index):
        poz = random.choice(button_list)
        if poz not in lista:
            lista.append(poz)
            btnClick(poz)


def btnClick(buttons, player=None):
    global bclick, flag, player2_name, player1_name, playerb, pa
    if buttons["text"] == " " and bclick:
        if player is None:
            player = "X"
        buttons["text"] = player
        bclick = False
        playerb = p2.get() + " Wins!"
        pa = p1.get() + " Wins!"
        checkForWin()
        flag += 1

    elif buttons["text"] == " " and not bclick:
        if player is None:
            player = "0"
        buttons["text"] = player
        bclick = True
        checkForWin()
        flag += 1
    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")


def reset():
    global flag, win
    button1["text"] = button2["text"] = button3["text"] = button4["text"] = button5["text"] = button6["text"] = \
        button7["text"] = button8["text"] = button9["text"] = " "
    flag = 0
    win = True


def checkForWin():
    global game
    if (button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" or
            button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X" or
            button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" or
            button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" or
            button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X" or
            button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or
            button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" or
            button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X"):
        # tkinter.messagebox.showinfo("Tic-Tac-Toe", "X Won!")
        txtOutput1.insert(END, str(game) + "." + " " + "X Won!" + "\n")
        txtOutput1.see(END)
        game += 1
        reset()

    elif flag == 8:
        # tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie")
        txtOutput1.insert(END, str(game) + "." + " " + "Tie!\n")
        txtOutput1.see(END)
        game += 1
        reset()

    elif (button1["text"] == "0" and button2["text"] == "0" and button3["text"] == "0" or
          button4["text"] == "0" and button5["text"] == "0" and button6["text"] == "0" or
          button7["text"] == "0" and button8["text"] == "0" and button9["text"] == "0" or
          button1["text"] == "0" and button5["text"] == "0" and button9["text"] == "0" or
          button3["text"] == "0" and button5["text"] == "0" and button7["text"] == "0" or
          button1["text"] == "0" and button4["text"] == "0" and button7["text"] == "0" or
          button2["text"] == "0" and button5["text"] == "0" and button8["text"] == "0" or
          button3["text"] == "0" and button6["text"] == "0" and button9["text"] == "0"):
        # tkinter.messagebox.showinfo("Tic-Tac-Toe", "0 Won!")
        txtOutput1.insert(END, str(game) + "." + " " + "0 Won!" + "\n")
        txtOutput1.see(END)
        game += 1
        reset()


buttons = StringVar()

button1 = Button(tk, text=" ", font="Times 20 bold", bg="white", fg="black", height=4, width=8,
                 command=lambda: btnClick(button1))
button1.grid(row=3, column=0)

button2 = Button(tk, text=" ", font="Times 20 bold", bg="white", fg="black", height=4, width=8,
                 command=lambda: btnClick(button2))
button2.grid(row=3, column=1)

button3 = Button(tk, text=" ", font="Times 20 bold", bg="white", fg="black", height=4, width=8,
                 command=lambda: btnClick(button3))
button3.grid(row=3, column=2)

button4 = Button(tk, text=" ", font="Times 20 bold", bg="white", fg="black", height=4, width=8,
                 command=lambda: btnClick(button4))
button4.grid(row=4, column=0)

button5 = Button(tk, text=" ", font="Times 20 bold", bg="white", fg="black", height=4, width=8,
                 command=lambda: btnClick(button5))
button5.grid(row=4, column=1)

button6 = Button(tk, text=" ", font="Times 20 bold", bg="white", fg="black", height=4, width=8,
                 command=lambda: btnClick(button6))
button6.grid(row=4, column=2)

button7 = Button(tk, text=" ", font="Times 20 bold", bg="white", fg="black", height=4, width=8,
                 command=lambda: btnClick(button7))
button7.grid(row=5, column=0)

button8 = Button(tk, text=" ", font="Times 20 bold", bg="white", fg="black", height=4, width=8,
                 command=lambda: btnClick(button8))
button8.grid(row=5, column=1)

button9 = Button(tk, text=" ", font="Times 20 bold", bg="white", fg="black", height=4, width=8,
                 command=lambda: btnClick(button9))
button9.grid(row=5, column=2)

button_list = [button1, button2, button3, button4, button5, button6, button7, button8, button9]

buttonlearn = Button(tk, text="Learn", font="Times 12 bold", bg="red4", fg="white", height=2, width=10,
                     command=learn).place(x=88, y=445)

buttongenerate = Button(tk, text="Generate", font="Times 12 bold", bg="red4", fg="white", height=2, width=10,
                        command=generate).place(x=230, y=445)

if debug:
    Label(tk, text="a", font="Times 10", bg="white").place(x=0, y=0)
    Label(tk, text="b", font="Times 10", bg="white").place(x=140, y=0)
    Label(tk, text="c", font="Times 10", bg="white").place(x=280, y=0)
    Label(tk, text="d", font="Times 10", bg="white").place(x=0, y=150)
    Label(tk, text="e", font="Times 10", bg="white").place(x=140, y=150)
    Label(tk, text="f", font="Times 10", bg="white").place(x=280, y=150)
    Label(tk, text="g", font="Times 10", bg="white").place(x=0, y=300)
    Label(tk, text="h", font="Times 10", bg="white").place(x=140, y=300)
    Label(tk, text="i", font="Times 10", bg="white").place(x=280, y=300)

Label(tk, text="Games", font="Times 15 bold", justify=RIGHT).place(x=450, y=30)
Label(tk, text="Wins", font="Times 15 bold").place(x=450, y=250)
txtFrame = Frame(tk, borderwidth=1, relief="sunken")
txtOutput = Text(txtFrame, wrap=NONE, height=10, width=58, borderwidth=0)
vscroll = Scrollbar(txtFrame, orient=VERTICAL, command=txtOutput.yview)
txtOutput["yscroll"] = vscroll.set

vscroll.pack(side="right", fill="y")
txtOutput.pack(side="left", fill="both", expand=True)

txtFrame.place(x=450, y=60)

# T = Text(tk, height=10, width=40)
# T.place(x=450, y=280)
#
# T.insert(END,
#          "")


txtFrame1 = Frame(tk, borderwidth=1, relief="sunken")
txtOutput1 = Text(txtFrame1, wrap=NONE, height=10, width=40, borderwidth=0)
vscroll1 = Scrollbar(txtFrame1, orient=VERTICAL, command=txtOutput1.yview)
txtOutput1["yscroll"] = vscroll1.set

vscroll1.pack(side="right", fill="y")
txtOutput1.pack(side="left", fill="both", expand=True)

txtFrame1.place(x=450, y=280)

tk.mainloop()
