# Tipo de dato compuesto - tupla - estático:

punto = (2, 5)
print('Tipo de dato:', type(punto))
print('Contenido de la variable punto:', punto)
print('Cantidad elementos de la tupla punto:', len(punto))

print()

# Acceso a los elementos de una tupla:
x = punto[0]
y = punto[1]
print('El valor en x es igual a:', x)
print('El valor en y es igual a:', y)

print()

# Desempaquetamiento:
abscisa, ordenada = punto
print('El valor en x es igual a:', abscisa)
print('El valor en y es igual a:', ordenada)

print()

# Acceso con índices negativos (de derecha a izquierda):

penultimo_elemento = punto[-2]
ultimo_elemento = punto[-1]
print('El valor en x es igual a:', penultimo_elemento)
print('El valor en y es igual a:', ultimo_elemento)
