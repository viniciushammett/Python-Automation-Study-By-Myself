from ambientes import classificar_ambiente


def main():
    nome = input("Digite o Nome do ambiente: ")

    classificacao, nivel = classificar_ambiente(nome)

    print(classificacao)

    if nivel == "critical":
        print("Atenção: Mudanças exigem Change Management.")

    elif nivel == "test":
        print("Deploy liberado para validação.")

    elif nivel == "unknown":
        print("Verifique o nome do ambiente antes de prosseguir.")


if __name__ == "__main__":
    main()