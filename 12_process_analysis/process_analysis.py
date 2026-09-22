import psutil


def get_processes():
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

    return processes


def get_top_cpu_processes(processes, limit=5):
    return sorted(
        processes,
        key=lambda process: process["cpu"],
        reverse=True
    )[:limit]


def get_top_memory_processes(processes, limit=5):
    return sorted(
        processes,
        key=lambda process: process["memory"],
        reverse=True
    )[:limit]


def display_processes(
    processes,
    title
):
    print("\n" + "=" * 75)
    print(title)
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
    print("===== PROCESS RESOURCE ANALYSIS =====")

    processes = get_processes()

    if not processes:
        print("No process information available.")
        return

    top_cpu = get_top_cpu_processes(
        processes
    )

    top_memory = get_top_memory_processes(
        processes
    )

    display_processes(
        top_cpu,
        "TOP CPU-CONSUMING PROCESSES"
    )

    display_processes(
        top_memory,
        "TOP MEMORY-CONSUMING PROCESSES"
    )


if __name__ == "__main__":
    main()
