# Funções

# As funções são blocos de código reutilizáveis que nos permitem encapsular tarefas específicas e executá-las quando necessário. As funções nos ajudam a organizar nosso código, evitar a repetição e fazer com que nossos programas sejam mais modulares e fáceis de manter.
 
    # Definição e chamada de funções
# Para definir uma função em Python, utilizamos a palavra-chave def seguida do nome da função e parênteses. Opcionalmente, podemos especificar parâmetros dentro dos parênteses. O bloco de código da função é indentado após os dois pontos.

# Para chamar uma função, simplesmente escrevemos o nome da função seguido de parênteses:

def saudacao():
    print("Olá, mundo!")

saudacao()  # Imprime "Olá, mundo!"

 
    # Parâmetros e argumentos
# As funções podem aceitar parâmetros, que são valores que são passados para a função quando ela é chamada. Os parâmetros são especificados dentro dos parênteses na definição da função.

def saudacao(nome):
    print(f"Olá, {nome}!")

# Ao chamar a função, fornecemos os argumentos correspondentes aos parâmetros:
saudacao("João")  # Imprime "Olá, João!"
saudacao("Maria")  # Imprime "Olá, Maria!"