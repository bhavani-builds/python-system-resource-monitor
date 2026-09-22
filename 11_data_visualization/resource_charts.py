import matplotlib.pyplot as plt


def plot_resource_usage(history):
    if not history:
        print("No monitoring data available.")
        return

    times = [
        record["time"].strftime("%H:%M:%S")
        for record in history
    ]

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

    # CPU Chart
    plt.figure(figsize=(10, 5))

    plt.plot(
        times,
        cpu_values,
        marker="o"
    )

    plt.title("CPU Usage History")
    plt.xlabel("Time")
    plt.ylabel("CPU Usage (%)")
    plt.xticks(rotation=30)

    plt.tight_layout()

    plt.savefig("cpu_usage.png")

    plt.show()

    # Memory Chart
    plt.figure(figsize=(10, 5))

    plt.plot(
        times,
        memory_values,
        marker="o"
    )

    plt.title("Memory Usage History")
    plt.xlabel("Time")
    plt.ylabel("Memory Usage (%)")
    plt.xticks(rotation=30)

    plt.tight_layout()

    plt.savefig("memory_usage.png")

    plt.show()

    # Disk Chart
    plt.figure(figsize=(10, 5))

    plt.plot(
        times,
        disk_values,
        marker="o"
    )

    plt.title("Disk Usage History")
    plt.xlabel("Time")
    plt.ylabel("Disk Usage (%)")
    plt.xticks(rotation=30)

    plt.tight_layout()

    plt.savefig("disk_usage.png")

    plt.show()


def main():
    from datetime import datetime

    sample_history = [
        {
            "time": datetime(2026, 9, 22, 21, 30, 1),
            "cpu": 35.2,
            "memory": 61.4,
            "disk": 67.8
        },
        {
            "time": datetime(2026, 9, 22, 21, 30, 4),
            "cpu": 42.5,
            "memory": 62.1,
            "disk": 67.8
        },
        {
            "time": datetime(2026, 9, 22, 21, 30, 7),
            "cpu": 28.7,
            "memory": 60.9,
            "disk": 67.8
        },
        {
            "time": datetime(2026, 9, 22, 21, 30, 10),
            "cpu": 51.3,
            "memory": 63.2,
            "disk": 67.8
        }
    ]

    plot_resource_usage(
        sample_history
    )


if __name__ == "__main__":
    main()
