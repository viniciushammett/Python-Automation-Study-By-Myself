from logs import classificar_severidade

def main():
    severidade = input("Insira a criticidade: ")

    # ⚠️ Aqui você sobrescreveu a variável "severidade" com o retorno da função.
    # Não é errado por si só, mas confunde muito: antes era a entrada do usuário,
    # depois vira o "nivel" (ok/warning/critical...). Melhor separar em nomes:
    # entrada, nivel.
    texto, severidade = classificar_severidade(severidade)

    print(texto)

    # ❌ Aqui está o erro MAIS importante:
    # Você está comparando severidade com "ok/error/warn/debug/unknown"
    # Só que no seu logs.py você retorna "critical/warning/ok/debug/unknown"
    # Exemplo: input "error" vira retorno ("Falha Detectada", "critical")
    # Então severidade nunca vai ser "error", vai ser "critical".
    if severidade == "ok":
        print("Informativo")
    
    # ❌ Nunca vai entrar aqui, porque "error" NÃO é um nível retornado.
    # O nível retornado é "critical".
    elif severidade == "error":
        print("Falha Detectada")
    
    # ❌ Mesmo problema: você compara com "warn", mas o retorno é "warning"
    elif severidade == "warn":
        print("Atenção")
    
    # ✅ debug aqui até poderia funcionar, porque você retorna "debug" mesmo,
    # mas a lógica geral ficou inconsistente.
    elif severidade == "debug":
        print("Depuração")
    
    # ✅ unknown também poderia funcionar, mas só nos casos que você retornasse.
    elif severidade == "unknown":
        print("Nivel Desconhecido")

if __name__ == "__main__":
    main()