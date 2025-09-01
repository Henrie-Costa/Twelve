"""Desenvolva um programa que consulte informações de endereço a partir de um CEP fornecido pelo usuário, utilizando a API ViaCEP. O programa deve exibir o logradouro, bairro, cidade e estado correspondentes ao CEP consultado."""

import requests


cep = input("Digite o CEP (somente números): ")


url = f"https://viacep.com.br/ws/{cep}/json/"


resposta = requests.get(url)


if resposta.status_code == 200:
    dados = resposta.json()
    
    if "erro" not in dados:
        print("\n=== Endereço Encontrado ===")
        print("Logradouro:", dados["logradouro"])
        print("Bairro    :", dados["bairro"])
        print("Cidade    :", dados["localidade"])
        print("Estado    :", dados["uf"])
    else:
        print(" CEP não encontrado!")
else:
    print("Erro ao consultar a API:", resposta.status_code)
