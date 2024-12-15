import time
import random

def forgetful_todo_app():
    """A to-do app that messes with your tasks."""
    print("Welcome to the Memory-Impaired To-Do App!")
    tasks = []

    while True:
        task = input("Enter a task (or type 'view' or 'quit'): ").lower()

        if task == "quit":
            break
        elif task == "view":
            if tasks:
                if random.random() < 0.2:  # 20% chance of messing up the list
                    print("Hmm, the list seems a bit... scrambled.")
                    random.shuffle(tasks)  # Shuffle the task order.
                    for i, t in enumerate(tasks):
                       if random.random() < 0.3:
                         print(f"{i+1}. ...oops lost a task!") # Delete the task when trying to view it.
                         tasks.remove(t)
                       else:
                         print(f"{i+1}. {t}")
                else:
                  print("\nYour current tasks:")
                  for i, t in enumerate(tasks):
                     print(f"{i+1}. {t}")

            else:
              print("\nNo Tasks Yet. Add some!")
            continue


        if task:
            tasks.append(task)
            print(f"Task '{task}' added... maybe. We'll see.")
            time.sleep(random.uniform(1, 5))

            if random.random() > 0.5:
              if random.random() < 0.8:
                tasks.remove(task)
                print("...Whoops! I forgot it faster than you expected!")
              else:
                 if tasks:
                   replace_task = random.choice(tasks)
                   tasks[tasks.index(replace_task)] = f'Messed up version of: {task}'
                   print(f"Wait it's actually '{replace_task}' now!")

            else:
              if random.random() < 0.4:
                print("...Phew, it's still here, but for how long?")
              else:
                 print(f"Actually I don't think I saved it")
                 tasks.remove(task)

        else:
            print("No task entered. Or did I hear a cat?...")
        
        if random.random() < 0.1:
          print("You know what? I'm going to delete all your tasks...")
          tasks = []

if __name__ == "__main__":
    forgetful_todo_app()