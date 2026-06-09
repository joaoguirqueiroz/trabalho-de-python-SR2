def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def pausar():
    input("\nPressione ENTER para continuar...")

def mostrar_titulo(titulo):
    print("=" * 50)
    print(titulo.center(50))
    print("=" * 50)

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
