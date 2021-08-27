# Criação da classe:
class bicicleta:
    # Estados:
    velocidade_atual = None
    velocidade_maxima = None
    altura_cela = None
    altura_maxima = None
    calibragem_pneus = None
    calibragem_maxima = None
    tamanho_aro = None


    # Comportamentos:
    def __init__(
            self, velocidade_atual, velocidade_maxima,
            altura_cela, altura_maxima, calibragem_pneus,
            calibragem_maxima, tamanho_aro):
        self.velocidade_atual = velocidade_atual
        self.velocidade_maxima = velocidade_maxima
        self.altura_cela = altura_cela
        self.altura_maxima = altura_maxima
        self.calibragem_pneus = calibragem_pneus
        self.calibragem_maxima = calibragem_maxima
        self.tamanho_aro = tamanho_aro
    def mudar_velocidade(self, velocidade):
        if (0 <= velocidade < self.velocidade_maxima) and (
                self.calibragem_pneus > 0):
            self.velocidade_atual = velocidade
            print(f"Velocidade atual: {self.velocidade_atual}Km/h")
        elif (velocidade >= self.velocidade_maxima):
            self.velocidade_atual = self.velocidade_maxima
            print("Você atingiu a velocidade máxima.")
            print(f"Velocidade atual: {self.velocidade_atual}km/h")
        else:
            print("Não é possível mudar a velocidade atual.")
    def mudar_altura(self, altura):
        if (1 <= altura < self.altura_maxima) and (
                self.velocidade_atual == 0):
            self.altura_cela = altura
            print(f"Altura da cela atual: {self.altura_cela}cm")
        elif (altura >= self.altura_maxima) and (
                self.velocidade_atual == 0):
            self.altura_cela = self.altura_maxima
            print("Você atingiu a altura máxima.")
            print(f"Altura da cela atual: {self.altura_cela}cm")
        else:
            print("Não é possível mudar a altura da cela.")
    def calibrar(self, libra):
        if (0 <= libra < self.calibragem_maxima) and (
                self.velocidade_atual == 0):
            self.calibragem_pneus = libra
            print(f"Calibragem atual: {self.calibragem_pneus} libra(s)")
        elif (libra >= self.calibragem_maxima) and (
                self.velocidade_atual == 0):
            self.calibragem_atual = self.calibragem_maxima
            print("Você atingiu a calibragem máxima.")
            print(f"Calibragem atual: {self.calibragem_atual} libra(s)")
        else:
            print("Não é possível calibrar os pneus.")
    def parar(self):
        if (self.velocidade_atual > 0):
            self.velocidade_atual = 0
            print(f"Bicicleta parou.")
        else:
            print("Bicicleta já estava parada.")


def main():
    # Processamento:
    minha_bicicleta = bicicleta(0, 50, 0, 140, 0, 30, 26)


    # Métodos:
    minha_bicicleta.calibrar(24)
    minha_bicicleta.mudar_velocidade(37)
    minha_bicicleta.parar()
    minha_bicicleta.mudar_altura(8)


if __name__ == "__main__":
    main()
