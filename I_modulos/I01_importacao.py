    # Importar módulos
# Para utilizar um módulo em nosso programa, devemos importá-lo utilizando a declaração import. Podemos importar um módulo completo ou funções específicas de um módulo.

import math

resultado = math.sqrt(25)
print(resultado)  # Imprime 5.0

# Neste exemplo, importa-se o módulo math utilizando a declaração import. Em seguida, utiliza-se a função sqrt() do módulo math para calcular a raiz quadrada de 25.

# Também podemos importar funções específicas de um módulo utilizando a sintaxe from módulo import função.

from math import sqrt

resultado = sqrt(25)
print(resultado)  # Imprime 5.0

# Neste caso, importa-se apenas a função sqrt() do módulo math, o que nos permite utilizá-la diretamente sem ter que precedê-la com o nome do módulo.