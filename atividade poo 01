class Pessoas():
    def __init__(self, nome,peso,idade):
        self.nome=nome
        self.peso=peso
        self.idade=idade
        self.comendo = False
        self.andando = False
        self.falando = False
        self.parado = True

    def parar(self):
        if self.parado == False:
            self.parado = True
            self.comendo = False
            self.andando = False
            self.falando = False
            print(self.nome,"está parado ")
        else:
            print(self.nome, "ja esta parado ")

    def comer(self):
        if self.comendo == False:
            self.parado = False
            self.comendo = True
            self.andando = False
            self.falando = False
            print(f"{self.nome} esta comendo ")
        else:
            print(f" {self.nome} já estava comendo ")

    def andar(self):
        if self.andando == False:
            self.parado = False
            self.comendo = False
            self.andando = True
            self.falando = False
            print(f"{self.nome} esta caminhando ")
        else:
            print(self.nome,"ja esta andando ")

    def falar(self):
        if self.falando == False:
            self.parado = False
            self.comendo = False
            self.andando = False
            self.falando = True
            print(f"{self.nome} esta falando ")
        else:
            print(self.nome,"ja esta falando ")


