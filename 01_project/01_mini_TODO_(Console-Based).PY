def add_task():
	task = input("Enter you task: ")
	with open("todo.txt","a") as file:
		file.write(task+"\n")
	print("Task added!\n")
def view_task():
	print("\nYour TO-DO List:")
	try:
		with open("todo.txt","r") as file:
			tasks = file.readlines()
			if not tasks:
				print("No task found.")
			else:
				for idx, task in enumerate(tasks,1):
					print(f"{idx}.{task.strip()}")
	except FileNotFoundError:
		print("No task file found.")
	print()
def del_task():
	open("todo.txt","w").close() #clears the file
	print("All task deleted.\n")
while True:
	print("1. Add Task\t2. View Task\n3. Delete All Task\t4. Exit")
	choice = input("Choose an Option(1-4): ")
	if choice == "1":
		add_task()
	elif choice == "2":
		view_task()
	elif choice == "3":
		del_task()
	elif choice == "4":
		print("Good Bye 👋")
		break
	else:
		print("Invalid choice. Try again.\n")