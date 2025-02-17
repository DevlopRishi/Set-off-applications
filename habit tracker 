import json
import os
from datetime import datetime

DATA_FILE = 'habits.json'

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def add_habit(habits, name):
    if name in habits:
        print("Habit already exists.")
    else:
        habits[name] = {
            "logs": [],
            "streak": 0,
            "best_streak": 0
        }
        print(f"Habit '{name}' added.")

def log_habit(habits, name):
    if name not in habits:
        print("Habit not found.")
        return

    today = datetime.now().strftime('%Y-%m-%d')
    if today in habits[name]["logs"]:
        print("Habit already logged for today.")
    else:
        habits[name]["logs"].append(today)
        habits[name]["logs"].sort()
        update_streak(habits, name)
        print(f"Habit '{name}' logged for today.")

def update_streak(habits, name):
    logs = habits[name]["logs"]
    current_streak = 0
    best_streak = habits[name]["best_streak"]
    
    for i in range(len(logs)):
        if i == 0 or (datetime.strptime(logs[i], '%Y-%m-%d') - datetime.strptime(logs[i - 1], '%Y-%m-%d')).days == 1:
            current_streak += 1
        else:
            current_streak = 1

        if current_streak > best_streak:
            best_streak = current_streak

    habits[name]["streak"] = current_streak
    habits[name]["best_streak"] = best_streak

def analyze_habits(habits):
    for name, data in habits.items():
        print(f"Habit: {name}")
        print(f"  Total Logs: {len(data['logs'])}")
        print(f"  Current Streak: {data['streak']}")
        print(f"  Best Streak: {data['best_streak']}")

def main():
    habits = load_data()

    while True:
        print("\nHabit Tracker Menu:")
        print("1. Add Habit")
        print("2. Log Habit")
        print("3. Analyze Habits")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter habit name: ")
            add_habit(habits, name)
        elif choice == '2':
            name = input("Enter habit name: ")
            log_habit(habits, name)
        elif choice == '3':
            analyze_habits(habits)
        elif choice == '4':
            save_data(habits)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()