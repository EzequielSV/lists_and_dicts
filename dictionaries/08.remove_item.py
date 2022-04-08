programer = {
    "name": "Alice",
    "position": "Fullstack Developer",
    "skills": ["Python", "Git", "SQL", "HTML", "CSS", "Javascript"]
}

# El método pop en los diccionarios requiere de las llaves a eliminar
#programer.pop("position")
#print(programer)
#print(position)

# Otra forma de eliminar la llave ejemplo "position"
del programer["position"]

print(programer)

# Eliminar el diccionario completo
del programer

# print(programer) # Esto es un error al eliminar el programer del programa

programer = {
    "name": "Alice",
    "position": "Fullstack Developer",
    "skills": ["Python", "Git", "SQL", "HTML", "CSS", "Javascript"]
}

# Vaciar el contenido del diccionario, pero manteniendo la variable
programer.clear()

print(programer) # {} es lo que se imprime
