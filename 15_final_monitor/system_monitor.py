import os
import time
from datetime import datetime

import psutil


CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80


def get_disk_path():
    if os.name == "nt":
        return "C:\\"

    return "/"


def get_system_information():
    return {
        "operating_system": os.name,
        "processor": psutil.cpu_count(logical=False),
        "logical_cpus": psutil.cpu_count(logical=True)
    }


def get_resource_usage():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage(get_disk_path())

    return {
        "cpu": cpu,
        "memory": memory.percent,
        "memory_total": memory.total,
        "memory_used": memory.used,
        "disk": disk.percent,
        "disk_total": disk.total,
        "disk_used": disk.used,
        "disk_free": disk.free
    }


def get_top_processes(limit=5):
    processes = []

    for process in psutil.process_iter(
        ["pid", "name", "cpu_percent", "memory_percent"]
    ):
        try:
            information = process.info

            processes.append({
                "pid": information["pid"],
                "name": information["name"] or "Unknown",
                "cpu": information["cpu_percent"] or 0,
                "memory": information["memory_percent"] or 0
            })

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess
        ):
            continue

    processes.sort(
        key=lambda process: process["memory"],
        reverse=True
    )

    return processes[:limit]


def get_alerts(resources):
    alerts = []

    if resources["cpu"] >= CPU_THRESHOLD:
        alerts.append(
            f"High CPU usage: "
            f"{resources['cpu']:.2f}%"
        )

    if resources["memory"] >= MEMORY_THRESHOLD:
        alerts.append(
            f"High memory usage: "
            f"{resources['memory']:.2f}%"
        )

    if resources["disk"] >= DISK_THRESHOLD:
        alerts.append(
            f"High disk usage: "
            f"{resources['disk']:.2f}%"
        )

    return alerts


def get_system_status(alerts):
    if not alerts:
        return "NORMAL"

    if len(alerts) == 1:
        return "WARNING"

    return "CRITICAL"


def bytes_to_gb(value):
    return value / (1024 ** 3)


def display_dashboard(
    resources,
    processes,
    alerts,
    status
):
    current_time = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    print("\n")
    print("=" * 70)
    print("              PYTHON SYSTEM RESOURCE MONITOR")
    print("=" * 70)

    print(f"Time: {current_time}")

    print("\nSYSTEM RESOURCES")
    print("-" * 70)

    print(
        f"CPU Usage       : "
        f"{resources['cpu']:.2f}%"
    )

    print(
        f"Memory Usage    : "
        f"{resources['memory']:.2f}% "
        f"({bytes_to_gb(resources['memory_used']):.2f} / "
        f"{bytes_to_gb(resources['memory_total']):.2f} GB)"
    )

    print(
        f"Disk Usage      : "
        f"{resources['disk']:.2f}% "
        f"({bytes_to_gb(resources['disk_used']):.2f} / "
        f"{bytes_to_gb(resources['disk_total']):.2f} GB)"
    )

    print("\nSYSTEM STATUS")
    print("-" * 70)

    print(f"Status          : {status}")

    if alerts:
        print("\nALERTS")

        for number, alert in enumerate(
            alerts,
            start=1
        ):
            print(
                f"{number}. {alert}"
            )

    print("\nTOP MEMORY-USING PROCESSES")
    print("-" * 70)

    print(
        f"{'PID':<10}"
        f"{'PROCESS':<30}"
        f"{'CPU %':<12}"
        f"{'MEMORY %':<12}"
    )

    for process in processes:
        print(
            f"{process['pid']:<10}"
            f"{process['name'][:28]:<30}"
            f"{process['cpu']:<12.2f}"
            f"{process['memory']:<12.2f}"
        )

    print("=" * 70)


def run_monitor():
    while True:
        try:
            resources = get_resource_usage()

            processes = get_top_processes()

            alerts = get_alerts(resources)

            status = get_system_status(
                alerts
            )

            os.system("cls" if os.name == "nt" else "clear")

            display_dashboard(
                resources,
                processes,
                alerts,
                status
            )

            print(
                "\nRefreshing in 5 seconds..."
            )

            time.sleep(5)

        except KeyboardInterrupt:
            print(
                "\n\nMonitoring stopped."
            )
            break


def main():
    print("=" * 70)
    print("        PYTHON SYSTEM RESOURCE MONITOR")
    print("=" * 70)

    information = get_system_information()

    print(
        f"\nOperating System : "
        f"{information['operating_system']}"
    )

    print(
        f"Physical CPUs    : "
        f"{information['processor']}"
    )

    print(
        f"Logical CPUs     : "
        f"{information['logical_cpus']}"
    )

    input(
        "\nPress Enter to start monitoring..."
    )

    run_monitor()


if __name__ == "__main__":
    main()
