import json

# Suponha que temos um arquivo faturamento.json contendo os valores
with open('data/faturamento.json', 'r') as file:
    faturamento = json.load(file)

# Removendo dias sem faturamento (valores zero ou negativos)
faturamento = [dia for dia in faturamento if dia > 0]

# Calculando o menor e o maior faturamento
menor_faturamento = min(faturamento)
maior_faturamento = max(faturamento)

# Calculando a média mensal
media_mensal = sum(faturamento) / len(faturamento)

# Contando os dias com faturamento acima da média
dias_acima_da_media = len([dia for dia in faturamento if dia > media_mensal])

print(f"Menor faturamento: {menor_faturamento}")
print(f"Maior faturamento: {maior_faturamento}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
