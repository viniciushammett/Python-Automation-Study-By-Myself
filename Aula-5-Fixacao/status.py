def classificar_status(codigo_str):
    try:
        codigo = int(codigo_str)
    except ValueError:
        return "Entrada inválida", "unknown"

    mapa_status = {
        200: ("Saudável", "ok"),
        500: ("Erro Interno", "critical"),
        404: ("Não Encontrado", "warning")
    }

    if codigo in mapa_status:
        return mapa_status[codigo]

    return mapa_status.get(codigo, ("Status Desconhecido", "unknown"))