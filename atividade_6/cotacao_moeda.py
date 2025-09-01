"""Crie um programa que consulte a cotação atual de uma moeda estrangeira em relação ao Real Brasileiro (BRL). O usuário deve informar o código da moeda desejada (ex: USD, EUR, GBP), e o programa deve exibir o valor atual, máximo e mínimo da cotação, além da data e hora da última atualização. Utilize a API da AwesomeAPI para obter os dados de cotação."""

import requests


moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").upper().strip()


url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"


resposta = requests.get(url)

if resposta.status_code == 200:
    dados = resposta.json()
    
   
    chave = f"{moeda}BRL"
    
    if chave in dados:
        cotacao = dados[chave]
        print("\n=== Cotação Atual ===")
        print(f"Moeda: {moeda} -> BRL")
        print(f"Valor atual: R$ {cotacao['bid']}")
        print(f"Máximo: R$ {cotacao['high']}")
        print(f"Mínimo: R$ {cotacao['low']}")
        print(f"Última atualização: {cotacao['create_date']}")
    else:
        print(" Moeda não encontrada.")
else:
    print("Erro ao consultar a API:", resposta.status_code)
