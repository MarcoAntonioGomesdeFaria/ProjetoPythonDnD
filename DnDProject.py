from tkinter import *
import sqlite3
import PIL

root = Tk()

conn= sqlite3.connect('dnd')
c=conn.cursor()

#c.execute("""CREATE TABLE personagens(
#                nome text,
#                vida integer,
#                CA integer,
#                Attack1 text,
#                Attack2 text,
#                Attack3 text
#              )""")

#Functions

def add_character():
    conn=sqlite3.connect('dnd')
    c=conn.cursor()



    c.execute("INSERT INTO personagens VALUES(:nome, :vida, :ca, :atk01, :atk02, :atk03)",
                {
                    'nome': e_nome.get(),
                    'vida': e_vida.get(),
                    'ca': e_CA.get(),
                    'atk01': e_atk1.get(),
                    'atk02': e_atk2.get(),
                    'atk03': e_atk3.get()
                 })
    e_nome.delete(0,END)
    e_vida.delete(0,END)
    e_CA.delete(0,END)
    e_atk1.delete(0,END)
    e_atk2.delete(0,END)
    e_atk3.delete(0,END)

    conn.commit()
    conn.close()

def search_char():
    conn=sqlite3.connect('dnd')
    c=conn.cursor()

    c.execute()

    conn.commit()
    conn.close()
    


#LABELS
lbl_nome = Label(root, text='Nome')
lbl_nome.grid(row=1,column=0, pady=10)

lbl_vida= Label(root, text='Vida')
lbl_vida.grid(row=2,column=0, pady=10)

lbl_CA= Label(root, text='CA')
lbl_CA.grid(row=3,column=0, pady=10)

lbl_Atk1= Label(root, text='atk1')
lbl_Atk1.grid(row=4,column=0, pady=10)

lbl_Atk2= Label(root, text='atk1')
lbl_Atk2.grid(row=5,column=0, pady=10)

lbl_Atk3= Label(root, text='atk1')
lbl_Atk3.grid(row=6,column=0, pady=10)

#ENTRIES
e_nome=Entry(root)
e_nome.grid(row=1,column=1, pady=10,padx=10)

e_vida=Entry(root)
e_vida.grid(row=2,column=1, pady=10,padx=10)

e_CA=Entry(root)
e_CA.grid(row=3,column=1, pady=10,padx=10)

e_atk1=Entry(root)
e_atk1.grid(row=4,column=1, pady=10,padx=10)

e_atk2=Entry(root)
e_atk2.grid(row=5,column=1, pady=10,padx=10)

e_atk3=Entry(root)
e_atk3.grid(row=6,column=1, pady=10,padx=10)

#BUTTONS
btn_add = Button(root, text='Adicionar', command=add_character)
btn_add.grid(row=7,column=0, columnspan=2)

btn_search = Button(root,textvariable="Procurar", command=search_char)
conn.commit()
conn.close()


root.mainloop()