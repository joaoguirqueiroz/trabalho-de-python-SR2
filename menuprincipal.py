def menu_principal():
    criar_arquivo()

    while True:
        limpar_tela()

        print("#" * 50)
        print("ORGANIZA FESTA".center(50))
        print("#" * 50)

        print("[1] - Adicionar evento")
        print("[2] - Visualizar eventos")
        print("[3]- Editar evento")
        print("[4] - Excluir evento")
        print("[5] - Relatório financeiro")
        print("[6] - Adicionar compra")
        print("[7] - Sugestão de evento")
        print("[0] - Sair")

        print("#" * 50)

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
