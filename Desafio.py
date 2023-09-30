import requests

print("Digite o cep: ")
cep = input()
cep = cep.replace("-", "").replace(".", "").replace(" ", "")

if len(cep) == 8:
    link = f'https://viacep.com.br/ws/{cep}/json/'
    requisicao = requests.get(link)

    if requisicao.status_code == 200:
        dic_requisicao = requisicao.json()
        logradouro = dic_requisicao['logradouro']
        bairro = dic_requisicao['bairro']
        cidade = dic_requisicao['localidade']
        uf = dic_requisicao['uf']
        print(f"O Cep informado é da {logradouro}, que fica no bairro: {bairro} na Cidade de {cidade}/{uf}")
    else: 
        print("Erro na requisição, falha na conexão com a internet ou servidor")
else:
    print("CEP Inválido")