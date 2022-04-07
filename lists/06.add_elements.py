from concurrent.futures.process import BrokenProcessPool

from matplotlib.animation import MovieWriterRegistry


todo_list = ["estudiar python", "sacar la basura", "alimentar al Boby", "Recibir el bono", "barrer la entrada"]

# Agrega un item en el índice del primer parámetro, desplazando los otros items
todo_list.insert(2, "bañarme")

todo_list.append("Ver Friends")

print(todo_list)

# Mezclar

movies = ["El día de la independencia", "American Pie", "Scary Movie"]

books = ["Harry Potter", "The Bro Code", "Cómo entrenar a tu dragón"]

#Agrega al final todo el arreglo entregado como parámetro
movies.extend(books)

print(movies)

print(books)