from tkinter import *
import random

wn = Tk()
f1 = Frame(wn)
f2 = Frame(wn)
f3 = Frame(wn)

gList=['Scissor', 'Rock', 'Paper']

count = StringVar()
game = StringVar()
com = StringVar()
you = StringVar()
count.set('0')
game.set('start')


def proc(key):
    com_ch = random.choice(gList)
    count.set(int(count.get()) + 1)
    com.set(com_ch)
    you.set(key)
    if (gList.index(com_ch) == gList.index(key)):
        game.set('Same')
    elif (gList.index(com_ch) ==0 and gList.index(key)==1):
        game.set('Win')
    elif (gList.index(com_ch) ==1 and gList.index(key)==2):
        game.set('Win')
    elif  (gList.index(com_ch) ==2 and gList.index(key)==0):
        game.set('Win')
    else:
        game.set('Loose')



l1 = Label(f1, text = 'count :')
l2 = Label(f1, textvariable = count)
l1.grid(column=0, row=0)
l2.grid(column=1, row=0)

l3 = Label(f2, textvariable=game)
l3.pack()

l4 = Label(f3, text = 'Computer')
l5 = Label(f3, text = 'You')
e1 = Entry(f3, textvariable = com)
e2 = Entry(f3, textvariable = you)
l4.grid(column = 0, row=0)
e1.grid(column = 1, row=0)
l5.grid(column = 0, row=1)
e2.grid(column = 1, row=1)
for i,j in enumerate(gList):
    def game_f(x=j):
        proc(x)
    Button(f3, text=j, command=game_f).grid(column=i, row=2)

f1.pack()
f2.pack()
f3.pack()

wn.mainloop()