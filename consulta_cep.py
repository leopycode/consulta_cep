import requests
import data_hoje

print("\n\033[1m{:=^75} \033[m \n".format(" Consulte um CEP "))

cep = str(input("Digite o CEP a ser consultado [apenas numeros]: "))

consulta_cep = requests.get(f"https://cep.awesomeapi.com.br/json/{cep}")
consulta_cep = consulta_cep.json()

cep_consultado = consulta_cep["cep"]
cep_formatado = f"{cep_consultado[0:2]}.{cep_consultado[2:5]}-{cep_consultado[5:8]}"
endereco = consulta_cep["address"]
bairro = consulta_cep["district"]
cidade = consulta_cep["city"]
estado = consulta_cep["state"]

print("\n\n\033[1m{:=^75} \033[m \n".format(" Dados do CEP contultado "))
print(f"CEP consultado: {cep_formatado}")
print(f"Logradouro: {endereco}")
print(f"Bairro: {bairro}")
print(f"Cidade: {cidade}")
print(f"Estado: {estado}")
print(f"\nConsulta de CEP efetuada em {data_hoje.hoje()}.")
print("\n\033[1m{:=^75} \033[m \n".format(" Consulta finalizada "))
