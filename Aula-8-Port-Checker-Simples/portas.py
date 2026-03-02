def port_checker(port_str):

    try:
        port = int(port_str)
    except ValueError:
        return "Entrada inválida", "unknown"
    
    mapa_portas = {
        22: ("SSH", "ok"),
        80: ("HTTP", "ok"),
        443: ("HTTPS", "ok"),
        5432: ("Postgres", "warning")
    }

    return mapa_portas.get(port, ("Serviço desconhecido", "unknown"))