from abc import ABC, abstractmethod
from typing import List, Dict, Optional

# Task Class
class Task:
    def __init__(self, title: str, description: str, priority: int):
        """
        Represents a task with a title, description, priority, and status.
        - title: The title of the task.
        - description: A brief description of the task.
        - priority: The priority level of the task (lower numbers indicate higher priority).
        - status: The current status of the task, defaulting to "Pending".
        """
        self.title = title
        self.description = description
        self.priority = priority
        self.status = "Pending"

    def mark_as_completed(self):
        """Marks the task as completed by updating its status."""
        self.status = "Completed"

    def __str__(self):
        """Returns a string representation of the task."""
        return f"{self.title} - {self.description} (Priority: {self.priority}, Status: {self.status})"

    @staticmethod
    def create_task(title: str, description: str, priority: int):
        """
        Factory method to create a task.
        - title: The title of the task.
        - description: A brief description of the task.
        - priority: The priority level of the task.
        """
        return Task(title, description, priority)

# TaskManager Interface
class ITaskManager(ABC):
    """
    Abstract base class defining the interface for a task manager.
    Any class implementing this interface must provide implementations for these methods.
    """
    @abstractmethod
    def add_task(self, task: Task):
        """Adds a new task to the task manager."""
        pass

    @abstractmethod
    def complete_task(self, title: str):
        """Marks a task as completed by its title."""
        pass

    @abstractmethod
    def get_tasks(self, status: Optional[str] = None):
        """Retrieves tasks, optionally filtered by status."""
        pass

# TaskManager Class
class TaskManager(ITaskManager):
    def __init__(self):
        """
        Initializes the task manager with an empty dictionary to store tasks.
        The dictionary uses task titles as keys for O(1) lookups.
        """
        self.tasks: Dict[str, Task] = {}

    def add_task(self, task: Task):
        """
        Adds a task to the task manager.
        - task: The task to add.
        Raises a ValueError if a task with the same title already exists.
        """
        if task.title in self.tasks:
            raise ValueError(f"Task with title '{task.title}' already exists.")
        self.tasks[task.title] = task

    def complete_task(self, title: str):
        """
        Marks a task as completed by its title.
        - title: The title of the task to mark as completed.
        Raises a ValueError if the task is not found.
        """
        if title not in self.tasks:
            raise ValueError(f"Task with title '{title}' not found.")
        self.tasks[title].mark_as_completed()

    def get_tasks(self, status: Optional[str] = None):
        """
        Retrieves tasks, optionally filtered by status.
        - status: The status to filter tasks by (e.g., "Pending", "Completed").
        Returns a list of tasks matching the status, or all tasks if no status is provided.
        """
        if status:
            return [task for task in self.tasks.values() if task.status == status]
        return list(self.tasks.values())

    def show_tasks(self, status: Optional[str] = None):
        """
        Displays tasks, optionally filtered by status.
        - status: The status to filter tasks by (e.g., "Pending", "Completed").
        Prints a message if no tasks are found.
        """
        tasks = self.get_tasks(status)
        if not tasks:
            print(f"No tasks found with status '{status}'." if status else "No tasks to display.")
        else:
            for task in tasks:
                print(task)

# TaskSorter Class
class TaskSorter:
    @staticmethod
    def sort_by_priority(tasks: List[Task]):
        """
        Sorts a list of tasks by priority (ascending order).
        - tasks: The list of tasks to sort.
        Returns the sorted list of tasks.
        """
        return sorted(tasks, key=lambda x: x.priority)

# Main Program
if __name__ == "__main__":
    # Create a task manager instance
    manager = TaskManager()

    # Adding tasks using the factory method
    manager.add_task(Task.create_task("Buy groceries", "Milk, Bread, Eggs", 2))
    manager.add_task(Task.create_task("Finish project", "Complete To-Do List Manager", 1))
    manager.add_task(Task.create_task("Call plumber", "Fix leaking faucet", 3))
    manager.add_task(Task.create_task("Plan vacation", "Book flights and hotels", 4))
    manager.add_task(Task.create_task("Read a book", "Finish 'The Alchemist'", 5))

    # Completing tasks
    manager.complete_task("Buy groceries")
    manager.complete_task("Call plumber")

    # Display all tasks
    print("All Tasks:")
    manager.show_tasks()

    # Display pending tasks
    print("\nPending Tasks:")
    manager.show_tasks("Pending")

    # Display completed tasks
    print("\nCompleted Tasks:")
    manager.show_tasks("Completed")

    # Display tasks sorted by priority
    print("\nTasks Sorted by Priority:")
    sorted_tasks = TaskSorter.sort_by_priority(manager.get_tasks())
    manager.show_tasks() if sorted_tasks else print("No tasks to sort.")