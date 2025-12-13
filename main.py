from alunos import carregar_dados, inserir, pesquisar

def main():
    df = carregar_dados()

    while True:
        print("\n       MENU        ")
        print("1 - INSERIR")
        print("2 - PESQUISAR")
        print("3 - SAIR")

        opcao = input("Escolha: ")

        if opcao == "1":
            df = inserir(df)
        elif opcao == "2":
            df = pesquisar(df)
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
