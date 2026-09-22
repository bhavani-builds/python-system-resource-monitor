import psutil


def get_disk_usage(path="/"):
    disk = psutil.disk_usage(path)

    return {
        "total": disk.total,
        "used": disk.used,
        "free": disk.free,
        "percentage": disk.percent
    }


def bytes_to_gb(value):
    return value / (1024 ** 3)


def display_disk_usage(disk):
    print("\n" + "=" * 45)
    print("            DISK MONITOR")
    print("=" * 45)

    print(
        f"Total Disk Space : "
        f"{bytes_to_gb(disk['total']):.2f} GB"
    )

    print(
        f"Used Disk Space  : "
        f"{bytes_to_gb(disk['used']):.2f} GB"
    )

    print(
        f"Free Disk Space  : "
        f"{bytes_to_gb(disk['free']):.2f} GB"
    )

    print(
        f"Disk Usage       : "
        f"{disk['percentage']:.2f}%"
    )

    if disk["percentage"] < 60:
        print("Disk Status      : Normal")

    elif disk["percentage"] < 80:
        print("Disk Status      : Moderate")

    else:
        print("Disk Status      : High")

    print("=" * 45)


def main():
    print("===== PYTHON DISK MONITOR =====")

    disk = get_disk_usage()

    display_disk_usage(disk)


if __name__ == "__main__":
    main()
