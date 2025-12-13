import pandas as pd
import os

ARQUIVO_CSV = "alunos.csv"

def carregar_dados():
    colunas = [
        "matricula", "nome", "rua", "numero", "bairro",
        "cidade", "uf", "telefone", "email"
    ]

    if os.path.exists(ARQUIVO_CSV):
        df = pd.read_csv(ARQUIVO_CSV)
        return df[colunas]
    else:
        df = pd.DataFrame(columns=colunas)
        df.to_csv(ARQUIVO_CSV, index=False)
        return df

def gerar_matricula(df):
    if df.empty:
        return 1
    else:
        return int(df["matricula"].max()) + 1

def inserir(df):
    novo = {}

    novo["matricula"] = gerar_matricula(df)
    print(f"\nMatrícula gerada: {novo['matricula']}")

    novo["nome"] = input("Nome: ")
    novo["rua"] = input("Rua: ")
    novo["numero"] = input("Número: ")
    novo["bairro"] = input("Bairro: ")
    novo["cidade"] = input("Cidade: ")
    novo["uf"] = input("UF: ")
    novo["telefone"] = input("Telefone: ")
    novo["email"] = input("E-mail: ")

    df = pd.concat([df, pd.DataFrame([novo])], ignore_index=True)
    df.to_csv(ARQUIVO_CSV, index=False)

    print("\nAluno cadastrado com sucesso!\n")
    return df

def exibir_aluno(resultado):
    print("\n             ALUNO           ")
    linha = resultado.iloc[0]
    print(f"Matrícula : {linha['matricula']}")
    print(f"Nome      : {linha['nome']}")
    print(f"Rua       : {linha['rua']}")
    print(f"Número    : {linha['numero']}")
    print(f"Bairro    : {linha['bairro']}")
    print(f"Cidade    : {linha['cidade']}")
    print(f"UF        : {linha['uf']}")
    print(f"Telefone  : {linha['telefone']}")
    print(f"E-mail    : {linha['email']}")
    print("                                ")

def pesquisar(df):
    print("\nPESQUISAR ALUNO")
    opcao = input("Pesquisar por (1) Matrícula ou (2) Nome? ")

    if opcao == "1":
        matricula = int(input("Digite a matrícula: "))
        resultado = df[df["matricula"] == matricula]

    elif opcao == "2":
        nome = input("Digite o nome: ").lower()
        resultado = df[df["nome"].str.lower() == nome]

    else:
        print("Opção inválida.")
        return df

    if resultado.empty:
        print("\nAluno não encontrado.\n")
        return df

    exibir_aluno(resultado)

    while True:
        acao = input("\nDeseja (E)ditar, (R)emover ou (V)oltar? ").upper()

        if acao == "E":
            matricula = int(resultado.iloc[0]["matricula"])
            df = editar(df, matricula)
            return df

        elif acao == "R":
            matricula = int(resultado.iloc[0]["matricula"])
            df = remover(df, matricula)
            return df

        elif acao == "V":
            return df

        else:
            print("Opção inválida.")

def editar(df, matricula):
    print("\n=== CAMPOS PARA EDITAR ===")
    print("1 - Nome")
    print("2 - Rua")
    print("3 - Número")
    print("4 - Bairro")
    print("5 - Cidade")
    print("6 - UF")
    print("7 - Telefone")
    print("8 - Email")

    campos = {
        "1": "nome",
        "2": "rua",
        "3": "numero",
        "4": "bairro",
        "5": "cidade",
        "6": "uf",
        "7": "telefone",
        "8": "email"
    }

    escolha = input("Escolha o campo: ")

    if escolha not in campos:
        print("Opção inválida.")
        return df

    novo_valor = input("Novo valor: ")

    df.loc[df["matricula"] == matricula, campos[escolha]] = novo_valor
    df.to_csv(ARQUIVO_CSV, index=False)

    print("\nDado atualizado!\n")
    return df

def remover(df, matricula):
    confirmar = input("Confirma remover o aluno? (S/N): ").upper()

    if confirmar == "S":
        df = df[df["matricula"] != matricula]
        df.to_csv(ARQUIVO_CSV, index=False)
        print("\nAluno removido!\n")
    else:
        print("\nRemoção cancelada.\n")

    return df

def menu():
    df = carregar_dados()

    while True:
        print("\n           MENU          ")
        print("1 - INSERIR")
        print("2 - PESQUISAR")
        print("3 - SAIR")
        opcao = input("Escolha: ")

        if opcao == "1":
            df = inserir(df)
        elif opcao == "2":
            df = pesquisar(df)
        elif opcao == "3":
            print("\nPrograma encerrado.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()