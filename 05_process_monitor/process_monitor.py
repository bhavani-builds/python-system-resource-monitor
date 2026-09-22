import psutil


def get_running_processes(limit=10):
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


def display_processes(processes):
    print("\n" + "=" * 75)
    print("                         RUNNING PROCESSES")
    print("=" * 75)

    print(
        f"{'PID':<10}"
        f"{'PROCESS':<30}"
        f"{'CPU %':<12}"
        f"{'MEMORY %':<12}"
    )

    print("-" * 75)

    for process in processes:
        print(
            f"{process['pid']:<10}"
            f"{process['name'][:28]:<30}"
            f"{process['cpu']:<12.2f}"
            f"{process['memory']:<12.2f}"
        )

    print("=" * 75)


def main():
    print("===== PYTHON PROCESS MONITOR =====")

    processes = get_running_processes()

    display_processes(processes)


if __name__ == "__main__":
    main()
