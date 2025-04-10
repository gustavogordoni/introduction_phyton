import pandas as pd

Autor = ['Sun Tau', 'Fernando Pessoa', 'Thonas Mann', 'Jodo Guimardes Rosa']

Livro = ['A Arte da Guerra', 'Poesias Selecionadas', 'A Montanha Migica', 'Prieiras Estérias']

Ano = [2000, 2004, 2015, 2017]

dados = {'Autor': Autor, 'Livro': Livro, 'Ano': Ano}

autores = pd.DataFrame(dados)
type(autores)

df = pd.DataFrame(autores)
print(df)

df.to_csv('autores.csv')

print(
    autores.info()
)

print(
    autores.columns
)

print(
    autores.index
)
