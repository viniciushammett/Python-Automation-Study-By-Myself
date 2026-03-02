from exitcodes import classificar_exit_code

def main():
    entrada = input("Insira o codigo para verificação: ")

    texto, nivel = classificar_exit_code(entrada)

    print(texto)

    if nivel == "critical":
        print("Checar PATH/instalação imediatamente")
    elif nivel == "warning":
        print("Rever parâmetros/execução")
    elif nivel == "unknown":
        print("Analisar documentação do comando")

if __name__ == "__main__":
    main()