def exercicio1():
    print("Hello, world!")


def exercicio2():
    numero1 = 12
    numero2 = 14
    soma = numero1 + numero2
    print("A soma é:", soma)


def exercicio3():
    comprimento = 12  # cm
    largura = 14      # cm
    altura = 20       # cm
    volume = comprimento * largura * altura
    print("O volume da caixa é:", volume, "cm³")


def exercicio4():
    nome_produto = "Cadeira Infantil"
    preco_unitario = 12.40
    quantidade = 3
    preco_total = preco_unitario * quantidade

    print("Produto:", nome_produto)
    print("Preço unitário: R$", preco_unitario)
    print("Quantidade:", quantidade)
    print("Preço total: R$", preco_total)


def exercicio5():
    A = int(input("Digite o valor de A: "))
    B = int(input("Digite o valor de B: "))
    C = int(input("Digite o valor de C: "))
    D = int(input("Digite o valor de D: "))

    diferenca = (A * B) - (C * D)
    print("DIFERENCA =", diferenca)


# ------------------- MENU -------------------
while True:
    print("\n===== Atividade Prática 01 =====")
    print("1 - Hello World")
    print("2 - Calculadora de Soma")
    print("3 - Calculadora de Volume")
    print("4 - Calculadora de Preço Total")
    print("5 - Calculadora de Número Inteiro")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        exercicio1()
    elif opcao == "2":
        exercicio2()
    elif opcao == "3":
        exercicio3()
    elif opcao == "4":
        exercicio4()
    elif opcao == "5":
        exercicio5()
    elif opcao == "0":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida, tente novamente!")
