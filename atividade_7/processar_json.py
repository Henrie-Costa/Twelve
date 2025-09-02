"""Crie um script em Python que leia e escreva dados em um arquivo JSON. O arquivo JSON deve conter informações de uma pessoa, com campos nome, idade e cidade."""


import json

# Informações para salvar no arquivo

dados_pessoas = [
    {
        'nome': 'Henrique',
        'idade': 30,
        'cidade': 'São Paulo'
    },
    {
        'nome': 'Maria',
        'idade': 25,
        'cidade': 'Rio de Janeiro'
    },
    {
        'nome': 'João',
        'idade': 45,
        'cidade': 'Belo Horizonte'
    },
    {
        'nome': 'Ana',
        'idade': 28,
        'cidade': 'Curitiba'
    },
    {
        'nome': 'Bruno',
        'idade': 35,
        'cidade': 'Maceió'
    },
    {   'nome': 'Oculos do Bruno',
        'idade': 1,
        'cidade': 'Banheiro'}
]

nome_do_arquivo = 'dados_pessoas.json'

# ---  ESCREVE OS DADOS NO ARQUIVO ---
try:
    print(f"Escrevendo dados no arquivo '{nome_do_arquivo}'...")
    
    with open(nome_do_arquivo, 'w', encoding='utf-8') as arquivo_json:
        # Garante que os caracteres não-ASCII sejam salvos corretamente
        json.dump(dados_pessoas, arquivo_json, indent=4, ensure_ascii=False)
        
    print("Dados salvos com sucesso!")

except Exception as e:
    print(f"Erro ao salvar o arquivo: {e}")

# ---  LÊ OS DADOS DO ARQUIVO ---
try:
    print(f"\nLendo dados do arquivo '{nome_do_arquivo}'...")
    
    with open(nome_do_arquivo, 'r', encoding='utf-8') as arquivo_json:
        dados_lidos = json.load(arquivo_json)
    
    print("Dados lidos com sucesso:")
    # Loop para exibir cada pessoa da lista
    for pessoa in dados_lidos:
        print(f"Nome: {pessoa['nome']}, Idade: {pessoa['idade']}, Cidade: {pessoa['cidade']}")

except FileNotFoundError:
    print(f"Erro: O arquivo '{nome_do_arquivo}' não foi encontrado.")
except Exception as e:
    print(f"Erro ao ler o arquivo: {e}")