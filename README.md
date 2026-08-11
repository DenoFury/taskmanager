# Task Manager CLI

A command-line task manager for adding, completing, and deleting tasks, built around a proper OOP design with validated data, custom exceptions, and JSON persistence between runs.

## Features
- Add, view, complete, and delete tasks through a menu-driven loop
- Each task has a title, optional description, completion status, and a date (auto-filled with today's date if left blank)
- Tasks are validated on creation (e.g. an empty title is rejected)
- Tasks persist between runs — saved to `data.json` on exit and reloaded automatically on startup, with original task IDs preserved
- Custom exception (`TaskNotFoundError`) for operations on a task ID that doesn't exist
- Handles invalid menu input and invalid task IDs gracefully, without crashing

## Tech Stack
- Python
- OOP — `Task` and `TaskManager` classes, with `@property`/setter validation on `Task`'s fields
- `json` — persistence
- `os` — checking for an existing save file
- `match`/`case` — menu branching

## Installation
```bash
git clone https://github.com/DenoFury/task-manager-cli.git
cd task-manager-cli
python task_manager.py
```

## Usage
```
What would you like to do:
 1. Create task
 2. View tasks
 3. Delete Task
 4. Complete task
 5. Quit
1
Name of your task: Buy groceries
Description of task (optional): Milk, eggs, bread
Choose a date: 
Task created successfully! Going back to main menu....

What would you like to do:
 1. Create task
 2. View tasks
 3. Delete Task
 4. Complete task
 5. Quit
2
Task id: 1 - Your task Buy groceries is False due 08/07/26
```
Tasks are saved automatically when you choose option 5 (Quit), and reloaded the next time the program runs.

## How It Works
- **`Task`** models a single task, with each field (`title`, `description`, `done`, `date`) implemented as a validated property. `title` can't be empty, `done` must be a real boolean, and `date` defaults to today's date (computed fresh at creation time) if none is provided.
- **`TaskManager`** owns a dict of `Task` objects keyed by a stable, auto-incrementing ID (`next_id`) — chosen over a plain list specifically so deleting a task never shifts or renumbers the others.
- **Persistence**: `save()` converts each `Task` to a plain dict via `Task.to_dict()` and writes the whole collection to `data.json`. `load()` reads the file back (if it exists), reconstructs real `Task` objects, and — critically — restores each task under its *original* saved ID rather than reassigning fresh ones, so IDs stay stable across restarts. `next_id` is also recalculated on load, based on the highest existing ID, so new tasks never collide with reloaded ones.
- **Error handling**: invalid menu choices and invalid task IDs are caught with targeted `except ValueError` blocks; operations on a non-existent task ID raise and catch a custom `TaskNotFoundError` instead of crashing.

## Future Improvements
- Save automatically after every action instead of only on exit, to avoid losing progress if the program is interrupted unexpectedly
- Due dates with actual date validation/parsing, rather than free-text input
- Task priorities or categories
- Edit an existing task's title/description instead of only add/complete/delete

## Lessons Learned
First project built with real OOP design rather than just syntax — working through when a `@property` setter should validate versus just store, and catching subtle bugs like a mutable default argument being computed once at class-definition time instead of fresh per object (the `date` field). Also the first project handling two-way data conversion (`Task` ↔ plain dict) for persistence, including a fiddly edge case: JSON only supports string dict keys, so loaded task IDs have to be explicitly converted back to `int`, and IDs need to be preserved deliberately on reload rather than relying on the normal `add_task()` path, which would have silently renumbered everything.