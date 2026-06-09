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


def listar_eventos():
    limpar_tela()

    print("=" * 30)
    print("LISTA DE EVENTOS")
    print("=" * 30)

    if len(eventos) == 0:
        print("Nenhum evento cadastrado.")
    else:
        for i, evento in enumerate(eventos):
            print(f"{i + 1}. {evento['titulo']}")
            print(f"Tipo: {evento['tipo']}")
            print(f"Data: {evento['data']}")
            print(f"Local: {evento['local']}")
            print(f"Orçamento: R$ {evento['orcamento']:.2f}")
            print("-" * 30)