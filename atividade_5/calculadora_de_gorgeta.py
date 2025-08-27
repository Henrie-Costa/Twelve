"""Crie uma função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de gorjeta desejada. Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada. Parâmetros: valor_conta (float): O valor total da conta porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%) Retorna: float: O valor da gorjeta calculadaz"""


calcular_gorjeta = lambda valor_conta, porcentagem_gorjeta: valor_conta * (porcentagem_gorjeta / 100)


valor = float(input("Digite o valor da conta: "))
porcentagem = float(input("Digite a porcentagem da gorjeta: "))

gorjeta = calcular_gorjeta(valor, porcentagem)
print(f"Para a Conta de R$ {valor}, A gorjeta deve ser de R$ {gorjeta:.2f}")
