Data_Evento = "sistema de eventos.txt"


def criar_arquivos():
    with open(Data_Evento, "a", encoding = "utf-8"):
        pass

def ler_arquivo():
    with open (Data_Evento, "r", encoding = "utf-8") as arquivo:
        return arquivo.readlines()

def filtrar_eventos():
  assunto = ler_arquivo()



 if assunto.strip() == "":
    return []

