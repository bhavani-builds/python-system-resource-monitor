def calculate_statistics(history):
    if not history:
        return None

    cpu_values = [
        record["cpu"]
        for record in history
    ]

    memory_values = [
        record["memory"]
        for record in history
    ]

    disk_values = [
        record["disk"]
        for record in history
    ]

    statistics = {
        "cpu_average": sum(cpu_values) / len(cpu_values),
        "cpu_minimum": min(cpu_values),
        "cpu_maximum": max(cpu_values),

        "memory_average": (
            sum(memory_values)
            / len(memory_values)
        ),
        "memory_minimum": min(memory_values),
        "memory_maximum": max(memory_values),

        "disk_average": sum(disk_values) / len(disk_values),
        "disk_minimum": min(disk_values),
        "disk_maximum": max(disk_values)
    }

    return statistics


def display_statistics(statistics):
    if not statistics:
        print("No monitoring data available.")
        return

    print("\n" + "=" * 55)
    print("              RESOURCE STATISTICS")
    print("=" * 55)

    print("\nCPU")
    print("-" * 55)

    print(
        f"Average : "
        f"{statistics['cpu_average']:.2f}%"
    )

    print(
        f"Minimum : "
        f"{statistics['cpu_minimum']:.2f}%"
    )

    print(
        f"Maximum : "
        f"{statistics['cpu_maximum']:.2f}%"
    )

    print("\nMEMORY")
    print("-" * 55)

    print(
        f"Average : "
        f"{statistics['memory_average']:.2f}%"
    )

    print(
        f"Minimum : "
        f"{statistics['memory_minimum']:.2f}%"
    )

    print(
        f"Maximum : "
        f"{statistics['memory_maximum']:.2f}%"
    )

    print("\nDISK")
    print("-" * 55)

    print(
        f"Average : "
        f"{statistics['disk_average']:.2f}%"
    )

    print(
        f"Minimum : "
        f"{statistics['disk_minimum']:.2f}%"
    )

    print(
        f"Maximum : "
        f"{statistics['disk_maximum']:.2f}%"
    )

    print("=" * 55)


def main():
    sample_history = [
        {
            "cpu": 35.2,
            "memory": 61.4,
            "disk": 67.8
        },
        {
            "cpu": 42.5,
            "memory": 62.1,
            "disk": 67.8
        },
        {
            "cpu": 28.7,
            "memory": 60.9,
            "disk": 67.8
        },
        {
            "cpu": 51.3,
            "memory": 63.2,
            "disk": 67.8
        },
        {
            "cpu": 31.8,
            "memory": 61.7,
            "disk": 67.8
        }
    ]

    statistics = calculate_statistics(
        sample_history
    )

    display_statistics(statistics)


if __name__ == "__main__":
    main()
