from tkinter import *
import tkinter.messagebox

tk = Tk()
tk.title("Tic Tac Toe Game PBR")
tk.iconbitmap("index.ico")
tk.geometry("414x500+450+152")
tk.resizable(0, 0)
pa = StringVar()
playerb = StringVar()
p1 = StringVar()
p2 = StringVar()

bclick = True
flag = 0

moves_list = [0, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']


def learn():
    global moves_list
    with open("games.csv", "r") as fd:
        for x in fd.readlines():
            move = x.split(",")
            print(move)
            for y in range(len(move)):
                play = move[y][0]
                mov = move[y][1]
                btnClick(moves_list.index(mov))


def generate():
    print("generate")


def btnClick(buttons):
    global bclick, flag, player2_name, player1_name, playerb, pa
    if buttons["text"] == " " and bclick == True:
        buttons["text"] = "X"
        bclick = False
        playerb = p2.get() + " Wins!"
        pa = p1.get() + " Wins!"
        checkForWin()
        flag += 1


    elif buttons["text"] == " " and bclick == False:
        buttons["text"] = "O"
        bclick = True
        checkForWin()
        flag += 1
    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")


def checkForWin():
    global flag
    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
            button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
            button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or
            button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
            button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
            button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
            button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
            button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
            button7['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", pa)
        button1['text'] = button2['text'] = button3['text'] = button4['text'] = button5['text'] = button6['text'] = \
            button7['text'] = button8['text'] = button9['text'] = ' '
        flag = 0

    elif (flag == 8):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie")
        button1['text'] = button2['text'] = button3['text'] = button4['text'] = button5['text'] = button6['text'] = \
            button7['text'] = button8['text'] = button9['text'] = ' '
        flag = 0



    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
          button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
          button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
          button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
          button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
          button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
          button7['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", playerb)
        button1['text'] = button2['text'] = button3['text'] = button4['text'] = button5['text'] = button6['text'] = \
            button7['text'] = button8['text'] = button9['text'] = ' '
        flag = 0


buttons = StringVar()

button1 = Button(tk, text=" ", font='Times 20 bold', bg='white', fg='black', height=4, width=8,
                 command=lambda: btnClick(button1))
button1.grid(row=3, column=0)

button2 = Button(tk, text=' ', font='Times 20 bold', bg='white', fg='black', height=4, width=8,
                 command=lambda: btnClick(button2))
button2.grid(row=3, column=1)

button3 = Button(tk, text=' ', font='Times 20 bold', bg='white', fg='black', height=4, width=8,
                 command=lambda: btnClick(button3))
button3.grid(row=3, column=2)

button4 = Button(tk, text=' ', font='Times 20 bold', bg='white', fg='black', height=4, width=8,
                 command=lambda: btnClick(button4))
button4.grid(row=4, column=0)

button5 = Button(tk, text=' ', font='Times 20 bold', bg='white', fg='black', height=4, width=8,
                 command=lambda: btnClick(button5))
button5.grid(row=4, column=1)

button6 = Button(tk, text=' ', font='Times 20 bold', bg='white', fg='black', height=4, width=8,
                 command=lambda: btnClick(button6))
button6.grid(row=4, column=2)

button7 = Button(tk, text=' ', font='Times 20 bold', bg='white', fg='black', height=4, width=8,
                 command=lambda: btnClick(button7))
button7.grid(row=5, column=0)

button8 = Button(tk, text=' ', font='Times 20 bold', bg='white', fg='black', height=4, width=8,
                 command=lambda: btnClick(button8))
button8.grid(row=5, column=1)

button9 = Button(tk, text=' ', font='Times 20 bold', bg='white', fg='black', height=4, width=8,
                 command=lambda: btnClick(button9))
button9.grid(row=5, column=2)

buttonlearn = Button(tk, text="Learn", font='Times 12 bold', bg='red4', fg='white', height=2, width=10,
                     command=learn).place(x=88, y=445)

buttongenerate = Button(tk, text="Generate", font='Times 12 bold', bg='red4', fg='white', height=2, width=10,
                        command=generate).place(x=230, y=445)

tk.mainloop()

# def main():
#     pass
#
#
#
# if __name__ == "__main__":
#     main()
