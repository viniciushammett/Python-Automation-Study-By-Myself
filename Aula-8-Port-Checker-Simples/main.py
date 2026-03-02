from portas import port_checker

def main():
    entrada = input("Insira a porta para verificar: ")

    texto, nivel = port_checker(entrada)

    print(texto)

    if nivel == "warning":
        print("Revisar regras de firewall.")

    elif nivel == "unknown":
        print("Mapear serviço antes de liberar.")

if __name__ == "__main__":
    main()