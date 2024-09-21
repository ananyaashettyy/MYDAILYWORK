import json
import os
from datetime import datetime

class ToDoList:
    def __init__(self, file_name="tasks.json"):
        self.file_name = file_name
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as file:
                self.tasks = json.load(file)
        else:
            self.tasks = []

    def save_tasks(self):
        with open(self.file_name, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task, priority="Medium", category="General", deadline=None):
        task_data = {
            "task": task,
            "priority": priority,
            "category": category,
            "deadline": deadline,
            "completed": False
        }
        self.tasks.append(task_data)
        self.save_tasks()
        print(f"Task '{task}' added successfully!")

   
    def update_task(self, task_number, new_task):
        if 0 <= task_number < len(self.tasks):
            self.tasks[task_number]["task"] = new_task
            self.save_tasks()
            print(f"Task {task_number+1} updated to: '{new_task}'")
        else:
            print("Invalid task number.")

   
    def delete_task(self, task_number):
        if 0 <= task_number < len(self.tasks):
            removed_task = self.tasks.pop(task_number)
            self.save_tasks()
            print(f"Task '{removed_task['task']}' deleted successfully!")
        else:
            print("Invalid task number.")

    
    def complete_task(self, task_number):
        if 0 <= task_number < len(self.tasks):
            self.tasks[task_number]["completed"] = True
            self.save_tasks()
            print(f"Task {task_number+1} marked as completed!")
        else:
            print("Invalid task number.")

    
    def view_tasks(self, filter_by=None, search_keyword=None):
        filtered_tasks = self.tasks

       
        if filter_by == "completed":
            filtered_tasks = [task for task in self.tasks if task["completed"]]
        elif filter_by == "incomplete":
            filtered_tasks = [task for task in self.tasks if not task["completed"]]

        
        if search_keyword:
            filtered_tasks = [task for task in filtered_tasks if search_keyword.lower() in task["task"].lower()]

       
        if len(filtered_tasks) == 0:
            print("No tasks found!")
        else:
            for i, task in enumerate(filtered_tasks):
                status = "Completed" if task["completed"] else "Incomplete"
                deadline = task["deadline"] if task["deadline"] else "No deadline"
                print(f"{i+1}. {task['task']} - [Priority: {task['priority']}, Category: {task['category']}, Deadline: {deadline}, Status: {status}]")

   
    def search_tasks(self, keyword):
        self.view_tasks(search_keyword=keyword)

   
    def filter_tasks(self, status):
        self.view_tasks(filter_by=status)



def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Application")
        print("1. Add a task")
        print("2. Update a task")
        print("3. Delete a task")
        print("4. Mark task as completed")
        print("5. View all tasks")
        print("6. Search tasks")
        print("7. Filter tasks (completed/incomplete)")
        print("8. Exit")

        try:
            choice = int(input("Enter your choice (1-8): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            task = input("Enter a task: ")
            priority = input("Enter task priority (High/Medium/Low): ")
            category = input("Enter task category (e.g., Work, Personal): ")
            deadline = input("Enter task deadline (YYYY-MM-DD) or leave blank: ")
            if deadline:
                try:
                    deadline = datetime.strptime(deadline, "%Y-%m-%d").strftime("%Y-%m-%d")
                except ValueError:
                    print("Invalid date format. Setting no deadline.")
                    deadline = None
            todo_list.add_task(task, priority, category, deadline)

        elif choice == 2:
            todo_list.view_tasks()
            try:
                task_num = int(input("Enter the task number to update: ")) - 1
                new_task = input("Enter the updated task: ")
                todo_list.update_task(task_num, new_task)
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        elif choice == 3:
            todo_list.view_tasks()
            try:
                task_num = int(input("Enter the task number to delete: ")) - 1
                todo_list.delete_task(task_num)
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        elif choice == 4:
            todo_list.view_tasks()
            try:
                task_num = int(input("Enter the task number to mark as completed: ")) - 1
                todo_list.complete_task(task_num)
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        elif choice == 5:
            todo_list.view_tasks()

        elif choice == 6:
            keyword = input("Enter a keyword to search for: ")
            todo_list.search_tasks(keyword)

        elif choice == 7:
            status = input("Enter filter (completed/incomplete): ").lower()
            if status in ["completed", "incomplete"]:
                todo_list.filter_tasks(status)
            else:
                print("Invalid filter. Choose 'completed' or 'incomplete'.")

        elif choice == 8:
            print("Exiting the application. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
