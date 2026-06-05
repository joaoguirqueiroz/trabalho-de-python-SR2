import os
import datetime

eventos = []

def limpar_tela():
    os.system("cls")


def adicionar_evento():
    limpar_tela()

    print("=" * 30)
    print("ADICIONAR EVENTO")
    print("=" * 30)

    titulo = input("Digite o título do evento: ")
    tipo = input("Digite o tipo do evento: ")
    data = input("Digite a data do evento: ")
    local = input("Digite o local do evento: ")
    orcamento = float(input("Digite o orçamento: R$ "))

    evento = {
        "titulo": titulo,
        "tipo": tipo,
        "data": data,
        "local": local,
        "orcamento": orcamento
    }

    eventos.append(evento)

    print("Evento adicionado com sucesso!")