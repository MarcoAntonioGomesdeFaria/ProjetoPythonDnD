from tkinter import *
from PIL import ImageTk,Image
import mysql.connector


root = Tk()
root.geometry("920x720")
root.title('teste')

#----------------------------------------CONFIGURANDO DATABASE----------------------------------------
my_db = mysql.connector.connect(host="localhost", user="root", passwd="ma0506",database='dnddb',)
cursor = my_db.cursor()


#----------------------------------------FUNÇOES----------------------------------------

def add_personagem(nome,vida,ca,classe,id):
    my_db = mysql.connector.connect(host="localhost", user="root", passwd="ma0506", database='dnddb', )
    cursor = my_db.cursor()
    cursor.execute(f'insert into player values ("{nome}", {vida}, {ca}, "{classe}",{id})')
    my_db.commit()


def delete_record(id):
    my_db = mysql.connector.connect(host="localhost", user="root", passwd="ma0506", database='dnddb', )
    cursor = my_db.cursor()
    cursor.execute(f'DELETE FROM player WHERE ID = {id}')
    my_db.commit()

def busca_dados(nome):
    my_db = mysql.connector.connect(host="localhost", user="root", passwd="ma0506", database='dnddb', )
    cursor = my_db.cursor()
    cursor.execute(f'SELECT * from player where nome = "{nome}"')
    for item in cursor:
            print(item)
    try:
        e_nome = Label(root, text=item[0])
        e_nome.grid(row='1', column='1')

        e_vida = Label(root, text=item[1])
        e_vida.grid(row='2', column='1')

        e_ca = Label(root, text=item[2])
        e_ca.grid(row='3', column='1')

        e_classe = Label(root, text=item[3])
        e_classe.grid(row='4', column='1')

    except:
        e_vida = Label(root, text='0')
        e_vida.grid(row='2', column='1')

        e_vida = Label(root, text='0')
        e_vida.grid(row='3', column='1')

        e_classe = Label(root, text='')
        e_classe.grid(row='4', column='1')

def search_magic(magic):
    my_db = mysql.connector.connect(host="localhost", user="root", passwd="ma0506", database='dnddb', )
    cursor = my_db.cursor()
    cursor.execute(f'SELECT * FROM dnd5_spells order by spell_level')
    

def equipamentos(id):
    my_db = mysql.connector.connect(host="localhost", user="root", passwd="ma0506", database='dnddb', )
    cursor = my_db.cursor()
    cursor.execute(f"select * from equipamento where player_id = {id}")
    for item in cursor:
        print(item)
    my_db.commit()



def inserir_equipamentos(nome, tipo, descriçao,id):

    my_db = mysql.connector.connect(host="localhost", user="root", passwd="ma0506", database='dnddb', )
    cursor = my_db.cursor()
    cursor.execute(f"insert into equipamento (`nome`,`tipo`, `descricao`, `player_id`) values ('{nome}','{tipo}','{descriçao}','{id}')")
    my_db.commit()

def remover_equipamentos(id):
    my_db = mysql.connector.connect(host="localhost", user="root", passwd="ma0506", database='dnddb', )
    cursor = my_db.cursor()
    cursor.execute(f'delete from equipamento where player_id = "{id}"')
    my_db.commit()




#----------------------------------------VARIAVEIS----------------------------------------

nome = 'kibi'
cursor.execute(f"select id from player where nome= '{nome}'")
for item in cursor:
    id=item[0]

busca_dados(nome)
#inserir_equipamentos("vorpal+3", "Ninkentou", "arma com habilidade de decepar membros com criticos 2d8 de dano cortante/perfurante", id)


#----------------------------------------VISUAL----------------------------------------

#----------------------------------------Buttons----------------------------------------
btn_equipamentos = Button(root, text='Equipamentos', command=lambda:equipamentos(id))
btn_equipamentos.grid(row=5, column=0)

btn_delete_equipamento = Button(root, text='Deletar Equipamento', command=lambda:remover_equipamentos(id))
btn_delete_equipamento.grid(row=5, column=1)

btn_inserirequipamentos = Button(root,text='Inserir', command=lambda:inserir_equipamentos())
btn_inserirequipamentos.grid(row=5, column=2)
#remover_equipamentos('')

#----------------------------------------LABELS----------------------------------------

lbl = Label(root,text='FICHA DE PERSONAGEM',font='roboto')
lbl.grid(row='0',column='1')

lbl = Label(root,text='Nome')
lbl.grid(row='1',column='0')

lbl = Label(root,text='Vida')
lbl.grid(row='2',column='0')

lbl = Label(root,text='CA')
lbl.grid(row='3',column='0')

lbl = Label(root,text='Classe')
lbl.grid(row='4',column='0')


root.mainloop()