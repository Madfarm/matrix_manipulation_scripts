class TodoList:
    def __init__(self):
        self.todos = []

    def add_todo(self, todo, priority=0):
        self.todos.append({"todo": todo, "priority": priority})
        self.sort_todos()

    def delete_todo(self, index):
        if index < len(self.todos):
            del self.todos[index]
        else:
            print("Todo index out of range")

    def edit_todo(self, index, todo, priority=0):
        if index < len(self.todos):
            self.todos[index] = {"todo": todo, "priority": priority}
            self.sort_todos()
        else:
            print("Todo index out of range")

    def display_todos(self):
        for index, todo in enumerate(self.todos):
            print(f"{index}: {todo['todo']} (Priority: {todo['priority']})")

    def sort_todos(self):
        self.todos.sort(key=lambda x: x['priority'], reverse=True)


# Testing the class
todo_list = TodoList()

todo_list.add_todo("Buy groceries", 1)
todo_list.add_todo("Finish project", 2)
todo_list.add_todo("Call mom", 0)

todo_list.display_todos()

todo_list.edit_todo(0, "Buy groceries and cook dinner", 2)

todo_list.display_todos()

todo_list.delete_todo(1)

todo_list.display_todos()