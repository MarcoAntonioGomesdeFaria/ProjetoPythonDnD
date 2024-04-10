from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root= Tk()

#CREATING DB
conn= sqlite3.connect('addresses_book.db')
c=conn.cursor()

#c.execute(""" CREATE TABLE addresses (
#    f_name text,
#    l_name text,
#    city text,
#    zipcode integer
#    )""")

conn.commit()
conn.close()

#FUNCTIONS

def submit():
    conn=sqlite3.connect('addresses_book.db')
    c=conn.cursor()

    c.execute("INSERT INTO addresses VALUES(:f_name, :l_name, :city, :zipcode)",
              {
                  'f_name': e_fname.get(),
                  'l_name': e_lname.get(),
                  'city': e_city.get(),
                  'zipcode': e_zipcode.get()
              })

    # clear Entries
    e_fname.delete(0, END)
    e_lname.delete(0, END)
    e_city.delete(0, END)
    e_zipcode.delete(0, END)

    conn.commit()
    conn.close

def query():
    conn = sqlite3.connect('addresses_book.db')
    c=conn.cursor()

    c.execute('SELECT *,oid FROM addresses')
    records=c.fetchall()
    print(records)
    print_records=""

    for record in records:
        print_records += str(record)+'\n'

    top=Toplevel()
    lbl_query=Label(top,text=print_records)
    lbl_query.grid(row=0,column=0)

    conn.commit()
    conn.close()

def deletar():
    conn = sqlite3.connect('addresses_book.db')
    c = conn.cursor()

    c.execute('DELETE FROM addresses WHERE oid = ' + e_id.get())

    conn.commit()
    conn.close()


def delete():
    top2=Toplevel()
    global e_id
    e_id=Entry(top2,width=10)
    e_id.grid(row=0,column=1,pady=10 ,padx=10)

    lbl_delete= Label(top2,text='Deletar ID:')
    lbl_delete.grid(row=0,column=0,pady=10, padx=10)

    btn_delete2= Button(top2,text='Confirmar', command=deletar)
    btn_delete2.grid(row=1,column=0,columnspan=2,pady=10, padx=10)



#Labels
lbl_fnome=Label(root,text="Primero Nome")
lbl_fnome.grid(row=1, column=0, pady=(10,0))

lbl_lnome=Label(root,text="Ultimo Nome")
lbl_lnome.grid(row=2, column=0, pady=(10,0))

lbl_city=Label(root,text="Cidade")
lbl_city.grid(row=3, column=0, pady=(10,0))

lbl_zipcode = Label(root, text='CEP')
lbl_zipcode.grid(row=4, column=0, pady=(10,0))


#Entries
e_fname = Entry(root,width=50)
e_fname.grid(row=1, column=1, pady=(10,0))

e_lname = Entry(root,width=50)
e_lname.grid(row=2, column=1, pady=(10,0))

e_city = Entry(root,width=50)
e_city.grid(row=3, column=1, pady=(10,0))

e_zipcode = Entry(root,width=50)
e_zipcode.grid(row=4, column=1, pady=(10,0))


#Buttons
btn_add = Button(root,text='Adicionar',command=submit)
btn_add.grid(row=5,column=0, columnspan=2, pady=10, padx=10,ipadx=100)

btn_query = Button(root, text='Show Data', command=query)
btn_query.grid(row=6,column=0, columnspan=2, pady=10, padx=10,ipadx=100)

btn_delete = Button(root, text='Delete', command=delete)
btn_delete.grid(row=7,column=0, columnspan=2, pady=10, padx=10,ipadx=100)




    

root.mainloop()