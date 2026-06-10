orcamento = pedir_valor_float("Orçamento do evento: R$ ")
    duracao = pedir_duracao()

    media = orcamento / duracao



def obter_media_evento(evento):
    linhas = evento.split("\n")

    for linha in linhas:
        if linha.startswith("MÉDIA PRIORIDADE:"):
            try:
                return float(linha.replace("MÉDIA PRIORIDADE:", "").strip())
            except ValueError:
                return 0
    return 0
