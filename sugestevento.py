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
