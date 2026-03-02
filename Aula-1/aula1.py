def verificar_servico(nome_servico):

    if nome_servico == "api":
        return "Serviço Critico"
    else:
        return "Serviço comum"
    
def main():

    nome = input("Digite o nome do serviço: ")

    resultado = verificar_servico(nome)

    print(resultado)

if __name__ == "__main__":
    main()