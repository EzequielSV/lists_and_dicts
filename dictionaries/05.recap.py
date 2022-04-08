programer = {
    "name": "Alice",
    "position": "Fullstack Developer",
    "skills": ["Python", "Git", "SQL", "HTML", "CSS", "Javascript"]
}

# Estas variables quedan referencias que se actualizan
keys = programer.keys()
values = programer.values()
items = programer.items()

print(keys)
print(values)
print(items)

# Acá estamos agregando un nuevo ítem
programer["dream"] = "Be a Python pro"

# Las llaves se actualizan considerando la nueva llave y valor agregados
print(keys)