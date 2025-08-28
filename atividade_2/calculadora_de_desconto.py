# Atividade Prática 02 - Calculadora de Desconto

# Dados
nome_produto = "Camiseta"
preco_original = 50.00
desconto_percentual = 20

# Cálculos
valor_desconto = preco_original * (desconto_percentual / 100)
preco_final = preco_original - valor_desconto

# Saída formatada
print(f"Produto: {nome_produto}")
print(f"Preço original: R$ {preco_original:.2f}")
print(f"Desconto: {desconto_percentual}% (R$ {valor_desconto:.2f})")
print(f"Preço final: R$ {preco_final:.2f}")


# Atividade Prática 02 - Calculadora de Desconto (versão interativa)

# Entrada do usuário
nome_produto = input("Digite o nome do produto: ")
preco_original = float(input("Digite o preço original do produto (R$): "))
desconto_percentual = float(input("Digite a porcentagem de desconto (%): "))

# Cálculos
valor_desconto = preco_original * (desconto_percentual / 100)
preco_final = preco_original - valor_desconto

# Saída formatada
print("\n--- Detalhes da Compra ---")
print(f"Produto: {nome_produto}")
print(f"Preço original: R$ {preco_original:.2f}")
print(f"Desconto: {desconto_percentual}% (R$ {valor_desconto:.2f})")
print(f"Preço final: R$ {preco_final:.2f}")

