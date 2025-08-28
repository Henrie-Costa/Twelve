def idade_em_dias(ano, mes=1, dia=1):
    # Ano atual
    ano_atual = 2025
    mes_atual = 8
    dia_atual = 28

    # idade em anos, meses e dias
    anos = ano_atual - ano
    meses = mes_atual - mes
    dias = dia_atual - dia

    if dias < 0:
        dias += 30  
        meses -= 1

    if meses < 0:
        meses += 12
        anos -= 1

    # Calcula dias totais aproximados
    idade_dias = anos * 365 + meses * 30 + dias

    # Adiciona anos bissextos aproximando 1 dia extra a cada 4 anos
    anos_bissextos = (ano_atual - ano) // 4
    idade_dias += anos_bissextos

    return idade_dias

# Exemplo de uso
ano = int(input("Ano de nascimento: "))
mes = int(input("Mês de nascimento: "))
dia = int(input("Dia de nascimento: "))

print(f"Você tem aproximadamente {idade_em_dias(ano, mes, dia)} dias de vida.")
