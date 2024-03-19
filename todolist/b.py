class TodoList:
    def __init__(self):
        self.todos = []

    def add_todo(self, todo):
        self.todos.append(todo)

    def delete_todo(self, index):
        if index < len(self.todos):
            del self.todos[index]
        else:
            print("Index out of range")

    def edit_todo(self, index, new_todo):
        if index < len(self.todos):
            self.todos[index] = new_todo
        else:
            print("Index out of range")

    def display_todos(self):
        for index, todo in enumerate(self.todos):
            print(f"{index + 1}. {todo}")

    def sort_todos(self, priority):
        if priority == 'ascending':
            self.todos.sort()
        elif priority == 'descending':
            self.todos.sort(reverse=True)
        else:
            print("Invalid priority. Must be either 'ascending' or 'descending'")

    def __str__(self):
        return f"TodoList({self.todos})"

# Test the TodoList class
todo_list = TodoList()
todo_list.add_todo("Task 1")
todo_list.add_todo("Task 2")
todo_list.add_todo("Task 3")
todo_list.display_todos()
todo_list.edit_todo(1, "Edited task 2")
todo_list.display_todos()
todo_list.delete_todo(2)
todo_list.display_todos()
todo_list.sort_todos('ascending')
todo_list.display_todos()
todo_list.sort_todos('descending')
todo_list.display_todos()
print(todo_list)