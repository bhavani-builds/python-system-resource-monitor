import psutil


def get_cpu_usage():
    cpu_usage = psutil.cpu_percent(
        interval=1
    )

    return cpu_usage


def display_cpu_usage(cpu_usage):
    print("\n" + "=" * 40)
    print("          CPU MONITOR")
    print("=" * 40)

    print(
        f"CPU Usage : {cpu_usage:.2f}%"
    )

    if cpu_usage < 50:
        print("CPU Status: Normal")

    elif cpu_usage < 80:
        print("CPU Status: Moderate")

    else:
        print("CPU Status: High")

    print("=" * 40)


def main():
    print("===== PYTHON CPU MONITOR =====")

    cpu_usage = get_cpu_usage()

    display_cpu_usage(cpu_usage)


if __name__ == "__main__":
    main()
