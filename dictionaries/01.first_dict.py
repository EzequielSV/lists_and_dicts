# Los diccionarios son estructuras similares a las listas o arreglos, pero se accede a sus elementos mediante "llaves" o "keys" y no por su índice

# Ejemplo
# Definimos un diccionario utilizando llaves o "curly braces"
programer = {
    "name": "Alice",
    "position": "Fullstack Developer",
    "skills": ["Python", "Git", "SQL", "HTML", "CSS", "Javascript"]
}

# Accdemos a los elementos por la llave
print(programer["name"])
# No podemos acceder por el índice
# print(programmer[0])
print(programer["position"])
print(programer["skills"])

# También podemos acceder a sus elementos con el método get()
print(programer.get("position"))

# Son de tipo <class dict>
print(type(programer))

# Podemos acceder a todas sus llaves con el método keys()
keys = programer.keys()
print(keys)