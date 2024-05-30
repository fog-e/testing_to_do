import csv

TODO_FILE = 'todos.csv'

def read_and_write_todos(fn):
    def wrapper(*args):
        todos = read_todos(TODO_FILE)
        result = fn(todos, *args)
        write_todos(result, TODO_FILE)
        return result
    return wrapper

def read_todos(filename):
    todos_file = open(filename, "r")
    file_contents = todos_file.read()
    todos = file_contents.split("\n")
    todos_file.close()
    todos_in_parts = []
    for todo in todos:
        todo_parts = todo.split(",")
        if len(todo_parts) > 1:
            todo_dict = {
                "done": todo_parts[2],
                "todo_text": todo_parts[1],
                "todo_id": todo_parts[0]
            }
            todos_in_parts.append(todo_dict)
    return todos_in_parts

def write_todos(todos, filename):
    todos_file = open(filename, 'w')
    todos_file.write("id,todo_text,done\n")
    for todo in todos:
        done = str(todo["done"])
        todo_text = str(todo["todo_text"])
        todo_id = str(todo["todo_id"])
        todo_parts = [todo_id, todo_text, done]
        put_back_together = ",".join(todo_parts)
        todos_file.write(put_back_together + "\n")

@read_and_write_todos
def view_incomplete_todos(todos):
    for todo in todos:
        if todo["done"] == "0":
            print(f"{todo['todo_id']}: {todo['todo_text']}")
    return todos

@read_and_write_todos
def complete_todo(todos, completed_todo_id):
    for todo in todos:
        if completed_todo_id == todo["todo_id"]:
            todo["done"] = "1"
    return todos

@read_and_write_todos
def undo_todo(todos, todo_id):
    for todo in todos:
        if todo_id == todo["todo_id"]:
            todo["done"] = "0"
    return todos

@read_and_write_todos
def delete_todo(todos, todo_id):
    todos = [todo for todo in todos if todo["todo_id"] != todo_id]
    return todos

@read_and_write_todos
def add_todo(todos, todo_text):
    last_id = int(todos[-1]["todo_id"]) if todos else 0
    new_todo = {
        "todo_text": todo_text,
        "todo_id": str(last_id + 1),
        "done": "0"
    }
    todos.append(new_todo)
    return todos

def main():
    while True:
        user_input = input("> what would you like to do? view, add, done, undo, delete, or exit: ").strip().lower()
        if user_input == "view":
            view_incomplete_todos()
        elif user_input.startswith("add "):
            todo_text = user_input[4:].strip('"')
            add_todo(todo_text)
        elif user_input.startswith("done "):
            try:
                todo_id = user_input.split()[1]
                complete_todo(todo_id)
            except IndexError:
                print("Invalid command. Usage: done <id>")
        elif user_input.startswith("undo "):
            try:
                todo_id = user_input.split()[1]
                undo_todo(todo_id)
            except IndexError:
                print("Invalid command. Usage: undo <id>")
        elif user_input.startswith("delete "):
            try:
                todo_id = user_input.split()[1]
                delete_todo(todo_id)
            except IndexError:
                print("Invalid command. Usage: delete <id>")
        elif user_input == "exit":
            break
        else:
            print("Unknown command. Please enter 'view', 'add', 'done', 'undo', 'delete', or 'exit'.")

if __name__ == "__main__":
    main()
