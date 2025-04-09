    # Documentação de funções (docstrings)
# É uma boa prática documentar nossas funções utilizando docstrings. Os docstrings são cadeias de texto que descrevem o propósito, os parâmetros e o valor de retorno de uma função. São colocados imediatamente após a definição da função e são encerrados entre aspas duplas triplas.

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