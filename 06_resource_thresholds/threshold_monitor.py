import psutil


CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80


def get_resource_usage():
    cpu_usage = psutil.cpu_percent(interval=1)

    memory_usage = psutil.virtual_memory().percent

    disk_usage = psutil.disk_usage(
        "C:\\" if psutil.WINDOWS else "/"
    ).percent

    return {
        "cpu": cpu_usage,
        "memory": memory_usage,
        "disk": disk_usage
    }


def check_thresholds(resources):
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


def display_status(resources, alerts):
    print("\n" + "=" * 50)
    print("          RESOURCE THRESHOLD MONITOR")
    print("=" * 50)

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

    print("-" * 50)

    if alerts:
        print("STATUS: WARNING")

        print("\nAlerts:")

        for number, alert in enumerate(
            alerts,
            start=1
        ):
            print(f"{number}. {alert}")

    else:
        print("STATUS: NORMAL")
        print("All resources are below the thresholds.")

    print("=" * 50)


def main():
    print("===== PYTHON RESOURCE THRESHOLD MONITOR =====")

    resources = get_resource_usage()

    alerts = check_thresholds(resources)

    display_status(
        resources,
        alerts
    )


if __name__ == "__main__":
    main()
