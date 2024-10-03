class TodoList:
    def __init__(self):
        self.todo_list = []

    # non return method
    def add_list(self, element):
        self.todo_list.append(element)

    def remove_index(self, idx):
        self.todo_list.pop(idx)

    # return method
    def format_list(self):
        out = ""

        for i, element in enumerate(self.todo_list):
            out += "\n{}. {}".format(i + 1, element)

        return out


# return function
def return_names():
    return ["Habib","Grey","Willy","kevin"]
    


# non return function
def display_help():
    print("help\nMenampilkan help ini")
    print("\nadd [teks]\nMenambahkan teks kedalam list")
    print("\nremove [n]\nMenghapus elemen ke-n didalam list")
    print("\nlist\nMenampilkan list")
    print("\nexit\nMenutup program")
    print("\ninfo\nMenampilkan anggota kelompok")


todo = TodoList()

print("Program Todo List Kelompok 41")
while True:
    command = input("\n> ").split(" ", 1)

    if command[0] == "help":
        display_help()
    elif command[0] == "exit":
        break
    elif command[0] == "add":
        todo.add_list(command[1])
    elif command[0] == "remove":
        if not command[1].isdigit():
            print("Harus menggunakan angka!")
        elif int(command[1]) > len(todo.todo_list) or int(command[1]) <= 0:
            print("Angka diluar jangkauan!")
        else:
            todo.remove_index(int(command[1]) - 1)
    elif command[0] == "list":
        if len(todo.todo_list) > 0:
            print(todo.format_list())
        else:
            print("List masih kosong!")
    elif command[0] == "info":
        print(", ".join(return_names()))
    else:
        print("Perintah tidak dikenal. Mohon tulis 'help' untuk perintah yang dapat dilakukan.")

print("Terima kasih")
