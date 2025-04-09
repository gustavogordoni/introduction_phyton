# Escrita de arquivos
# Para escrever dados em um arquivo, abrimos em modo de escrita ("w") utilizando a função open(). Se o arquivo não existir, será criado automaticamente. Se o arquivo já existir, seu conteúdo será sobrescrito.

arquivo = open("dados.txt", "w")
arquivo.write("Olá, mundo!")
arquivo.close()

# Neste exemplo, o arquivo "dados.txt" é aberto em modo de escrita utilizando open(). Depois, a string "Olá, mundo!" é escrita no arquivo utilizando o método write(). Finalmente, o arquivo é fechado utilizando o método close().

    # Importante
# É importante fechar sempre os arquivos depois de utilizá-los para liberar os recursos do sistema. 