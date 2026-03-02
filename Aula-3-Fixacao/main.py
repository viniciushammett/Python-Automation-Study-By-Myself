from ambientes import classificar_ambiente

def main():
    nome = input("Digite o Nome do ambiente: ")
    resultado = classificar_ambiente (nome)
    print(resultado)

if __name__ == "__main__":
    main()