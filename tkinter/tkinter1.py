from tkinter import *
import tkinter
win= tkinter.Tk()
win.geometry('400x400')
label = tkinter.Label(win,text="hello students....................................").place(x=40,y=70) # place is used to print the data at specific place
label2 = tkinter.Label(win,text="hello world....................................").pack() 
label3 = tkinter.Label(win,text="hello programming....................................").pack() 
btn = Button(win,text = "submit").pack()
en= tkinter.Entry().place(x=30,y=50)
win.mainloop() 

