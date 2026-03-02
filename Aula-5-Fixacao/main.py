from status import classificar_status


def main():
    codigo = input("Digite o código HTTP: ")

    texto, nivel = classificar_status(codigo)

    print(texto)

    if nivel == "ok":
        print("Tudo certo, serviço está respondendo.")

    elif nivel == "critical":
        print("Abrir incidente imediatamente.")

    elif nivel == "warning":
        print("Verificar rota ou endpoint.")

    elif nivel == "unknown":
        print("Investigar comportamento inesperado.")


if __name__ == "__main__":
    main()