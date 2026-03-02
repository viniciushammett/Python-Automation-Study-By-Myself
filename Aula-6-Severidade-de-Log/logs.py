def classificar_severidade(severidade_str):
    severidade = severidade_str.strip().lower()

    mapa_severidade = {
        "error": ("Falha Detectada", "critical"),
        "warn": ("Atenção", "warning"),
        "info": ("Informativo", "ok"),
        "debug": ("Depuração", "debug"),
    }

    return mapa_severidade.get(severidade, ("Nível Desconhecido", "unknown"))

    # ❌ Esse try/except não vai funcionar do jeito que você imagina.
    # str(...) praticamente nunca levanta ValueError.
    # Então esse except aqui é "código morto" (nunca vai rodar).


    mapa_severidade = {
        "error": ("Falha Detectada", "critical"),
        "warn": ("Atenção", "warning"),
        "info": ("Informativo", "ok"),
        "debug": ("Depuração", "debug"),

        # ❌ Esse "others" não vai ser usado porque o usuário não digita "others".
        # E você nem usa .get() com fallback, então esse item não resolve.
        "others": ("Nivel Desconhecido", "unknown")
    }

    # ❌ Aqui faltou normalizar: severidade deveria ser severidade_str.strip().lower()
    # Senão " ERROR " ou "Warn" não bate no dicionário.
    if severidade in mapa_severidade:
        return mapa_severidade[severidade]

    # ❌ Outro bug importante: se NÃO estiver no mapa, a função não retorna nada.
    # Em Python isso vira "None", e o main quebra quando tentar desempacotar:
    # texto, severidade = None  -> erro.