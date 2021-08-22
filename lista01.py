# Criação da classe
class carro:
    # Estados:
    nome = None
    ano = None
    cor = None
    velocidade_maxima = None
    velocidade_atual = None
    estado: None
    # Comportamentos:
    def ligar(self):
        self.estado = "ligado"
        print(f"O {self.nome} está {self.estado}")
    def parar(self):
        self.velocidade_atual = 0
        print(f"{self.nome} parado")
    def desligar(self):
        self.parar()
        self.estado = "desligado"
        print(f"O {self.nome} está {self.estado}")
    def acelerar(self, velocidade):
        if (self.estado == "ligado") and (
                velocidade <= self.velocidade_maxima):
            self.velocidade_atual = velocidade
            print(f"Velocidade atual do {self.nome}: {velocidade}km/h")
        elif self.estado == "desligado":
            print(f"Não é possível acelerar. O {self.nome} está desligado")
        elif velocidade > self.velocidade_maxima:
            self.velocidade_atual = self.velocidade_maxima  
            print(f"O {self.nome} atingiu sua velocidade máxima!")
            print(f"Velocidade atual do {self.nome}: {self.velocidade_atual}km/h")


# Atributos Carro 1
fusca = carro()
fusca.nome = "fusca"
fusca.ano = 1965
fusca.cor = "preto"
fusca.velocidade_maxima = 80
fusca.velocidade_atual = 20
fusca.estado = "ligado"


# Atributos Carro 2
ferrari = carro()
ferrari.nome = "ferrari_sr2000"
ferrari.ano = 2014
ferrari.cor = "vermelho"
ferrari.velocidade_maxima = 300
ferrari.velocidade_atual = 0
ferrari.estado = "desligado"


# Métodos:
fusca.acelerar(40)
ferrari.acelerar(200)
fusca.desligar()
ferrari.ligar()
ferrari.acelerar(320)
ferrari.parar()
ferrari.desligar()
fusca.ligar()
fusca.acelerar(100)
fusca.desligar()
