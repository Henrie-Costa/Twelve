"""

Calculadora de salário por horas trabalhadas

Leia o número de um funcionário, seu número de horas trabalhadas 
e o valor que recebe por hora. Calcule o salário do funcionário e exiba
 o resultado formatado corretamente.

Entrada:

O programa recebe 2 números inteiros e 1 número com duas casas decimais, 
representando:


Número do funcionário (numero_funcionario).

Quantidade de horas trabalhadas (horas_trabalhadas).

Valor recebido por hora (valor_por_hora).

Saída:




Imprima o número do funcionário e o salário calculado
 com duas casas decimais. Deve haver um espaço em branco antes 
 e depois do sinal de igualdade, e no caso do salário, também um espaço
   em branco após o R$





"""
# Atividade 06 - Calculadora de salário por horas trabalhadas

# Entrada
numero_funcionario = int(input("Digite o número do funcionário: "))
horas_trabalhadas = int(input("Digite a quantidade de horas trabalhadas: "))
valor_por_hora = float(input("Digite o valor recebido por hora (R$): "))

# Processamento
salario = horas_trabalhadas * valor_por_hora

# Saída
print(f"Numero = {numero_funcionario}")
print(f"Salario = R$ {salario:.2f}")


# Atividade 06 - Calculadora de salário por horas trabalhadas (versão interativa)

print("=== Calculadora de Salário ===")

# Entrada do usuário
numero_funcionario = int(input("Informe o número do funcionário: "))
horas_trabalhadas = int(input("Informe a quantidade de horas trabalhadas: "))
valor_por_hora = float(input("Informe o valor recebido por hora (R$): "))

# Cálculo do salário
salario = horas_trabalhadas * valor_por_hora

# Saída formatada
print("\n--- Resultado ---")
print(f"Número = {numero_funcionario}")
print(f"Salário = R$ {salario:.2f}")
