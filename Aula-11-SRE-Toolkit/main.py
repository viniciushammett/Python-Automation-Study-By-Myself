import argparse
from exitcodes import classificar_exit_code

def main():
    parser = argparse.ArgumentParser(description="Classificador de HTTP Status Code")
    parser.add_argument("codigo", type=int, help="Código HTTP para classificar")

    args = parser.parse_args()

    descricao, severidade = classificar_exit_code(args.codigo)

    print(f"Descrição: {descricao}")
    print(f"Severidade: {severidade}")

if __name__ == "__main__":
    main()