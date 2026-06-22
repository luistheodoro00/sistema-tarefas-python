import func

lista=func.carregar_dados()

while True:

    func.menu()
    try:
        op=int(input("Escolha uma das opções:"))

    except ValueError:
        func.mensagem_de_erro()
        continue

    match op:

        case 1:
            try:

                escolha=int(input("1 para tarefa urgente e 2 para tarefa normal:"))

            except ValueError:
                print("Digite apenas dados compátiveis")
                continue


            if escolha == 1:

                if func.cadastrar_tarefa_urgente(lista):
                    func.salvar_dados(lista)
                    print("Tarefa cadastrada")
                else:
                    print("Erro ao cadastrar tarefa")

            elif escolha == 2:

                if func.cadastrar_tarefa(lista):
                    func.salvar_dados(lista)
                    print("Tarefa cadastrada")
                else:
                    print("Erro ao cadastrar tarefa")


        case 2:

            try:
                titulo_1=int(input("Digite o id da tarefa:"))

            except ValueError:
                func.mensagem_de_erro()
                continue

            encontrado=func.concluir_tarefa(lista,titulo_1)

            if encontrado:
                func.salvar_dados(lista)
                print("Tarefa atualizada")
            else:
                print("Falha ao atualizar tarefa")
                continue

        case 3:

            func.listar_todos(lista)

        case 4:

            try:

                busca=int(input("Digite o id da tarefa:"))

            except ValueError:
                func.mensagem_de_erro()

                continue

            encontrado_1=func.buscar_tarefa(lista,busca)

            if encontrado_1:

                encontrado_1.exibir()

            else:
                print(f"Nada encontrado")

        case 5:
            print("Encerrando sistema.")
            break






