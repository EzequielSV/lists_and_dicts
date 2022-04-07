todo_list = ["estudiar python", "sacar la basura", "alimentar al Boby", "Recibir el bono", "barrer la entrada"]

for todo in todo_list:
    print(todo)

index = 0
while index < len(todo_list):
    print(todo_list[index])
    index += 1

# El índiice termina en 5 por la úlima iteración
print(index)

# Utilizando list comprehensions
[print(todo) for todo in todo_list]
