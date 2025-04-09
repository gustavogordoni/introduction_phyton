# IF-ELIF-ELSE

# A estrutura if-elif-else nos permite especificar múltiplas condições e blocos de código alternativos. A sintaxe básica é a seguinte:

if condicao1:
   # Bloco de código a executar se a condicao1 for verdadeira
   instruções

elif condicao2:
   # Bloco de código a executar se a condicao2 for verdadeira
   instruções
   
else:
   # Bloco de código a executar se nenhuma condição anterior for verdadeira
   instruções


# Exemplo:
nota = 85

if nota >= 90:
   print ("Excelente")

elif nota >= 80:
   print ("Muito bom")

elif nota >= 70:
   print ("Bom")

else:
   print ("Precisa melhorar")

# Neste exemplo, são avaliadas múltiplas condições em ordem. Se a variável nota for maior ou igual a 90, será impresso "Excelente". Se não se cumprir a primeira condição, mas nota for maior ou igual a 80, será impresso "Muito bom". Se não se cumprirem as condições anteriores, mas nota for maior ou igual a 70, será impresso "Bom". Se nenhuma das condições anteriores for verdadeira, será executado o bloco else e será impresso "Precisa melhorar".