def criar_arquivo():
    with open(ARQUIVO_EVENTOS, "a", encoding="utf-8"):
        pass

def ler_arquivo():
    with open(ARQUIVO_EVENTOS, "r", encoding="utf-8") as arquivo:
        return arquivo.read()

def salvar_arquivo(assunto):
    with open(ARQUIVO_EVENTOS, "w", encoding="utf-8") as arquivo:
        arquivo.write(conteudo)

def separar_eventos():
    assunto= ler_arquivo()
    if assunto.strip() == "":
        return []
    return assunto.split("\n\n")
