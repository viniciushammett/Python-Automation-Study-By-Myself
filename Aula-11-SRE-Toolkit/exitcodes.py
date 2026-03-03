def classificar_exit_code(code):
    mapa_codigo = {
        200: ("Saudável", "ok"),
        500: ("Erro Interno", "critical"),
        404: ("Não Encontrado", "warning")
    }

    return mapa_codigo.get(code, ("Código desconhecido", "unknown"))