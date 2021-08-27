# Criação da classe:
class radio:
    # Estados:
    estado = None
    volume = None
    faixa = None
    frequencia_atual = None

    # Comportamentos:
    def __init__(self, estado, volume, faixa, frequencia_atual):
        self.estado = estado
        self.volume = volume
        self.faixa = faixa
        self.frequencia_atual = frequencia_atual
    def onoff(self):
        if self.estado.lower() == "ligado":
            self.estado = "desligado"
            print(f"Seu rádio está {self.estado}")
        elif self.estado.lower() == "desligado":
            self.estado = "ligado"
            print(f"Seu rádio está {self.estado}")
    def mudar_volume(self, altura):
        if (1 <= altura <= 10) and (
                self.estado.lower() == "ligado"):
            self.volume = altura
            print(f"Volume atual: {self.volume}")
        else:
            print("Não foi possível mudar o volume.")
    def mudar_faixa(self):
        if (self.faixa.upper() == "AM") and (
                self.estado.lower() == "ligado"):
            self.faixa = "FM"
            print(f"Faixa atual: {self.faixa}")
        elif (self.faixa.upper() == "FM") and (
                self.estado.lower() == "ligado"):
            self.faixa = "AM"
            print(f"Faixa atual: {self.faixa}")
        else:
            print("Não foi possível mudar a faixa.")
    def mudar_frequencia(self, frequencia):
        if (520 <= frequencia <= 1710) and (
                self.faixa == "AM") and (
                self.estado.lower() == "ligado"):
            self.frequencia_atual = frequencia
            print(f"Frequência atual: {self.frequencia_atual}kHz")
        elif (87.5 <= frequencia <= 108) and (
                self.faixa == "FM") and (
                self.estado.lower() == "ligado"):
            self.frequencia_atual = frequencia
            print(f"Frequência atual: {self.frequencia_atual}MHz")
        else:
            print("Não foi possível mudar a frequência.")


def main():
    # Processamento:
    meu_radio = radio("desligado", 1, "AM", None)


    # Métodos:
    meu_radio.onoff()
    meu_radio.mudar_volume(6)
    meu_radio.mudar_faixa()
    meu_radio.mudar_frequencia(101.1)
    meu_radio.onoff()


if __name__ == "__main__":
    main()
