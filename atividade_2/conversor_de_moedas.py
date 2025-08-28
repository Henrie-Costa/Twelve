# Atividade Prática 02 - Conversor de Moeda

# Dados
valor_reais = 100.00
taxa_dolar = 5.60
taxa_euro = 6.60

# Conversão
valor_dolar = valor_reais / taxa_dolar
valor_euro = valor_reais / taxa_euro

# Saída formatada
print(f"Valor em reais: R$ {valor_reais:.2f}")
print(f"Em dólares: US$ {valor_dolar:.2f}")
print(f"Em euros: € {valor_euro:.2f}")


# Atividade Prática 02 - Conversor de Moeda (versão interativa)

# Taxas fixas
taxa_dolar = 5.60
taxa_euro = 6.60

# Entrada do usuário
valor_reais = float(input("Digite o valor em reais (R$): "))

# Conversão
valor_dolar = valor_reais / taxa_dolar
valor_euro = valor_reais / taxa_euro

# Saída formatada
print(f"\nValor em reais: R$ {valor_reais:.2f}")
print(f"Em dólares: US$ {valor_dolar:.2f}")
print(f"Em euros: € {valor_euro:.2f}")
