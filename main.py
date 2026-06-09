import os
import random
from datetime import datetime

ARQUIVO_EVENTOS = "Sistema de Eventos.txt"

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def pausar():
    input("\nPressione ENTER para continuar...")

def mostrar_titulo(titulo):
    print("#" * 50)
    print(titulo.center(50))
    print("#" * 50)

def validar_data():
    while True:
        data = input("Digite a data do evento (DD/MM/AAAA): ").strip()
        try:
            datetime.strptime(data, "%d/%m/%Y")
            return data
        except ValueError:
            print("Data inválida! Use DD/MM/AAAA.")

def calcular_dias_restantes(data_evento):
    try:
        data = datetime.strptime(data_evento, "%d/%m/%Y").date()
        hoje = datetime.today().date()
        diferenca = data - hoje

        if diferenca.days > 0:
            return f"Faltam {diferenca.days} dias"
        elif diferenca.days == 0:
            return "É HOJE!"
        else:
            return f"Aconteceu há {abs(diferenca.days)} dias"
    except ValueError:
        return "Data inválida"

def pedir_valor_float(mensagem):
    while True:
        try:
            return float(input(mensagem).replace(",", "."))
        except ValueError:
            print("Digite um valor válido.")

def pedir_duracao():
    while True:
        try:
            horas = int(input("Duração do evento em horas: "))
            if horas > 0:
                return horas
            print("A duração deve ser maior que zero.")
        except ValueError:
            print("Digite um número inteiro válido.")

def criar_arquivo():
    with open(ARQUIVO_EVENTOS, "a", encoding="utf-8"):
        pass

def ler_arquivo():
    with open(ARQUIVO_EVENTOS, "r", encoding="utf-8") as arquivo:
        return arquivo.read()

def salvar_arquivo(conteudo):
    with open(ARQUIVO_EVENTOS, "w", encoding="utf-8") as arquivo:
        arquivo.write(conteudo)

def separar_eventos():
    conteudo = ler_arquivo()
    if conteudo.strip() == "":
        return []
    return conteudo.split("\n\n")

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

def editar_evento():
    limpar_tela()
    mostrar_titulo("EDITAR EVENTO")

    eventos = separar_eventos()
    nome_procurado = input("Digite o nome do evento que deseja editar: ").upper().strip()

    for posicao, evento in enumerate(eventos):
        linhas = evento.split("\n")

        if len(linhas) < 8:
            continue

        if linhas[1] == f"NOME DO EVENTO: {nome_procurado}":
            nome_atual = linhas[1].replace("NOME DO EVENTO: ", "")
            tipo_atual = linhas[2].replace("TIPO DO EVENTO: ", "")
            data_atual = linhas[3].replace("DATA DO EVENTO: ", "").split(" - ")[0]
            local_atual = linhas[4].replace("LOCAL DO EVENTO: ", "")
            orcamento_total = linhas[5].replace("ORÇAMENTO TOTAL: R$ ", "")
            orcamento_atual = linhas[6].replace("ORÇAMENTO ATUAL: R$ ", "")
            duracao_atual = linhas[7].replace("DURAÇÃO: ", "").replace(" horas", "")

            print("\nDeixe vazio para manter o valor atual.\n")

            novo_nome = input(f"Novo nome [{nome_atual}]: ").upper().strip() or nome_atual
            novo_tipo = input(f"Novo tipo [{tipo_atual}]: ").upper().strip() or tipo_atual
            nova_data = input(f"Nova data [{data_atual}]: ").strip() or data_atual
            novo_local = input(f"Novo local [{local_atual}]: ").upper().strip() or local_atual
            novo_orcamento_total = input(f"Novo orçamento total [{orcamento_total}]: ").strip() or orcamento_total
            novo_orcamento_atual = input(f"Novo orçamento atual [{orcamento_atual}]: ").strip() or orcamento_atual
            nova_duracao = input(f"Nova duração [{duracao_atual}]: ").strip() or duracao_atual

            novo_orcamento_total = float(novo_orcamento_total.replace(",", "."))
            novo_orcamento_atual = float(novo_orcamento_atual.replace(",", "."))
            nova_duracao = int(nova_duracao)

            status = calcular_dias_restantes(nova_data)
            media = novo_orcamento_total / nova_duracao
            compras_antigas = linhas[9:]

            evento_editado = (
                "Dados do Evento:"
                f"\nNOME DO EVENTO: {novo_nome}"
                f"\nTIPO DO EVENTO: {novo_tipo}"
                f"\nDATA DO EVENTO: {nova_data} - {status}"
                f"\nLOCAL DO EVENTO: {novo_local}"
                f"\nORÇAMENTO TOTAL: R$ {novo_orcamento_total:.2f}"
                f"\nORÇAMENTO ATUAL: R$ {novo_orcamento_atual:.2f}"
                f"\nDURAÇÃO: {nova_duracao} horas"
                f"\nMÉDIA PRIORIDADE: {media:.2f}"
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

def sugerir_evento():
    limpar_tela()
    mostrar_titulo("SUGESTÃO DE EVENTO")

    categoria = input("Categoria (social, empresarial ou educacional): ").lower().strip()

    eventos = {
        "social": [
            "CASAMENTO",
            "ANIVERSÁRIO",
            "CHÁ REVELAÇÃO",
            "FORMATURA"
        ],
        "empresarial": [
            "CONFRATERNIZAÇÃO",
            "FEIRA DE NEGÓCIOS",
            "LANÇAMENTO DE PRODUTO"
        ],
        "educacional": [
            "PALESTRA",
            "WORKSHOP",
            "MINICURSO",
            "SEMINÁRIO"
        ]
    }

    if categoria in eventos:
        print(f"\nSugestão: {random.choice(eventos[categoria])}")
    else:
        print("\nCategoria inválida.")

def menu_principal():
    criar_arquivo()

    while True:
        limpar_tela()

        print("=" * 50)
        print("ORGANIZA FESTA".center(50))
        print("=" * 50)

        print("[1] Adicionar evento")
        print("[2] Visualizar eventos")
        print("[3] Editar evento")
        print("[4] Excluir evento")
        print("[5] Relatório financeiro")
        print("[6] Adicionar compra")
        print("[7] Sugestão de evento")
        print("[0] Sair")

        print("=" * 50)

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
            print("\nSistema finalizado. Até mais!")
            break
        else:
            print("\nOpção inválida!")

        pausar()

menu_principal()
