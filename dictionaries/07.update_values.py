programer = {
    "name": "Alice",
    "position": "Fullstack Developer",
    "skills": ["Python", "Git", "SQL", "HTML", "CSS", "Javascript"]
}

# Actualizamos indicando  la llave con el nuevo valor
programer["position"] = "Sr Software Developer"

print(programer)

# Actualizando utilizando el método update entregando un diccionario con la llave a actualizar
programer.update({"name" : "Alice Smith"})

print(programer)

# Con el método update() podemos también agregar nuevas llaves con su valor 
programer.update({"hobbies": ["Cats", "Plastation", "Contemplate the moon"]})

print(programer)