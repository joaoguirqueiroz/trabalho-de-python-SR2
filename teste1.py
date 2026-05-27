import os
from datetime import datetime

eventos = []

def limpar_tela():
    os.system("cls")

def adicionar_evento():
   limpar_tela()
print("#" * 30)
print(" " * 5, "ADICIONAR EVENTO")
print("#" * 30)

titulo = input("Digite o título do evento: ")
tipo = input("Digite o tipo do evento (Palestra, Workshop, etc.): ")
data = input("Digite a data do evento (DD/MM/AAAA): ")
local = input("Digite o local do evento: ")
orcamento = float(input("Digite o orçamento do evento: R$ "))
evento = {
    "titulo": titulo,
    "tipo": tipo,
    "data": data,
    "local": local,
    "orcamento": orcamento
}
eventos.append(evento)

print("\nEvento adicionado com sucesso!")
input("\nPressione Enter para continuar...")
adicionar_evento()