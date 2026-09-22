import psutil
import time
from datetime import datetime


INTERVAL = 3


def get_disk_path():
    if psutil.WINDOWS:
        return "C:\\"

    return "/"


def get_system_resources():
    cpu = psutil.cpu_percent(interval=1)

    memory = psutil.virtual_memory().percent

    disk = psutil.disk_usage(
        get_disk_path()
    ).percent

    return {
        "cpu": cpu,
        "memory": memory,
        "disk": disk
    }


def display_resources(resources):
    current_time = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    print("\n" + "=" * 55)
    print("          CONTINUOUS SYSTEM MONITOR")
    print("=" * 55)

    print(f"Time          : {current_time}")

    print(
        f"CPU Usage     : "
        f"{resources['cpu']:.2f}%"
    )

    print(
        f"Memory Usage  : "
        f"{resources['memory']:.2f}%"
    )

    print(
        f"Disk Usage    : "
        f"{resources['disk']:.2f}%"
    )

    print("=" * 55)


def monitor_system():
    print("===== CONTINUOUS MONITORING =====")
    print("Press Ctrl+C to stop monitoring.")

    try:
        while True:
            resources = get_system_resources()

            display_resources(resources)

            time.sleep(INTERVAL)

    except KeyboardInterrupt:
        print("\nMonitoring stopped.")
        print("Thank you for using the System Monitor.")


def main():
    monitor_system()


if __name__ == "__main__":
    main()
