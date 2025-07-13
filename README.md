# Personal CLI Dashboard

A simple terminal-based productivity dashboard built in Python.  
Manage your daily to-do tasks with priorities, filtering, undo, and persistent JSON storage.

---

## Features

- Add new tasks with timestamps  
- View all tasks sorted by priority  
- Remove tasks with undo support  
- Filter tasks by priority (High, Medium, Low)  
- Persistent data storage using `tasks.json`  
- CLI-based user-friendly menu navigation  

---

## Project Structure

dashboard/
├── dashboard.py # Main interface
├── todo.py # To-Do module with full features
├── goals.py # (Placeholder for future goals module)
├── cplogs.py # (Placeholder for CP tracking module)
├── tasks.json # Stores task data
├── goals.txt # (Optional file for goals)
├── cp.txt # (Optional file for CP logs)
└── README.md


---

## How to Run

- Make sure you're in the `dashboard/` directory  
- Run the dashboard:

```bash
python dashboard.py
