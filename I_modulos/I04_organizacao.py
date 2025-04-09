    # Organização do código em módulos
# À medida que nossos programas crescem em tamanho e complexidade, é uma boa prática organizar nosso código em módulos separados segundo sua funcionalidade. Isso nos permite manter um código mais legível, agrupado em módulos e fácil de manter.

# Por exemplo, podemos ter um módulo operacoes.py que contenha funções relacionadas com operações matemáticas, e outro módulo utilidades.py que contenha funções de uso geral.

# # operacoes.py
# def somar(a, b):
#     return a + b


# def subtrair(a, b):
#     return a - b


# # utilidades.py
# def imprimir_mensagem(mensagem):
#     print(mensagem)


# def obter_nome_usuario():
#     return input("Digite seu nome: ")


# Depois, podemos importar e utilizar essas funções em nosso programa principal.

import operacoes
import utilidades

resultado = operacoes.somar(5, 3)
utilidades.imprimir_mensagem(f"O resultado da soma é: {resultado}")

nome = utilidades.obter_nome_usuario()
utilidades.imprimir_mensagem(f"Olá, {nome}!")

# Ao organizar nosso código em módulos, podemos reutilizar funções e manter um código mais estruturado e agrupado em módulos.