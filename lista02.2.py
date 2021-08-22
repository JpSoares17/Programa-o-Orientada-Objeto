# Criação da Classe:
class bicicleta:

    
    # Estados:
    peso = 0
    altura = 0
    velocidade_atual = 0
    cor = None
    aro = 0
    altura_cela = 0
    calibragem_pneus = 0


    # Comportamentos:
    def pedalar(self):
        if  0 <= self.velocidade_atual < 50:
            self.velocidade_atual += 1
            print(f"Velocidade aumentou... Velocidade atual: {self.velocidade_atual}")
        elif self.velocidade_atual == 50:
            print("A bicicleta já atingiu sua velocidade máxima!")
    def regular_cela(self, nivel):
        if (1 <= nivel <= 10) and (
                self.velocidade_atual == 0):
            self.altura_cela = nivel
            print(f"Cela está regulada no nível {self.altura_cela}")
        elif self.velocidade_atual != 0:
            print(f"Para regular cela a bicicleta precisa estar parada!")
        else:
            print("Essa regulagem de cela não está disponível")
    def frear(self):
        if 0 < self.velocidade_atual <= 50:
            self.velocidade_atual -= 1
            print(f"Velocidade diminuiu... Velocidade atual: {self.velocidade_atual}")
        elif self.velocidade_atual == 0:
            print("A bicicleta já atingiu sua velocidade mínima!")
    def calibrar_pneu(self, calibre):
        if (0 <= self.calibragem_pneus <= 30) and (
                self.velocidade_atual == 0):
            self.calibragem = calibre
            print(f"Pneus calibrados: {self.calibragem_pneus} libras")
        elif calibre > 30:
            print("Seu pneu vai explodir, calibragem impossibilitada")
        elif calibre == 0:
            print("Seu pneu está vazio!")
    def parar(self):
        if self.velocidade_atual != 0:
            self.velocidade_atual = 0
            print("Bicicleta está parada!")
    

# Atributos:
minha_bicicleta = bicicleta()
minha_bicicleta.peso = 13
minha_bicicleta.altura = 115
minha_bicicleta.velocidade_atual = 0
minha_bicicleta.cor = "preta"
minha_bicicleta.aro = 26
minha_bicicleta.altura_cela = 4
minha_bicicleta.calibragem_pneus = 20


# Métodos:
minha_bicicleta.pedalar()
minha_bicicleta.parar()
minha_bicicleta.regular_cela(8)
minha_bicicleta.pedalar()
minha_bicicleta.pedalar()
minha_bicicleta.frear()
minha_bicicleta.parar()
minha_bicicleta.calibrar_pneu(27)
