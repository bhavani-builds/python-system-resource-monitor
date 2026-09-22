import psutil
import time
from datetime import datetime


def get_disk_path():
    if psutil.WINDOWS:
        return "C:\\"

    return "/"


def collect_resource_data():
    cpu = psutil.cpu_percent(interval=1)

    memory = psutil.virtual_memory().percent

    disk = psutil.disk_usage(
        get_disk_path()
    ).percent

    return {
        "time": datetime.now(),
        "cpu": cpu,
        "memory": memory,
        "disk": disk
    }


def display_record(record):
    print(
        f"{record['time'].strftime('%H:%M:%S')} | "
        f"CPU: {record['cpu']:6.2f}% | "
        f"RAM: {record['memory']:6.2f}% | "
        f"Disk: {record['disk']:6.2f}%"
    )


def monitor_system(samples=5, interval=2):
    history = []

    print("\n===== SYSTEM MONITORING HISTORY =====")
    print(
        "Time     | CPU       | RAM       | Disk"
    )
    print("-" * 50)

    for _ in range(samples):
        record = collect_resource_data()

        history.append(record)

        display_record(record)

        time.sleep(interval)

    return history


def display_summary(history):
    if not history:
        return

    average_cpu = (
        sum(record["cpu"] for record in history)
        / len(history)
    )

    average_memory = (
        sum(record["memory"] for record in history)
        / len(history)
    )

    average_disk = (
        sum(record["disk"] for record in history)
        / len(history)
    )

    print("\n===== MONITORING SUMMARY =====")

    print(
        f"Average CPU Usage    : "
        f"{average_cpu:.2f}%"
    )

    print(
        f"Average Memory Usage : "
        f"{average_memory:.2f}%"
    )

    print(
        f"Average Disk Usage   : "
        f"{average_disk:.2f}%"
    )


def main():
    print("===== PYTHON SYSTEM MONITOR =====")

    history = monitor_system(
        samples=5,
        interval=2
    )

    display_summary(history)


if __name__ == "__main__":
    main()
