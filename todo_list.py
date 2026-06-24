tasks = []

def add_task(name):
    tasks.append({"task": name, "done": False})
    print(f"Added: {name}")

def view_tasks():
    if not tasks:
        print("No tasks yet.")
        return
    for i, t in enumerate(tasks, start=1):
        status = "[x]" if t["done"] else "[ ]"
        print(f"{i}. {status} {t['task']}")

def mark_done(index):
    if 0 < index <= len(tasks):
        tasks[index - 1]["done"] = True
        print("Marked as done.")
    else:
        print("Invalid task number.")

def delete_task(index):
    if 0 < index <= len(tasks):
        removed = tasks.pop(index - 1)
        print(f"Deleted: {removed['task']}")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\n1. Add  2. View  3. Mark Done  4. Delete  5. Exit")
        choice = input("Choose: ")

        if choice == "1":
            add_task(input("Task: "))
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_tasks()
            mark_done(int(input("Task number: ")))
        elif choice == "4":
            view_tasks()
            delete_task(int(input("Task number: ")))
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()