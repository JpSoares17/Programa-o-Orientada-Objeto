class contato:
    # Estados:
    nome = None
    cidade = None
    estado = None
    telefone = None


class agenda:
    # Estados:
    lista_de_contatos = []

    #Métodos:
    def adicionar(self):
        pessoa = contato()
        pessoa.nome = input("Digite o nome da pessoa: ").strip()
        pessoa.cidade = input("Digite a cidade da pessoa: ").strip()
        pessoa.estado = input("Digite o Estado da pessoa:").strip()
        pessoa.telefone = input("Digite o telefone da pessoa: ").strip()
        self.lista_de_contatos.append(pessoa)
    def mostrar_lista(self):
        for pessoa in self.lista_de_contatos:
            cidade = f"{pessoa.cidade}({pessoa.estado})"
            print(f"{pessoa.nome:<25}", end="")
            print(f"{cidade:<30}", end="")
            print(f"{pessoa.telefone:<}")


def main():
    # Leitura/Processamento
    minha_agenda = agenda()
    minha_agenda.adicionar()
    minha_agenda.mostrar_lista()


if __name__ == "__main__":
    main()
