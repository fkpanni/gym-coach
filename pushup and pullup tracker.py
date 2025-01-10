import os
from datetime import datetime

LOG_FILE = "track_log.txt"

def read_logs():
    if not os.path.exists(LOG_FILE):
        return {}
    with open(LOG_FILE, "r") as file:
        logs = {}
        for line in file:
            exercise, count, date = line.strip().split(",")
            logs[exercise] = {"count": int(count), "date": date}
        return logs
def write_logs(logs):
    with open(LOG_FILE, "w") as file:
        for exercise, data in logs.items():
            file.write(f"{exercise},{data['count']},{data['date']}\n")


def main():
    logs = read_logs()

    #MENU
    print("Enter 1 for push-ups")
    print("Enter 2 for pull-ups")
    choice = input("Select an exercise: ").strip()
    if choice == "1":
        exercise = "pushup"
    elif choice == "2":
        exercise = "pullup"
    else:
        print("Invalid choice. Please enter 1 or 2.")
        return

    #DISPLAY LAST LOG
    if exercise in logs:
        last_count = logs[exercise]["count"]
        last_date = logs[exercise]["date"]
        print(f"Last session for {exercise}s: {last_count} on {last_date}")
    else:
        print(f"No previous logs found for {exercise}s.")

    #LOG CURRENT
    try:
        count = int(input(f"How many {exercise}s did you do today? "))
        logs[exercise] = {"count": count, "date": datetime.now().strftime("%Y-%m-%d")}
        write_logs(logs)
        print(f"Logged {count} {exercise}s for today.")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()