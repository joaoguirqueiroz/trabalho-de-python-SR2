def relatorio_financeiro():
    limpar_tela()
    mostrar_titulo("RELATÓRIO FINANCEIRO")

    eventos = separar_eventos()

    if not eventos:
        print("Nenhum evento cadastrado.")
        return

    total_orcamento = 0
    total_atual = 0
    evento_mais_caro = ""
    evento_mais_barato = ""
    maior_orcamento = 0
    menor_orcamento = None

    for evento in eventos:
        linhas = evento.split("\n")

        if len(linhas) < 7:
            continue

        nome = linhas[1].replace("NOME DO EVENTO: ", "")
        orcamento_total = float(linhas[5].replace("ORÇAMENTO TOTAL: R$ ", "").replace(",", "."))
        orcamento_atual = float(linhas[6].replace("ORÇAMENTO ATUAL: R$ ", "").replace(",", "."))

        total_orcamento += orcamento_total
        total_atual += orcamento_atual

        if orcamento_total > maior_orcamento:
            maior_orcamento = orcamento_total
            evento_mais_caro = nome

        if menor_orcamento is None or orcamento_total < menor_orcamento:
            menor_orcamento = orcamento_total
            evento_mais_barato = nome

    total_gasto = total_orcamento - total_atual

    print(f"Total de eventos cadastrados: {len(eventos)}")
    print(f"Orçamento total geral: R$ {total_orcamento:.2f}")
    print(f"Orçamento atual geral: R$ {total_atual:.2f}")
    print(f"Total gasto em compras: R$ {total_gasto:.2f}")
    print(f"Evento mais caro: {evento_mais_caro} - R$ {maior_orcamento:.2f}")
    print(f"Evento mais barato: {evento_mais_barato} - R$ {menor_orcamento:.2f}")
