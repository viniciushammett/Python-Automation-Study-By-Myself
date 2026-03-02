from servicos import verificador_servico

def main():
    nome = input("Digite o nome do serviço: ")
    resultado = verificador_servico(nome)
    print(resultado)

if __name__ == "__main__":
    main()