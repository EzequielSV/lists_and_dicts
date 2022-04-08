programer = {
    "name": "Alice",
    "position": "Fullstack Developer",
    "skills": ["Python", "Git", "SQL", "HTML", "CSS", "Javascript"]
}

# Por defecto itera sobre las llaves, pero podría ser cualquier nombre: ej attr
for key in programer:
    print(key)

# Podriamos imprimir los valores
for key in programer:
    print(programer[key])

for key, value in programer.items():
    print(key, ":", value)