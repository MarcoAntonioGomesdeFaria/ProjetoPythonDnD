from tkinter import *
from PIL import ImageTk, Image

root= Tk()

def window2():
    global img
    top=Toplevel()
    img = ImageTk.PhotoImage(Image.open('imagens/mai.png'))
    lbl1 = Label(top, image=img, width=400, height=300).pack()

btn1=Button(root, text='click here', command=window2).pack()


root.mainloop()