# Define una variable de cada tipo primitivo
# Cadena de caracteres --> str(): Las cadenas de caracteres representan texto.
#   se crean cadenas utilizando comillas simples ('texto') o dobles ("texto").
nombre = 'Ariel'
colorFav = "Blanco"

# Enteros --> int(): los numeros enteros representan numeros sin parte fraccional
edad = 27

# Numeros de punto flotantes --> float(): Los numeros de punto flotante representan
#   numeros con parte fraccional.
numero = 45.7

# Booleanos --> bool(): Los booleanos representan valores de verdad (True) o falso (False).
#   Se Utilizan en expresiones logicas y de control de flujo
seraVdd = True

# 1) concatena a la cadena las otras variables aplicando la conversion correcta
#    para funcionar, guarde el resultado en una variable
resultadoUno = 'Hola mi nombre es ' + nombre + ' yo tengo ' + str(edad) + ' años mi color favorito es el ' + colorFav


# 2) Investiga sobre el limite de los enteros y los flotantes en python y anotar sus
#    descrubimientos como comentarios en el archivo

# En Python, los enteros y los flotantes no tienen un limite en terminos de su
# valor maximo o minimo. En lugar de tener un limite fijo, estos tipos de datos pueden
# crecer o encogerese segun sea necesario para acomodar el valor que estas
# almacenando. Esto se debe a que Python utiliza una representacion dinamica de
# datos para numeros enteros y flotantes, lo que significa que el tamaño de la memoria
# asignada para un numero en particular se ajusta automaticamente para acomodar su valor.

# Sin embargo, hay limitaciones prácticas en función de la cantidad de memoria
# disponible en tu sistema y el rendimiento de la máquina. A medida que los números
# enteros o flotantes aumentan en magnitud, pueden requerir más memoria y pueden
# llevar más tiempo realizar cálculos con ellos.

# Para números enteros, en la mayoría de las implementaciones de Python, los enteros
# se almacenan de forma nativa en la memoria, lo que significa que el tamaño de un
# entero en bytes depende de la arquitectura del sistema. Por ejemplo, en una arquitectura
# de 64 bits, los enteros se almacenan en 4, 8 o más bytes, lo que proporciona una amplia
# gama de valores enteros que pueden representarse. El límite práctico se encuentra en la
# cantidad de memoria disponible en tu sistema.

# Para números de punto flotante, Python utiliza el estándar IEEE 754 para representar números
# en coma flotante, que tiene una precisión finita y un rango limitado. Los números de punto
# flotante tienen límites de representación en términos de su valor máximo y mínimo. En Python,
# puedes obtener estos límites usando las constantes sys.float_info.max y sys.float_info.min.

# Es importante tener en cuenta que cuando trabajas con números muy grandes o muy pequeños en
# Python, es posible que te encuentres con problemas de precisión debido a las limitaciones de
# representación de punto flotante. Para cálculos de alta precisión, Python proporciona la
# biblioteca decimal que te permite trabajar con números decimales con una precisión arbitraria.

# En resumen, Python no tiene límites fijos para enteros y flotantes, pero hay límites prácticos
# en función de la memoria y el rendimiento de la máquina. Los números enteros pueden crecer hasta
# que se agote la memoria disponible, mientras que los números de punto flotante tienen límites
# determinados por el estándar IEEE 754.


# 3) Aplica la formula de la suma de los primeros n numeros pares (investigar), tomando como
#    n la variable de tipo entero y almacenar el resultado en una variable

# suma_n = es la suma de los primeros 'n' terminos
# n = es el numero de terminos que desea sumar
# formula = suma_n = n * (n + 1)

n = 10
suma_n = n * (n + 1)

# 4) imprimir los resultados de las tareas anteriores

print(resultadoUno)

print('suma_n = n * (n + 1) = ' + str(suma_n))

