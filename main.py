import os
import random
from datetime import datetime

ARQUIVO_EVENTOS = "eventos.txt"

SUGESTOES_EVENTOS = {
    "privados": [
        "Casamento",
        "Aniversário",
        "Resenha",
        "Carnaval entre amigos",
        "Encontro familiar"
    ],
    "publico": [
        "Carnaval",
        "São João",
        "Show aberto",
        "Natal",
        "Ano Novo",
        "7 de Setembro"
    ],
    "restrito": [
        "Reuniões empresariais",
        "Reunião política",
        "Festas VIP",
        "Camarim de shows"
    ]
}

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def pausar():
    input("\nPressione ENTER para continuar...")

def cabecalho(texto):
    print("#" * 50)
    print(texto.center(50))
    print("#" * 50)

def sim_ou_nao(pergunta):
    while True:
        resposta = input(pergunta).strip().lower()

        if resposta in ["sim", "s"]:
            return "Sim"

        if resposta in ["nao", "não", "n"]:
            return "Não"

        print("Digite apenas SIM ou NÃO.")

def pedir_valor_float(mensagem):
    while True:
        try:
            return float(input(mensagem).replace(",", "."))
        except ValueError:
            print("Digite um valor numérico válido.")

def pedir_duracao():
    while True:
        try:
            horas = int(input("Duração do evento (horas): "))
            if horas > 0:
                return horas

            print("Digite um valor maior que zero.")

        except ValueError:
            print("Digite apenas números inteiros.")

def validar_data():
    while True:
        data = input("Digite a data do evento (DD/MM/AAAA): ").strip()

        try:
            datetime.strptime(data, "%d/%m/%Y")
            return data

        except ValueError:
            print("Data inválida.")

def calcular_dias_restantes(data_evento):
    try:
        data = datetime.strptime(data_evento, "%d/%m/%Y").date()
        hoje = datetime.today().date()

        diferenca = data - hoje

        if diferenca.days > 0:
            return f"Faltam {diferenca.days} dias"

        elif diferenca.days == 0:
            return "Evento acontece hoje"

        else:
            return f"Evento ocorreu há {abs(diferenca.days)} dias"

    except ValueError:
        return "Data inválida"

def obter_prioridade(evento):
    linhas = evento.split("\n")

    for linha in linhas:
        if linha.startswith("NÍVEL DE PRIORIDADE:"):
            try:
                return float(
                    linha.replace(
                        "NÍVEL DE PRIORIDADE:",
                        ""
                    ).strip()
                )

            except ValueError:
                return 0

    return 0

def criar_arquivo():
    with open(
        ARQUIVO_EVENTOS,
        "a",
        encoding="utf-8"
    ):
        pass

def ler_arquivo():
    with open(
        ARQUIVO_EVENTOS,
        "r",
        encoding="utf-8"
    ) as arquivo:

        return arquivo.read()

def salvar_arquivo(conteudo):
    with open(
        ARQUIVO_EVENTOS,
        "w",
        encoding="utf-8"
    ) as arquivo:

        arquivo.write(conteudo)

def separar_eventos():
    conteudo = ler_arquivo()

    if conteudo.strip() == "":
        return []

    return conteudo.split("\n\n")


def adicionar_evento():
    limpar_tela()
    cabecalho("ADICIONAR EVENTO")

    nome = input("Nome do evento: ").upper().strip()
    tipo = input("Tipo do evento: ").upper().strip()
    data = validar_data()
    local = input("Local do evento: ").upper().strip()
    orcamento_total = pedir_valor_float("Orçamento total: R$ ")
    duracao = pedir_duracao()

    buffet = sim_ou_nao("Terá buffet? (Sim/Não): ")

    if buffet == "Sim":
        itens_buffet = input("Itens do buffet: ").upper().strip()
    else:
        itens_buffet = "NÃO POSSUI"

    musica = sim_ou_nao("Terá música ao vivo? (Sim/Não): ")

    if musica == "Sim":
        estilo_musical = input("Estilo musical: ").upper().strip()
    else:
        estilo_musical = "NÃO POSSUI"

    palco = sim_ou_nao("Terá palco? (Sim/Não): ")
    ingressos = sim_ou_nao("Terá venda de ingressos? (Sim/Não): ")

    while True:
        try:
            convidados = int(input("Quantidade de convidados: "))
            if convidados > 0:
                break
            print("Digite uma quantidade maior que zero.")
        except ValueError:
            print("Digite apenas números inteiros.")

    status = calcular_dias_restantes(data)
    prioridade = orcamento_total / duracao

    novo_evento = (
        "DADOS DO EVENTO:"
        f"\nNOME DO EVENTO: {nome}"
        f"\nTIPO DO EVENTO: {tipo}"
        f"\nDATA DO EVENTO: {data} - {status}"
        f"\nLOCAL DO EVENTO: {local}"
        f"\nORÇAMENTO TOTAL: R$ {orcamento_total:.2f}"
        f"\nORÇAMENTO ATUAL: R$ {orcamento_total:.2f}"
        f"\nDURAÇÃO: {duracao} horas"
        f"\nNÍVEL DE PRIORIDADE: {prioridade:.2f}"
        f"\nBUFFET: {buffet}"
        f"\nITENS DO BUFFET: {itens_buffet}"
        f"\nMÚSICA AO VIVO: {musica}"
        f"\nESTILO MUSICAL: {estilo_musical}"
        f"\nPALCO: {palco}"
        f"\nVENDA DE INGRESSOS: {ingressos}"
        f"\nQUANTIDADE DE CONVIDADOS: {convidados}"
    )

    conteudo = ler_arquivo()

    if conteudo.strip() == "":
        conteudo = novo_evento
    else:
        conteudo += "\n\n" + novo_evento

    salvar_arquivo(conteudo)

    print("\nEvento cadastrado com sucesso!")


def visualizar_eventos():
    limpar_tela()
    cabecalho("EVENTOS CADASTRADOS")

    eventos = separar_eventos()

    if not eventos:
        print("Nenhum evento cadastrado ainda.")
        return

    eventos.sort(key=obter_prioridade, reverse=True)

    for posicao, evento in enumerate(eventos, start=1):
        print(f"\nPRIORIDADE #{posicao}")
        print("-" * 50)
        print(evento)


def editar_evento():
    limpar_tela()
    cabecalho("EDITAR EVENTO")

    eventos = separar_eventos()

    if not eventos:
        print("Nenhum evento cadastrado ainda.")
        return

    nome_procurado = input("Nome do evento que deseja editar: ").upper().strip()

    for posicao, evento in enumerate(eventos):
        linhas = evento.split("\n")

        if len(linhas) < 15:
            continue

        if linhas[1] == f"NOME DO EVENTO: {nome_procurado}":
            nome_atual = linhas[1].replace("NOME DO EVENTO: ", "")
            tipo_atual = linhas[2].replace("TIPO DO EVENTO: ", "")
            data_atual = linhas[3].replace("DATA DO EVENTO: ", "").split(" - ")[0]
            local_atual = linhas[4].replace("LOCAL DO EVENTO: ", "")
            orcamento_total_atual = linhas[5].replace("ORÇAMENTO TOTAL: R$ ", "")
            orcamento_atual = linhas[6].replace("ORÇAMENTO ATUAL: R$ ", "")
            duracao_atual = linhas[7].replace("DURAÇÃO: ", "").replace(" horas", "")
            buffet_atual = linhas[9].replace("BUFFET: ", "")
            itens_buffet_atual = linhas[10].replace("ITENS DO BUFFET: ", "")
            musica_atual = linhas[11].replace("MÚSICA AO VIVO: ", "")
            estilo_musical_atual = linhas[12].replace("ESTILO MUSICAL: ", "")
            palco_atual = linhas[13].replace("PALCO: ", "")
            ingressos_atual = linhas[14].replace("VENDA DE INGRESSOS: ", "")
            convidados_atual = linhas[15].replace("QUANTIDADE DE CONVIDADOS: ", "")
            compras_antigas = linhas[16:]

            print("\nDeixe em branco para manter o valor atual.\n")

            novo_nome = input(f"Novo nome [{nome_atual}]: ").upper().strip() or nome_atual
            novo_tipo = input(f"Novo tipo [{tipo_atual}]: ").upper().strip() or tipo_atual
            nova_data = input(f"Nova data [{data_atual}]: ").strip() or data_atual
            novo_local = input(f"Novo local [{local_atual}]: ").upper().strip() or local_atual
            novo_orcamento_total = input(f"Novo orçamento total [{orcamento_total_atual}]: ").strip() or orcamento_total_atual
            novo_orcamento_atual = input(f"Novo orçamento atual [{orcamento_atual}]: ").strip() or orcamento_atual
            nova_duracao = input(f"Nova duração [{duracao_atual}]: ").strip() or duracao_atual
            novo_buffet = input(f"Possui buffet [{buffet_atual}]: ").strip() or buffet_atual
            novo_buffet = novo_buffet.capitalize()

            if novo_buffet == "Sim":
                novos_itens_buffet = input(f"Itens do buffet [{itens_buffet_atual}]: ").upper().strip() or itens_buffet_atual
            else:
                novos_itens_buffet = "NÃO POSSUI"

            nova_musica = input(f"Música ao vivo [{musica_atual}]: ").strip() or musica_atual
            nova_musica = nova_musica.capitalize()

            if nova_musica == "Sim":
                novo_estilo_musical = input(f"Estilo musical [{estilo_musical_atual}]: ").upper().strip() or estilo_musical_atual
            else:
                novo_estilo_musical = "NÃO POSSUI"

            novo_palco = input(f"Palco [{palco_atual}]: ").strip() or palco_atual
            novo_palco = novo_palco.capitalize()

            novos_ingressos = input(f"Venda de ingressos [{ingressos_atual}]: ").strip() or ingressos_atual
            novos_ingressos = novos_ingressos.capitalize()

            novos_convidados = input(f"Quantidade de convidados [{convidados_atual}]: ").strip() or convidados_atual

            novo_orcamento_total = float(novo_orcamento_total.replace(",", "."))
            novo_orcamento_atual = float(novo_orcamento_atual.replace(",", "."))
            nova_duracao = int(nova_duracao)

            status = calcular_dias_restantes(nova_data)
            prioridade = novo_orcamento_total / nova_duracao



            evento_editado = (
                "DADOS DO EVENTO:"
                f"\nNOME DO EVENTO: {novo_nome}"
                f"\nTIPO DO EVENTO: {novo_tipo}"
                f"\nDATA DO EVENTO: {nova_data} - {status}"
                f"\nLOCAL DO EVENTO: {novo_local}"
                f"\nORÇAMENTO TOTAL: R$ {novo_orcamento_total:.2f}"
                f"\nORÇAMENTO ATUAL: R$ {novo_orcamento_atual:.2f}"
                f"\nDURAÇÃO: {nova_duracao} horas"
                f"\nNÍVEL DE PRIORIDADE: {prioridade:.2f}"
                f"\nBUFFET: {novo_buffet}"
                f"\nITENS DO BUFFET: {novos_itens_buffet}"
                f"\nMÚSICA AO VIVO: {nova_musica}"
                f"\nESTILO MUSICAL: {novo_estilo_musical}"
                f"\nPALCO: {novo_palco}"
                f"\nVENDA DE INGRESSOS: {novos_ingressos}"
                f"\nQUANTIDADE DE CONVIDADOS: {novos_convidados}"
            )

            if compras_antigas:
                evento_editado += "\n" + "\n".join(compras_antigas)

            eventos[posicao] = evento_editado
            salvar_arquivo("\n\n".join(eventos))

            print("\nEvento editado com sucesso!")
            return

    print("\nEvento não encontrado.")


def excluir_evento():
    limpar_tela()
    cabecalho("EXCLUIR EVENTO")

    eventos = separar_eventos()

    if not eventos:
        print("Nenhum evento cadastrado ainda.")
        return

    nome_excluir = input("Nome do evento que deseja excluir: ").upper().strip()

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


def relatorio_financeiro():
    limpar_tela()
    cabecalho("RELATÓRIO FINANCEIRO")

    eventos = separar_eventos()

    if not eventos:
        print("Nenhum evento cadastrado ainda.")
        return

    total_orcamento = 0
    total_atual = 0
    maior_orcamento = 0
    menor_orcamento = None
    evento_mais_caro = ""
    evento_mais_barato = ""

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

    print(f"\nTotal de eventos cadastrados: {len(eventos)}")
    print(f"Orçamento total geral: R$ {total_orcamento:.2f}")
    print(f"Orçamento disponível geral: R$ {total_atual:.2f}")
    print(f"Total gasto em compras: R$ {total_gasto:.2f}")
    print(f"Evento mais caro: {evento_mais_caro} - R$ {maior_orcamento:.2f}")
    print(f"Evento mais barato: {evento_mais_barato} - R$ {menor_orcamento:.2f}")


def adicionar_compra():
    limpar_tela()
    cabecalho("ADICIONAR COMPRA")

    eventos = separar_eventos()

    if not eventos:
        print("Nenhum evento cadastrado ainda.")
        return

    nome_procurado = input("Nome do evento: ").upper().strip()

    for posicao, evento in enumerate(eventos):
        linhas = evento.split("\n")

        if len(linhas) < 8:
            continue

        if linhas[1] == f"NOME DO EVENTO: {nome_procurado}":
            nome_item = input("Item comprado: ").upper().strip()
            valor_item = pedir_valor_float("Valor do item: R$ ")

            saldo_atual = float(linhas[6].replace("ORÇAMENTO ATUAL: R$ ", "").replace(",", "."))
            novo_saldo = saldo_atual - valor_item

            linhas[6] = f"ORÇAMENTO ATUAL: R$ {novo_saldo:.2f}"
            linhas.append(f"COMPRA: {nome_item} - R$ {valor_item:.2f}")

            eventos[posicao] = "\n".join(linhas)
            salvar_arquivo("\n\n".join(eventos))

            print(f"\nCompra registrada: {nome_item}")
            print(f"Valor descontado: R$ {valor_item:.2f}")
            print(f"Saldo restante: R$ {novo_saldo:.2f}")
            return

    print("\nEvento não encontrado.")


def sugerir_evento():
    limpar_tela()
    cabecalho("SUGESTÃO DE EVENTO")

    categoria = input("Informe a categoria (privados, publico ou restrito): ").lower().strip()

    if categoria in SUGESTOES_EVENTOS:
        sugestao = random.choice(SUGESTOES_EVENTOS[categoria])
        print(f"\nSugestão para '{categoria}': {sugestao}")
    else:
        print("\nCategoria inválida. Use: privados, publico ou restrito.")


def menu_principal():
    criar_arquivo()

    while True:
        limpar_tela()

        print("*" * 50)
        print("ORGANIZA FESTA".center(50))
        print("*" * 50)

        print("[1] Adicionar evento")
        print("[2] Visualizar eventos")
        print("[3] Editar evento")
        print("[4] Excluir evento")
        print("[5] Relatório financeiro")
        print("[6] Adicionar compra")
        print("[7] Sugestão de evento")
        print("[0] Sair")

        print("*" * 50)

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            adicionar_evento()
        elif opcao == "2":
            visualizar_eventos()
        elif opcao == "3":
            editar_evento()
        elif opcao == "4":
            excluir_evento()
        elif opcao == "5":
            relatorio_financeiro()
        elif opcao == "6":
            adicionar_compra()
        elif opcao == "7":
            sugerir_evento()
        elif opcao == "0":
            print("\nAté a próxima!")
            break
        else:
            print("\nOpção inválida! Tente novamente.")

        pausar()


menu_principal()
