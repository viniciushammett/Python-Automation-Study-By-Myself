def classificar_cpu(load_str):
    valor_str = load_str.strip()

    try:
        load = float(valor_str)
    except ValueError:
        return "Entrada inválida", "unknown"

    if load < 1.0:
        return "Normal", "ok"
    elif load < 2.0:
        return "Alto", "warning"
    else:
        return "Crítico", "critical"