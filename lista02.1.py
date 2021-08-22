# Criação da classe
class radio:

    
    # Estados:
    modelo = None
    faixa = None
    modo = None
    frequencia = 0
    volume = 0
    estado = None

    
    # Comportamentos:
    def mudar_faixa(self, faixa):
        if (faixa[0].lower() == "a"):
            self.faixa = "AM"
            print(f"Rádio está configurada na faixa {self.faixa}")
        elif faixa[0].lower == "f":
            self.faixa = "FM"
            print(f"Rádio está configurada na faixa {self.faixa}")
        else:
            print("Opção inválida!")
    def mudar_modo(self, modo):
        if modo[0].lower() == "u":
            self.modo = "USB"
            print(f"O {self.modelo} está em modo {self.modo}")
        elif modo[0].lower() == "c":
            self.modo = "CD"
            print(f"O {self.modelo} está em modo {self.modo}")
        elif modo[0].lower() == "r":
            self.modo = "RADIO"
            print(f"O {self.modelo} está em modo {self.modo}")
        elif modo[0].lower() == "b":
            self.modo = "BLUETOOTH"
            print(f"O {self.modelo} está em modo {self.modo}")
        else:
            print("Opção Inválida!")
    def sintonizar(self, frequencia):
        if (self.modo == "RADIO") and (
                self.faixa == "AM") and (
                500 <= frequencia <= 1600) and (
                self.estado == "ligado"):
            self.frequencia = frequencia
            print(
            f"Sintonizado na frequência {self.frequencia}KHz na faixa {self.faixa}")
        elif (self.modo == "RADIO") and (
                self.faixa == "FM") and (
                88 <= frequencia <= 108) and (
                self.estado == "ligado"):
            self.frequencia = frequencia
            print(
            f"Sintonizado na frequência {self.frequencia}MHz na faixa {self.faixa}")
        else:
            print(
            f"Não foi possível sintonizar nesta frequencia, tente novamente.")
    def aumentar_volume(self):
        if self.volume < 10:
            self.volume += 1
            print(
            f"{self.modelo} teve seu volume aumentado... Volume atual: {self.volume}")
        else:
            print(f"Seu volume está na altura máxima!")
    def diminuir_volume(self):
        if self.volume >0:
            self.volume -= 1
            print(f"{self.modelo} teve seu volume diminuido... Volume atual: {self.volume}")
        else:
            print(f"Seu volume está na altura mínima!")
    def ligar(self):
        if self.estado == "ligado":
            print(f"{self.modelo} já estava ligado(a)!")
        else:
            self.estado = "ligado"
            print(f"{self.modelo} está {self.estado}")
    def desligar(self):
        if self.estado == "desligado":
            print(f"{self.modelo} já estava desligado(a)!")
        else:
            self.estado = "desligado"
            print(f"{self.modelo} está {self.estado}")


# Atributos rádio 1:
meu_radio = radio()
meu_radio.modelo = "BC-R21"
meu_radio.faixa = "FM"
meu_radio.modo = "RADIO"
meu_radio.frequencia = 101.01
meu_radio.volume = 4
meu_radio.estado = "ligado"


# Atributos rádio 2:
jbl = radio()
jbl.modelo = "Boombox"
jbl.faixa = "AM"
jbl.modo = "RADIO"
jbl.frequencia = 780.00
jbl.volume = 0
jbl.estado = "desligado"


# Métodos para o rádio 1:
meu_radio.mudar_faixa("am")
meu_radio.mudar_modo("Bluetooth")
meu_radio.mudar_modo("Usb")
meu_radio.mudar_modo("Radio")
meu_radio.sintonizar(1300)
meu_radio.aumentar_volume()
meu_radio.diminuir_volume()
meu_radio.ligar()
meu_radio.desligar()


# Métodos para o rádio 2:
jbl.mudar_faixa("fm")
jbl.mudar_modo("Bluetooth")
jbl.mudar_modo("Usb")
jbl.mudar_modo("Radio")
jbl.sintonizar(98.4)
jbl.aumentar_volume()
jbl.diminuir_volume()
jbl.ligar()
jbl.desligar()
