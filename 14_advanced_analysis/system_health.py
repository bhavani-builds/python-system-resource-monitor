import psutil


CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80


def get_disk_path():
    if psutil.WINDOWS:
        return "C:\\"

    return "/"


def get_resources():
    return {
        "cpu": psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage(
            get_disk_path()
        ).percent
    }


def get_health_status(resources):
    alerts = []

    if resources["cpu"] >= CPU_THRESHOLD:
        alerts.append(
            "CPU usage is high."
        )

    if resources["memory"] >= MEMORY_THRESHOLD:
        alerts.append(
            "Memory usage is high."
        )

    if resources["disk"] >= DISK_THRESHOLD:
        alerts.append(
            "Disk usage is high."
        )

    if not alerts:
        return "NORMAL", alerts

    if len(alerts) == 1:
        return "WARNING", alerts

    return "CRITICAL", alerts


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


def display_health(
    resources,
    status,
    alerts,
    processes
):
    print("\n" + "=" * 60)
    print("             SYSTEM HEALTH ANALYSIS")
    print("=" * 60)

    print(
        f"CPU Usage    : "
        f"{resources['cpu']:.2f}%"
    )

    print(
        f"Memory Usage : "
        f"{resources['memory']:.2f}%"
    )

    print(
        f"Disk Usage   : "
        f"{resources['disk']:.2f}%"
    )

    print("-" * 60)

    print(
        f"System Status: {status}"
    )

    if alerts:
        print("\nAlerts:")

        for number, alert in enumerate(
            alerts,
            start=1
        ):
            print(
                f"{number}. {alert}"
            )

    else:
        print(
            "\nNo resource problems detected."
        )

    print("\nTop Memory-Using Processes")
    print("-" * 60)

    for process in processes:
        print(
            f"PID: {process['pid']:<8} "
            f"{process['name'][:25]:<25} "
            f"Memory: {process['memory']:.2f}%"
        )

    print("=" * 60)


def main():
    print("===== ADVANCED SYSTEM HEALTH ANALYZER =====")

    resources = get_resources()

    status, alerts = get_health_status(
        resources
    )

    processes = get_top_processes()

    display_health(
        resources,
        status,
        alerts,
        processes
    )


if __name__ == "__main__":
    main()
