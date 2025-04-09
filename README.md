# Anotações: Curso de Python - Santander

## **1. Conceitos básicos da sintaxe em Python**

### Indentação

```
if condition:
    # Bloco de código se a condição for verdadeira
    instrucao1
    instrucao2
else:
    # Bloco de código se a condição for falsa
    instrucao3
    instrucao4
```

### Comentários

```
# Este é um comentário de uma única linha

"""
Este é um comentário
de várias linhas
"""
```

## **2. Tipos de dados básicos**

### Inteiros (int)

```
idade = 25
quantidade = 100
```

### Flutuantes (float)

```
preço = 9.99
altura = 1.75
```

### Cadeias de texto (strings)

```
nome = "Juan"
mensagem = '¡Hola, mundo!'
```

### Booleanos

```
maior_de_idade = True
tem_desconto = False
```

## 2.1. Variáveis

Exemplos:

```
nome = "Juan"
idade = 25
altura = 1.75
estudante = True
```

#### Nomes válidos:

```
idade
nome_completo
total_vendas
_contador
```

#### Nomes inválidos:

```
1idade   # Começa com um número
nome-completo   # Usa um hífen em vez de um sublinhado
if   # Palavra-chave reservada do Python
```

## 2.2. Operadores

### **Aritméticos**

* Soma (+): soma dois valores.
* Subtração (-): subtrai o segundo valor do primeiro.
* Multiplicação (*): multiplica dois valores.
* Divisão (/): divide o primeiro valor pelo segundo e devolve um resultado de tipo flutuante.
* Divisão inteira (//): divide o
  primeiro valor pelo segundo e devolve um resultado de tipo inteiro (a
  parte decimal é descartada).
* Módulo (%): devolve o resto da divisão entre o primeiro valor e o segundo.
* Exponenciação (**): eleva o primeiro valor à potência do segundo.

Exemplo:

```
a = 10
b = 3

soma = a + b   # 13
subtracao = a - b    # 7
multiplicacao = a * b    # 30
divisao = a / b   # 3.333333333
divisao_inteira = a // b   # 3
modulo = a % b   # 1
exponenciacao = a ** b   # 1000
```

### **De comparação**

* Igual a (==): devolve True se ambos os valores são iguais.
* Diferente de (!=): devolve True se os valores são diferentes.
* Maior que (>): devolve True se o primeiro valor é maior que o segundo.
* Menor que (<): devolve True se o primeiro valor é menor que o segundo.
* Maior ou igual que (>=): devolve True se o primeiro valor é maior ou igual que o segundo.
* Menor ou igual que (<=): devolve True se o primeiro valor é menor ou igual que o segundo.

Exemplo:

```
a = 10
b = 3

igual = a == b   # False
diferente = a != b   # True
maior que = a > b   # True
menor que = a < b   # False
maior ou igual = a >= b   # True
menor ou igual = a <= b   # False
```

### **Lógicos**

* AND (and): devolve True se ambas as condições são verdadeiras.
* OR (or): devolve True se ao menos uma das condições é verdadeira.
* NOT (not): inverte o valor de uma condição, devolve True se a condição é falsa e False se a condição é verdadeira.

Exemplo:

```
a = 10
b = 3

resultado_and = (a > 5) and (b < 5)   # True
resultado_or = (a > 15) or (b < 5)   # True
resultado_not = not (a > 5)   # False
```

## **3. Estruturas condicionais**

### IF

A estrutura if é utilizada para executar um bloco de código se uma condição for verdadeira.

Sintaxe:

```
if condicao:

   # Bloco de código a executar se a condição for verdadeira
   instruções
```

Exemplo:

```
idade = 18

if idade >= 18:
   print ("Você é maior de idade.")
```

### IF-ELSE

A estrutura if-else permite especificar um bloco de código alternativo que será  executado se a condição do if for falsa.

Exemplo:

```
idade = 15

if idade >= 18:
   print ("Você é maior de idade.")

else:
   print ("Você é menor de idade.")
```

### IF-ELIF-ELSE

A estrutura if-elif-else permite especificar múltiplas condições e blocos de código alternativos.

Sintaxe:

```
if condicao1:

   # Bloco de código a executar se a condicao1 for verdadeira
   instruções

elif condicao2:

   # Bloco de código a executar se a condicao2 for verdadeira
   instruções

else:

   # Bloco de código a executar se nenhuma condição anterior for verdadeira
   instruções
```

Exemplo:

```
nota = 85

if nota >= 90:
   print ("Excelente")

elif nota >= 80:
   print ("Muito bom")

elif nota >= 70:
   print ("Bom")

else:
   print ("Precisa melhorar")
```

## 3.1 Loops

### **For**

O loop for é utilizado para iterar sobre uma sequência (como uma lista, uma tupla ou uma string) ou qualquer objeto iterável.

Sintaxe:

```
for variável in sequência:

    # Bloco de código a repetir
    instruções
```

Exemplo:

```
frutas = ["maçã", "banana", "laranja"]

for fruta in frutas:
    print(fruta)
```

### **While**

O loop while é utilizado para repetir um bloco de código enquanto uma condição for verdadeira.

Sintaxe:

```
while condição:

    # Bloco de código a repetir
    instruções
```

Exemplo:

```
contador = 0

while contador < 5:

    print(contador)
    contador += 1
```

### **Controle de loops**

#### Break

Utilizada para sair  prematuramente de um loop, independentemente da condição. O loop é interrompido e o fluxo de execução continua com a próxima instrução fora do loop.

```
contador = 0

while True:

    print(contador)
    contador += 1

    if contador == 5:
        break
```

#### Continue

Utilizada para pular o restante do bloco de código dentro de um loop e passar para a próxima iteração.

Exemplo:

```
for i in range(10):

    if i % 2 == 0:
        continue
    print(i)
```

#### Pass

Operação nula que não faz nada. É utilizada como um marcador de posição quando uma instrução é sintaticamente necessária, mas nenhuma ação é desejada.

Exemplo:

```
for i in range(5):
    pass
```

## 4. Estruturas de dados

### **Listas**

#### Criação e acesso

Para criar uma lista, simplesmente encerre os elementos entre colchetes:

```
frutas = ["maçã", "banana", "laranja"]
```

Para acessar os elementos de uma lista, utilize-se o índice do elemento entre colchetes. Os índices começam a partir de 0.

```
print(frutas[0])  # Imprime "maçã"
print(frutas[1])  # Imprime "banana"
print(frutas[2])  # Imprime "laranja"
```

Pode acessar os elementos a partir do final da lista utilizando índices negativos. O índice -1 representa o último elemento, -2 representa o penúltimo, e assim por
diante.

```
print(frutas[-1])  # Imprime "laranja"
print(frutas[-2])  # Imprime "banana"
print(frutas[-3])  # Imprime "maçã"
```

#### Métodos de listas

* append(elemento): adiciona um elemento ao final da lista.
* insert(indice, elemento): insere um elemento em uma posição específica da lista.
* remove(elemento): remove a primeira ocorrência de um elemento na lista.
* pop(indice): remove e retorna o elemento em uma posição específica da lista.
* sort(): ordena os elementos da lista em ordem ascendente.
* reverse(): inverte a ordem dos elementos na lista.

Exemplo:

```
frutas = ["maçã", "banana", "laranja"]

frutas.append("pera")
print(frutas)  # Imprime ["maçã", "banana", "laranja", "pera"]

frutas.insert(1, "uva")
print(frutas)  # Imprime ["maçã", "uva", "banana", "laranja", "pera"]

frutas.remove("banana")
print(frutas)  # Imprime ["maçã", "uva", "laranja", "pera"]

fruta_removida = frutas.pop(2)
print(frutas)  # Imprime ["maçã", "uva", "pera"]
print(fruta_removida)  # Imprime "laranja"

frutas.sort()
print(frutas)  # Imprime ["maçã", "pera", "uva"]

frutas.reverse()
print(frutas)  # Imprime ["uva", "pera", "maçã"]
```

#### Listas de compreensão

As listas de compreensão são uma forma de criar novas listas baseadas em uma sequência existente. Permitem filtrar e transformar os elementos de uma lista em uma única linha de código.

```
nova_lista = [expressão for elemento in sequência if condição]
```

Exemplo:

```
números = [1, 2, 3, 4, 5]
quadrados = [x ** 2 for x in números if x % 2 == 0]
print(quadrados)  # Imprime [4, 16]
```

## 4.1. Tuplas

Estrutura de dados imutável e ordenada que permite armazenar uma coleção de elementos.

### Criação e acesso

Para criar uma tupla, encerre os elementos entre parênteses:

```
ponto = (3, 4)
```

Para acessar os elementos de uma tupla, utilize o índice do elemento entre colchetes, similar às listas:

```
print(ponto[0])  # Imprime 3

print(ponto[1])  # Imprime 4
```

### Diferença entre Tulpa e Lista:

Ao contrário das listas, as tuplas são imutáveis, o que significa que não podem ser modificadas uma vez criadas. Não se pode adicionar, eliminar ou alterar elementos em uma tupla existente.

### Métodos de tuplas

Embora sejam imutáveis, existem vários métodos úteis para trabalhar com elas:

* **count(elemento):** devolve o número de vezes que um elemento aparece na tupla.
* **index(elemento):** devolve **o índice da primeira aparição de um elemento na tupla. Opcionalmente, pode-se especificar o início e fim da busca.**
* **len(tupla):** **embora não seja um método de tupla propriamente dito, esta função incorporada devolve o comprimento da tupla.**

```
minha_tupla = (1, 2, 3, 2, 4, 2)

print (minha_tupla.index(2))   # Saída: 1
print (minha_tupla.index(2, 2))   #Saída: 3
print (minha_tupla.index(2, 2, 4))   #Saída: 3
```

## 4.2. Dicionários

Estrutura de dados mutável e não ordenada que permite armazenar pares de chave-valor. Cada elemento em um dicionário consiste em uma chave única e seu valor correspondente.

### Criação e acesso

Utilizar chaves e separar as chaves e valores com dois pontos.

```
pessoa = {"nome": "João", "idade": 25, "cidade": "Madri"}
```

Para acessar seus valores, utiliza-se a chave correspondente entre colchetes:

```
print(pessoa["nome"])  # Imprime "João"
print(pessoa["idade"])    # Imprime 25
print(pessoa["cidade"])  # Imprime "Madri"
```

Pode-se utilizar o método get() para obter o valor de uma chave. Se a chave não existir, retorna None.

### Métodos de dicionários

Possuem vários métodos para manipular e acessar os elementos. Alguns métodos comuns são:

* **keys():** retorna uma visualização de todas as chaves do dicionário.
* **values():** retorna uma visualização de todos os valores do dicionário.
* **items():** retorna uma visualização de todos os pares chave-valor do dicionário.
* **update(**outro_dicionario**):** atualiza o dicionário com os pares chave-valor de outro dicionário.

Exemplo:

```
pessoa = {"nome": "João", "idade": 25, "cidade": "Madri"}

print(pessoa.keys())    # Imprime dict_keys(["nome", "idade", "cidade"])
print(pessoa.values())  # Imprime dict_values(["João", 25, "Madri"])
print(pessoa.items())   # Imprime dict_items([("nome", "João"), ("idade", 25), ("cidade", "Madri")])

pessoa.update({"profissao": "Engenheiro"})
print(pessoa)  # Imprime {"nome": "João", "idade": 25, "cidade": "Madri", "profissao": "Engenheiro"}
```

## 4.3. Conjuntos (set)

Trata-se de uma estrutura de dados mutável e não ordenada que permite armazenar uma coleção de elementos únicos. São delimitados por chaves {} ou são criados utilizando a função set().

### Criação e operações básicas

Utilize chaves ou a função set():

```
frutas = {"maçã", "banana", "laranja"}
numeros = set([1, 2, 3, 4, 5])
```

Suportam operações matemáticas de conjuntos, como a **união (|)**, a **interseção (&)**, a **diferença (-)** e a **diferença simétrica (^)**.

```
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

uniao = conjunto1 | conjunto2
print(uniao)  # Imprime {1, 2, 3, 4, 5}

intersecao = conjunto1 & conjunto2
print(intersecao)  # Imprime {3}

diferenca = conjunto1 - conjunto2
print(diferenca)  # Imprime {1, 2}

diferenca_simetrica = conjunto1 ^ conjunto2
print(diferenca_simetrica)  # Imprime {1, 2, 4, 5}
```

### Métodos de conjuntos

Possuem métodos incorporados para manipular e acessar os elementos. Alguns métodos comuns são:

* **add(elemento):** adiciona um elemento ao conjunto.
* **remove(elemento):** remove um elemento do conjunto. Se o elemento não existir, gera um erro.
* **discard(elemento):** remove um elemento do conjunto se estiver presente. Se o elemento não existir, não faz nada.
* **clear():** remove todos os elementos do conjunto.

Exemplo:

```
frutas = {"maçã", "banana", "laranja"}

frutas.add("pera")
print(frutas)  # Imprime {"maçã", "banana", "laranja", "pera"}

frutas.remove("banana")
print(frutas)  # Imprime {"maçã", "laranja", "pera"}

frutas.discard("uva")
print(frutas)  # Imprime {"maçã", "laranja", "pera"}

frutas.clear()
print(frutas)  # Imprime set()
```

## 5.  Funções

São blocos de código reutilizáveis que permitem encapsular tarefas específicas e executá-las quando necessário. Ajudame em: organizar o código; evitar repetição; programas sejam mais modulares; facilitam manutenção.

### **Definição e chamada de funções**

Utiliza-se a palavra-chave def seguida do nome da função e parênteses. Opcionalmente, pode conter parâmetros.

Para chamar uma função, deve ser escrito o nome da função seguido de parênteses:

```
def saudacao():
    print("Olá, mundo!")

saudacao()  # Imprime "Olá, mundo!"
```

### **Parâmetros e argumentos**

São passados para a função quando ela é chamada, e são especificados dentro dos parênteses na definição da função.

```
def saudacao(nome):
    print(f"Olá, {nome}!")
```

Ao chamar a função, fornecemos os argumentos correspondentes aos parâmetros:

```
saudacao("João")  # Imprime "Olá, João!"
saudacao("Maria")  # Imprime "Olá, Maria!"
```

### **Valores de retorno**

Podem retornar valores usando a palavra-chave ***return***.

```
def soma(a, b):
    return a + b

resultado = soma(3, 4)
print(resultado)  # Imprime 7
```

### **Funções anônimas (lambda)**

Funções sem nome definidas em uma única linha. São comumente usadas para funções pequenas e concisas.

```
quadrado = lambda x: x ** 2
print(quadrado(5))  # Imprime 25
```

### **Escopo das variáveis (local vs. global)**

* **Locais:** Variáveis definidas dentro de uma função têm um escopo local, isto é, são acessíveis apenas dentro da função.
* **Globais**: Variáveis definidas fora de qualquer função têm um escopo global, isto é, podem ser acessadas de qualquer parte do programa.

```
def funcao():
    variavel_local = 10
    print(variavel_local)  # Acessível dentro da função

variavel_global = 20

def funcao2():
    print(variavel_global)  # Acessível de qualquer lugar

funcao()  # Imprime 10
funcao2()  # Imprime 20
print(variavel_global)  # Imprime 20
print(variavel_local)  # Gera um erro, a variável não está definida neste escopo.

```

### Documentação de funções (docstrings)

Cadeias de texto que descrevem o propósito, os parâmetros e o valor de retorno de uma função. São colocados após a definição da função e são encerrados entre aspas duplas triplas.

```
def area_retangulo(base, altura):
    """
    Calcula a área de um retângulo.


    Args:
        base (float): A base do retângulo.
        altura (float): A altura do retângulo.


    Returns:
        float: A área do retângulo.
    """
    return base * altura

```

### Funções com número variável de argumentos

Permite definir funções que aceitem um número variável de argumentos. Utiliza-se  o operador * antes do nome do parâmetro.

```
def soma_variavel(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total


print(soma_variavel(1, 2, 3))  # Imprime 6
print(soma_variavel(4, 5, 6, 7))  # Imprime 22
```

## 6. Tratamento de erros e exceções

### **Erro de sintaxe (SyntaxError)**

Ocorre quando o código não segue as regras de sintaxe do Python.

| Ex: esquecer  dois pontos após uma declaração de função ou um loop.

```
def minha_funcao() # Faltam os dois pontos
    print("Olá")
```

### Erro de nome (NameError)

Ocorre quando se faz referência a uma variável ou função que não foi definida.

```
print(variavel_nao_definida)
```

### **Erro de tipo (TypeError)**

Ocorre quando se realiza uma operação com tipos de dados incompatíveis,

Ex: tentar somar um número e uma string.

```
resultado = 5 + "10"
```

### **Erro de índice (IndexError)**

Ocorre quando se tenta acessar um índice fora do intervalo válido de uma lista ou sequência.

```
lista = [1, 2, 3]
print(lista[3])  # O índice 3 está fora do intervalo
```

### 6.1. Manejo de exceções

#### **Try**

Contém o código que pode gerar uma exceção. Se ocorrer uma exceção dentro do bloco try, o fluxo de execução é transferido para o bloco except correspondente.

```
try:
    # Código que pode gerar uma exceção
    resultado = 10 / 0  # Divisão por zero
    print(resultado)
except ZeroDivisionError:
    print("Erro: Divisão por zero")
```

#### **Except**

Especifica o tipo de exceção que se deseja capturar e lidar. Pode haver múltiplos blocos
except para lidar com diferentes tipos de exceções.

```
try:
    # Código que pode gerar uma exceção
    resultado = 10 / 0  # Divisão por zero
    print(resultado)
except ZeroDivisionError:
    print("Erro: Divisão por zero")
except ValueError:
    print("Erro: Valor inválido")
```

#### **Finally**

É opcional e é executado sempre, independentemente de ter ocorrido uma exceção ou não.

```
try:
    # Código que pode gerar uma exceção
    arquivo = open("arquivo.txt", "r")
    # Realizar operações com o arquivo
except FileNotFoundError:
    print("Erro: Arquivo não encontrado")
finally:
    arquivo.close()  # Fechar o arquivo sempre, mesmo se ocorrer uma exceção
```

### 6.2. Exceções personalizadas

Para criar uma exceção personalizada, deve-se criar uma classe que herde da classe base Exception ou de uma de suas subclasses.

```
def funcao():
    # Código que pode gerar uma exceção personalizada
    if condicao:
        raise Exception("Descrição do erro")


try:
    funcao()
except Exception as e:
    print(f"Erro: {str(e)}")
```

## 7. Entradas/saídas

Permitm interagir com o usuário e manipular arquivos. Possibilita solicitar informações, mostrar resultados e ler/escrever dados em arquivos externos.

## **Entrada de dados do usuário**

**input():** Esta função mostra uma mensagem na tela e espera que o usuário insira um valor.

```
nome = input("Insira seu nome: ")
idade = input("Insira sua idade: ")

print("Olá, " + nome + "!")
print("Você tem " + idade + " anos.")
```

Outro exemplo:

```
idade = int(input("Insira sua idade: "))

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
```

## **Saída de dados**

**print():** recebe um ou mais argumentos e os mostra no console.

**f-string (formatação de cadeias):** utilizado para inserir variáveis diretamente dentro de uma cadeia de texto.

```
nome = "Juan"
idade = 25

print(f"Olá, meu nome é {nome} e tenho {idade} anos.")
```

### 7.1. Leitura e escrita de arquivos

É possível abrir arquivos em diferentes modos, como leitura ("r"), escrita ("w") ou anexar ("a"), e realizar operações de leitura e escrita.

#### **Leitura de arquivos**

Deve ser utilizado a função **open()** em modo de **leitura ("r")**. Para ler o conteúdo do arquivo, utiliza-se métodos como **read()** ou **readlines()**.

```
arquivo = open("dados.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()
```

#### **Escrita de arquivos**

Deve ser aberto em modo de **escrita ("w")** utilizando a função **open()**. Se o arquivo não existir, será criado automaticamente. Se o arquivo já existir, seu conteúdo será sobrescrito.

```
arquivo = open("dados.txt", "w")
arquivo.write("Olá, mundo!")
arquivo.close()
```

A declaração **with** é utilizada para manejar a **abertura** e **fechamento** de arquivos de maneira automática.

```
with open("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
```

## 8. Importação e criação de módulos

**Módulo:** arquivo que contém definições de funções, classes e variáveis que podem ser utilizadas em outros programas.

A importação de módulos permite acessar a funcionalidade definida em outros arquivos e reutilizar código de maneira eficiente.

### **Importar módulos**

Utiliza-se a declaração **import**. É possível importar um módulo completo ou funções específicas de um módulo.

Importação de módulo completo:

```
import math

resultado = math.sqrt(25)
print(resultado)  # Imprime 5.0
```

Para a importação de uma função específica, utiliza-se a sintaxe **from:**

```
from math import sqrt

resultado = sqrt(25)
print(resultado)  # Imprime 5.0
```

### **Funções e classes de módulos padrão**

Exemplos de módulos com funções e classes:

```
import random
import datetime

numero_aleatorio = random.randint(1, 10)
print(numero_aleatório)  # Imprime um número inteiro aleatório entre 1 e 10

data_atual = datetime.datetime.now()
print(data_atual)  # Imprime a data e hora atual
```

### 8.1. Criação de módulos próprios

Para criar um módulo personalizado, deve ser criado um novo arquivo Python e com a definição das funções, classes e variáveis desejadas.

```
#meu_modulo.py
def saudar(nome):
    print(f"Olá, {nome}!")


def calcular_soma(a, b):
    return a + b
```

Para acessar as funções definidas, basta utilizar o **import** em outro arquivo.

```
import meu_modulo

meu_modulo.saudar("João")  # Imprime "Olá, João!"
resultado = meu_modulo.calcular_soma(5, 3)
print(resultado)  # Imprime 8
```

### 8.2. Pacotes

Maneira de organizar módulos relacionados em uma estrutura hierárquica de diretórios. Permitem agrupar módulos relacionados e evitar conflitos de nomes entre módulos.

### **Criar e utilizar pacotes**

Para criar um pacote, é necessário criar um diretório e adicionar um arquivo especial chamado __init.py__ dentro dele. Este arquivo pode estar vazio ou conter código de inicialização do pacote.

Exemplo: diretório meu_pacote:

```
meu_pacote/
    __init__.py
    modulo1.py
    modulo2.py
```

Para importar e utilizar os módulos do pacote:

```
from meu_pacote import modulo1, modulo2

modulo1.funcao1()
modulo2.funcao2()
```
