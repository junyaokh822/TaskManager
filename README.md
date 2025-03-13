# Task Manager

A Python-based Task Manager application that allows users to create, manage, and track tasks. This project includes features such as adding tasks, marking tasks as completed, filtering tasks by status, and sorting tasks by priority.

## Features

- **Task Creation**: Create tasks with a title, description, and priority.
- **Task Completion**: Mark tasks as completed.
- **Task Filtering**: Filter tasks by their status (e.g., "Pending" or "Completed").
- **Task Sorting**: Sort tasks by priority.
- **Task Display**: Display tasks in a user-friendly format.

## Code Structure

The project is organized into the following classes:

### `Task`
Represents a task with attributes:
- `title`: The title of the task.
- `description`: A brief description of the task.
- `priority`: The priority level of the task (lower numbers indicate higher priority).
- `status`: The current status of the task, defaulting to "Pending".

Methods:
- `mark_as_completed()`: Marks the task as completed.
- `__str__()`: Returns a string representation of the task.
- `create_task(title, description, priority)`: Factory method to create a task.

### `ITaskManager` (Interface)
Abstract base class defining the interface for a task manager. Implementations must provide:
- `add_task(task)`: Adds a new task to the task manager.
- `complete_task(title)`: Marks a task as completed by its title.
- `get_tasks(status)`: Retrieves tasks, optionally filtered by status.

### `TaskManager`
Implements the `ITaskManager` interface and manages a collection of tasks.

Methods:
- `add_task(task)`: Adds a task to the task manager.
- `complete_task(title)`: Marks a task as completed by its title.
- `get_tasks(status)`: Retrieves tasks, optionally filtered by status.
- `show_tasks(status)`: Displays tasks, optionally filtered by status.

### `TaskSorter`
Provides utility methods for sorting tasks.

Methods:
- `sort_by_priority(tasks)`: Sorts a list of tasks by priority (ascending order).

## Usage

1. **Clone the repository**:
   ```bash
   git clone https://github.com/junyaokh822/TaskManager.git
   cd TaskManager

2. Run the Script:
   ```bash
   python main.py

3. Interact with the Task Manager:
   - Add tasks using the Task.create_task() factory method.
   - Mark tasks as completed using the complete_task() method.
   - Filter and display tasks by status using show_tasks(status).
   - Sort tasks by priority using TaskSorter.sort_by_priority().
