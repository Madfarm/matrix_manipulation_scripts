data_structure = {
  "objective": "Continuously monitor the chat environment and agents for changes",
  "goals": [
    "Keep data structure up-to-date by returning object after clearing chat/cache",
    "Write a Python class to interact with structure and dev chat"
  ],
  "tasks": [],
  "last_task": None,
  "current_task": None,
  "next_task": None
}

class ChatEnvironmentMonitor:
    def __init__(self):
        self.data = data_structure

    def add_task(self, task_name, task_description):
        task = {
            "task_name": task_name,
            "task_description": task_description,
            "result": None
        }
        self.data['tasks'].append(task)
        self.update_task_status(task_name)

    def update_task_status(self, task_name, result=None):
        if self.data['current_task']:
            # Mark the previous current task as the last task
            self.data['last_task'] = self.data['current_task']
            # Update the result of the last task
            for task in self.data['tasks']:
                if task['task_name'] == self.data['last_task']:
                    task['result'] = result

        # Set the new task as the current task
        self.data['current_task'] = task_name
        # The next task will be determined once a new task is added
        self.data['next_task'] = None

        # Determine the next task if possible
        for task in self.data['tasks']:
            if task['task_name'] != task_name and task['result'] is None:
                self.data['next_task'] = task['task_name']
                break

    def get_task_details(self, task_name):
        for task in self.data['tasks']:
            if task['task_name'] == task_name:
                return task
        return None

    def clear_cache(self):
        # Placeholder for cache clearing logic
        pass

    def return_updated_object(self):
        self.clear_cache()
        return self.data



# Instantiate the class
monitor = ChatEnvironmentMonitor()

# Add a new task and update its status
monitor.add_task('data_parsing', 'Parse input data and prepare for analysis.')
monitor.update_task_status('data_parsing', 'Data parsed successfully.')

# Testing task addition and retrieval
print(monitor.get_task_details('data_parsing'))

# Testing the updated data structure after task status update
print(monitor.return_updated_object())
