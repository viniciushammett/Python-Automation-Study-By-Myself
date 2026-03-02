def classificar_ambiente(nome_ambiente):

    # Normaliza a entrada
    nome_ambiente = nome_ambiente.lower()

    ambiente_critico = ["prod", "production"] 
    ambiente_teste = ["staging", "qa"]

    if nome_ambiente in ambiente_critico:
        return "Serviço critico"
    if nome_ambiente in ambiente_teste:
        return "Ambiente Teste"
    
        return "Ambiente Desconhecido"
