def adicionar_compra():
    limpar_tela()
    mostrar_titulo("ADICIONAR COMPRA")

    eventos = separar_eventos()

    if not eventos:
        print("Nenhum evento cadastrado.")
        return

    nome_procurado = input("Digite o nome do evento: ").upper().strip()

    for posicao, evento in enumerate(eventos):
        linhas = evento.split("\n")

        if len(linhas) < 8:
            continue

        if linhas[1] == f"NOME DO EVENTO: {nome_procurado}":
            nome_item = input("Nome do item comprado: ").upper().strip()
            valor_item = pedir_valor_float("Valor do item: R$ ")

            orcamento_atual = linhas[6].replace("ORÇAMENTO ATUAL: R$ ", "")
            orcamento_atual = float(orcamento_atual.replace(",", "."))

            novo_orcamento = orcamento_atual - valor_item

            linhas[6] = f"ORÇAMENTO ATUAL: R$ {novo_orcamento:.2f}"
            linhas.append(f"COMPRA: {nome_item} - R$ {valor_item:.2f}")

            eventos[posicao] = "\n".join(linhas)
            salvar_arquivo("\n\n".join(eventos))

            print("\nCompra adicionada com sucesso!")
            print(f"Item comprado: {nome_item}")
            print(f"Valor da compra: R$ {valor_item:.2f}")
            print(f"Novo orçamento atual: R$ {novo_orcamento:.2f}")
            return

    print("\nEvento não encontrado.")
