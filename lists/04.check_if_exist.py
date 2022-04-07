todo_list = ["estudiar python", "sacar la basura", "alimentar al Boby", "Recibir el bono", "barrer la entrada"]

def check_if_exist(check, list):
    if check in list:
        return True

if check_if_exist("Recibir el bono", todo_list):
    print("tienes cosas por hacer")
else:
    print("Sin bono sigo en cama")