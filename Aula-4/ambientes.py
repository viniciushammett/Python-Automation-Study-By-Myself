def classificar_ambiente(nome_ambiente):
    nome_ambiente = nome_ambiente.strip().lower()

    ambiente_critico = ["prod", "production"]
    ambiente_teste = ["staging", "qa"]

    if nome_ambiente in ambiente_critico:
        return "Ambiente Crítico", "critical"

    if nome_ambiente in ambiente_teste:
        return "Ambiente de Teste", "test"

    return "Ambiente Desconhecido", "unknown"