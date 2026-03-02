def verificador_servico(nome_servico):

    servicos_criticos = ["api", "auth", "payment"]

    if nome_servico in servicos_criticos:
        return "Serviço Critico"
    
    return "Serviço comum"