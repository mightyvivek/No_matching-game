print('  1  |  2  |  3  ')
print('-----|-----|-----')
print('  4  |  5  |  6  ')
print('-----|-----|-----')
print('  7  |  8  |  9  ')
import tkinter as tk
from tkinter import *
win = tk.Tk()
win.title('Matching_Game')
win.geometry('600x300')

label = Label(win,text='First Player: ')
label.pack()
entry = Entry(win,textvariable='First player')
entry.pack()

win.mainloop()
'''n = 1
while(n>0):
    x = input('first player: ')
    y = input('Second player: ')
    if(x == y):
        print('                   Second player win\n')
        break
    z = input('first player: ')
    w = input('Second player: ')
    if(y == z):
        print('                   First player win\n')
        break
    elif(z == w):
        print('                   Second payer win\n')
    break'''