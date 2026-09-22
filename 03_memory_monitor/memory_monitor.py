import psutil


def get_memory_usage():
    memory = psutil.virtual_memory()

    return {
        "total": memory.total,
        "used": memory.used,
        "available": memory.available,
        "percentage": memory.percent
    }


def bytes_to_gb(value):
    return value / (1024 ** 3)


def display_memory_usage(memory):
    print("\n" + "=" * 45)
    print("           MEMORY MONITOR")
    print("=" * 45)

    print(
        f"Total Memory     : "
        f"{bytes_to_gb(memory['total']):.2f} GB"
    )

    print(
        f"Used Memory      : "
        f"{bytes_to_gb(memory['used']):.2f} GB"
    )

    print(
        f"Available Memory : "
        f"{bytes_to_gb(memory['available']):.2f} GB"
    )

    print(
        f"Memory Usage     : "
        f"{memory['percentage']:.2f}%"
    )

    if memory["percentage"] < 60:
        print("Memory Status    : Normal")

    elif memory["percentage"] < 80:
        print("Memory Status    : Moderate")

    else:
        print("Memory Status    : High")

    print("=" * 45)


def main():
    print("===== PYTHON MEMORY MONITOR =====")

    memory = get_memory_usage()

    display_memory_usage(memory)


if __name__ == "__main__":
    main()
