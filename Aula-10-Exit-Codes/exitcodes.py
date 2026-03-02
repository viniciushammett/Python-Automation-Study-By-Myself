def classificar_exit_code(code_str):
    nivel_str = code_str.strip()

    try:
        code = int(nivel_str)
    except ValueError:
        return "Entrada Invalida", "unknown"
    
    mapa_codigo = {
        0: ("Sucesso", "ok"),
        2: ("Uso incorreto", "warning"),
        1: ("Erro Generico", "warning"),
        127: ("Comando não encontrado", "critical")
    }

    return mapa_codigo.get(code, ("Código desconhecido", "unknown"))