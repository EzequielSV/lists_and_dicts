programer = {
    "name": "Alice",
    "position": "Fullstack Developer",
    "skills": ["Python", "Git", "SQL", "HTML", "CSS", "Javascript"]
}

# Por defecto al buscar en el diccionario, se busca por las llaves
if "position" in programer:
    print("Existe la posición")

# No va a buscar directamente a los valores
if "Alice" in programer:
    print("Alice está presente")

# De esta forma podemos buscar en los valores
if "Alice" in programer.values():
    print("Alice está en los valores")