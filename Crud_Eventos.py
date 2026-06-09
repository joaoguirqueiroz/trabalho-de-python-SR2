def adicionar_evento():
    limpar_tela()
    mostrar_titulo("ADICIONAR EVENTO")

    nome = input("Nome do evento: ").upper().strip()
    tipo = input("Tipo do evento: ").upper().strip()
    data = validar_data()
    local = input("Local do evento: ").upper().strip()
    orcamento = pedir_valor_float("Orçamento do evento: R$ ")
    duracao = pedir_duracao()

    media = orcamento / duracao
    status = calcular_dias_restantes(data)

    novo_evento = (
        "Dados do Evento:"
        f"\nNOME DO EVENTO: {nome}"
        f"\nTIPO DO EVENTO: {tipo}"
        f"\nDATA DO EVENTO: {data} - {status}"
        f"\nLOCAL DO EVENTO: {local}"
        f"\nORÇAMENTO TOTAL: R$ {orcamento:.2f}"
        f"\nORÇAMENTO ATUAL: R$ {orcamento:.2f}"
        f"\nDURAÇÃO: {duracao} horas"
        f"\nMÉDIA PRIORIDADE: {media:.2f}"
    )

    conteudo = ler_arquivo()

    if conteudo.strip() == "":
        conteudo = novo_evento
    else:
        conteudo += "\n\n" + novo_evento

    salvar_arquivo(conteudo)
    print("\nEvento cadastrado com sucesso!")

def obter_media_evento(evento):
    linhas = evento.split("\n")

    for linha in linhas:
        if linha.startswith("MÉDIA PRIORIDADE:"):
            try:
                return float(linha.replace("MÉDIA PRIORIDADE:", "").strip())
            except ValueError:
                return 0
    return 0

def visualizar_eventos():
    limpar_tela()
    mostrar_titulo("EVENTOS CADASTRADOS")

    eventos = separar_eventos()

    if not eventos:
        print("Nenhum evento cadastrado.")
        return

    eventos.sort(key=obter_media_evento, reverse=True)

    for posicao, evento in enumerate(eventos, start=1):
        print(f"\nPRIORIDADE #{posicao}")
        print("-" * 50)
        print(evento)

def excluir_evento():
    limpar_tela()
    mostrar_titulo("EXCLUIR EVENTO")

    eventos = separar_eventos()
    nome_excluir = input("Digite o nome do evento que deseja excluir: ").upper().strip()

    eventos_restantes = []
    removido = False

    for evento in eventos:
        if f"NOME DO EVENTO: {nome_excluir}" in evento:
            removido = True
        else:
            eventos_restantes.append(evento)

    salvar_arquivo("\n\n".join(eventos_restantes))

    if removido:
        print("\nEvento excluído com sucesso!")
    else:
        print("\nEvento não encontrado.")
