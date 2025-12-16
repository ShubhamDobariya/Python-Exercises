from datetime import datetime


def activityLog(activity):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("./Problem14.txt", "a") as f:
        f.write(f"[{timestamp}] {activity}\n")

    print("Activity logged successfully.")


if __name__ == "__main__":
    activity = input("Enter Your Activity : ")

    activityLog(activity)
