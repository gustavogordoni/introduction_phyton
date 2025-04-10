import pandas as pd

series_objeto = pd.Series([1,7,9,13,17,99])
print(series_objeto)

print("-" * 30)

series_objeto2= pd.Series([4, 7, 8, -2], index = ['alfa', 'beta', 'teta', 'gama'])
print(series_objeto2)

print("-" * 30)

disciplinas = {
    "cursos" : ["Estatistica", "Economia","Célculo", "Geometri"],
    "créditos" : [90, 60, 90, 40],
    "requisito" : [True, False, True, False]
}

data = pd.DataFrame(disciplinas)
print(data)

print("-" * 30)

nome_cidade = pd.Series(
    ['Maringá', 'Itabira', 'Uberlandia']
)

populacao = pd.Series([403.063, 120.904, 699.097])

print(
    pd.DataFrame({"Cidade": nome_cidade, "Populacao": populacao})
)

print("-" * 30)

cidades = ['Maringá', 'Itabira', 'Uberlandia', 'Salvador', 'Fortaleza']
populacao = [463.063, 120.904, 699.897, 2.886698, 2.686612]

populacao_cidades = dict(zip(cidades, populacao))

print (populacao_cidades)

print("-" * 30)

print(
    type(populacao_cidades)
)

print("-" * 30)

print(
    populacao_cidades['Uberlandia']
)

print("-" * 30)

print(
'Maringá' in populacao_cidades
)

print(
'São Carlos' in populacao_cidades
)

print("-" * 30)

populacao_cidades['Vitória'] = 365.855

print(
    populacao_cidades
)

print("-" * 30)

del populacao_cidades['Fortaleza']

print(
    populacao_cidades
)