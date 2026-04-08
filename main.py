print ("This is your To-do list: EMPTY")
todo_list = []
while True:
    task = input("Enter a task to add to your To-do list (or type 'exit' to quit): ")
    if task.lower() == 'exit':
        break
    todo_list.append(task)
    print("This is your To-do list:")
    for idx, item in enumerate(todo_list, start=1):
        print(f"{idx}. {item}")
print("Goodbye!")   
