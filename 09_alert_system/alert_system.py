CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80


def check_cpu(cpu_usage):
    if cpu_usage >= CPU_THRESHOLD:
        return (
            f"High CPU usage detected: "
            f"{cpu_usage:.2f}%"
        )

    return None


def check_memory(memory_usage):
    if memory_usage >= MEMORY_THRESHOLD:
        return (
            f"High memory usage detected: "
            f"{memory_usage:.2f}%"
        )

    return None


def check_disk(disk_usage):
    if disk_usage >= DISK_THRESHOLD:
        return (
            f"High disk usage detected: "
            f"{disk_usage:.2f}%"
        )

    return None


def generate_alerts(resources):
    alerts = []

    cpu_alert = check_cpu(
        resources["cpu"]
    )

    if cpu_alert:
        alerts.append(cpu_alert)

    memory_alert = check_memory(
        resources["memory"]
    )

    if memory_alert:
        alerts.append(memory_alert)

    disk_alert = check_disk(
        resources["disk"]
    )

    if disk_alert:
        alerts.append(disk_alert)

    return alerts


def display_alerts(alerts):
    print("\n" + "=" * 55)
    print("                  ALERT SYSTEM")
    print("=" * 55)

    if not alerts:
        print("\nSTATUS: NORMAL")
        print("No resource threshold violations detected.")

    else:
        print("\nSTATUS: WARNING")

        print("\nAlerts:")

        for number, alert in enumerate(
            alerts,
            start=1
        ):
            print(f"{number}. {alert}")

    print("=" * 55)


def main():
    print("===== SYSTEM RESOURCE ALERT SYSTEM =====")

    resources = {
        "cpu": 85.4,
        "memory": 72.6,
        "disk": 91.2
    }

    alerts = generate_alerts(
        resources
    )

    display_alerts(alerts)


if __name__ == "__main__":
    main()
