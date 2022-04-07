todo_list = ["estudiar python", "sacar la basura", "alimentar al Boby", "Recibir el bono", "barrer la entrada"]

# Podemos eliminar un elemento en particular
todo_list.remove("Recibir el bono")

print(todo_list)

# Podemos eliminar el último elemento con el método pop(). También acepta el índice
element = todo_list.pop()

print(todo_list)
print(element)

# También existe la palabra clave "del"
del todo_list[1]

print(todo_list)

# Esto lo elimina del programa!
del todo_list

# print(todo_list)

todo_list = ["estudiar python", "sacar la basura", "alimentar al Boby", "Recibir el bono", "barrer la entrada"]

# Limpía toda la lista, pero no la elimina
todo_list.clear()

print(todo_list)