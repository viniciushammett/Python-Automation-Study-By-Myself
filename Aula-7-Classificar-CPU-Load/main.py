from cpu import classificar_cpu

def main():
    entrada = input("Insira o CPU load (ex: 0.8, 1.4, 2.9): ")

    texto, nivel = classificar_cpu(entrada)

    print(texto)

    if nivel == "warning":
        print("Avaliar escala/otimização.")
    elif nivel == "critical":
        print("Escalar imediatamente.")
    elif nivel == "unknown":
        print("Validar entrada.")

if __name__ == "__main__":
    main()