from tkinter import *
from PIL import ImageTk, Image

root = Tk()

img1= ImageTk.PhotoImage(Image.open('imagens/1.png'))
img2= ImageTk.PhotoImage(Image.open('imagens/2.jpg'))
img3= ImageTk.PhotoImage(Image.open('imagens/3.jpg'))
img4= ImageTk.PhotoImage(Image.open('imagens/4.png'))
img5= ImageTk.PhotoImage(Image.open('imagens/5.png'))
img6= ImageTk.PhotoImage(Image.open('imagens/6.jpeg'))
img7= ImageTk.PhotoImage(Image.open('imagens/7.png'))


img_list=[img1,img2,img3,img4,img5,img6,img7]
current=0
listagem=1

lbl1= Label(image=img_list[current], width=1200, height=700,)
lbl1.grid(row=0,column=0, columnspan=3)

def Next(img_n):
    global listagem
    global lbl1
    global btn_next
    global btn_back
    global current
    lbl1.grid_forget()
    current+=1
    if current>=7:
        current-=1
    lbl1= Label(image=img_list[current], width=400, height=300,)
    lbl1.grid(row=0,column=0, columnspan=3)

    listagem += 1
    if listagem>7:
        listagem=7

    lbl_text = Label(root, text=f'Image {listagem} of {len(img_list)}', anchor=E)
    lbl_text.grid(row=2, column=2, sticky=E + W)


def Back():
    global listagem
    global lbl1
    global btn_next
    global btn_back
    global current
    lbl1.grid_forget()
    current-=1
    if current<1:
        current+=1
    lbl1= Label(image=img_list[current], width=400, height=300,)
    lbl1.grid(row=0,column=0, columnspan=3)
    listagem-=1
    if listagem <1:
        listagem=1

    lbl_text = Label(root, text=f'Image {listagem} of {len(img_list)}', anchor=E)
    lbl_text.grid(row=2, column=2, sticky=E + W)


lbl_text= Label(root, text=f'Image {listagem} of {len(img_list)}', anchor=E)
lbl_text.grid(row=2,column=2,sticky=E+W)

btn_Next= Button(root, text=">>",  command= lambda: Next(2))
btn_Back= Button(root, text="<<",command= lambda: Back())
btn_Reset=Button(root, text='Exit', command=root.quit())

btn_Next.grid(row=1, column=2 )
btn_Back.grid(row=1, column=0)
btn_Reset.grid(row=1, column=1)

root.mainloop()