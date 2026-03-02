def classificar_ambiente(ambiente_str):
    
    nome_ambiente = ambiente_str.strip().lower()

    ambiente_critico = ["prod", "production"]
    ambiente_teste = ["staging", "qa"]
    ambiente_dev = ["dev", "development"]

    if nome_ambiente in ambiente_critico:
        return "Ambiente Crítico", "critical"
    
    if nome_ambiente in ambiente_teste:
        return "Ambiente de Teste", "test"
    
    if nome_ambiente in ambiente_dev:
        return "Ambiente de Desenvolvimento", "ok"
    
    return "Ambiente Desconhecido", "unknown"