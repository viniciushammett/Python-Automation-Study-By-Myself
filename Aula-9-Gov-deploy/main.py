from ambientes import classificar_ambiente

def main():
    nome = input("Digite o Nome do Ambiente: ")

    classificacao, nivel = classificar_ambiente(nome)
    print(classificacao)

    if nivel == "critical":
        print("Exigir Change + Aprovação")
    
    elif nivel == "test":
        print("Liberar para aprovação")
    
    elif nivel == "ok":
        print("Deploy permitido com cautela")
    
    elif nivel == "unknown":
        print ("Bloquear até confirmar")


if __name__ == "__main__":
    main()