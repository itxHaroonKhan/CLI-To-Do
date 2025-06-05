

# 📝 CLI To-Do App (Python + Click)

A simple and efficient command-line To-Do list application built using Python and the Click library. It stores tasks in a local JSON file for easy management.

---

## 🚀 Features

- ✅ Add new tasks  
- 📋 List all tasks  
- ✔️ Mark tasks as completed  
- ❌ Delete tasks  

---

## 🛠️ Requirements

- Python 3.x  
- Click library  

Install the required library using pip:

```bash
pip install click
````

---

## 📁 File Structure

```
main.py       # Main CLI application  
todo.json     # Local JSON file for storing tasks  
```

---

## ⚙️ Usage Instructions

### ▶️ Add a Task

```bash
python main.py add "Buy groceries"
```

### 📃 List All Tasks

```bash
python main.py list
```

### ✅ Mark a Task as Completed

```bash
python main.py complete 1
```

### 🗑️ Delete a Task

```bash
python main.py delete 1
```

---

## 📌 Notes

* All tasks are saved in `todo.json`
* Task IDs start from `1`
* ✔️ = Completed, ✖️ = Not completed

---

## 📥 Example Output

```bash
$ python main.py add "Finish homework"
Task added successfully: Finish homework

$ python main.py list
1. Finish homework [✖]
```

---

## 📄 License

This project is open-source and free to use under the MIT License.

---

**Developed by: Haroon Devlaper**

```

---

