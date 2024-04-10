class Personagem():
    def __init__(self, vida, CA, arma):
        self.vida = vida
        self.ca = CA
        self.arma = arma
        if(self.arma>3):self.arma=2
        self.armas=['espada','machado','cajado']

    def ataque(self):
        if(self.arma==0):
            print('ataque desarmado')
        else:
            print(f'atacou com {self.armas[self.arma-1]}')

joao= Personagem(10, 15, 0)
joao.ataque()




