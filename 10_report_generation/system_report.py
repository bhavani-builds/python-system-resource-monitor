from datetime import datetime


def generate_report(
    resources,
    statistics,
    alerts,
    output_file="system_report.txt"
):
    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as file:

        file.write("=" * 60 + "\n")
        file.write("        PYTHON SYSTEM RESOURCE REPORT\n")
        file.write("=" * 60 + "\n\n")

        file.write(
            f"Report Generated: "
            f"{datetime.now()}\n\n"
        )

        # Current Resources
        file.write("CURRENT RESOURCE USAGE\n")
        file.write("-" * 60 + "\n")

        file.write(
            f"CPU Usage    : "
            f"{resources['cpu']:.2f}%\n"
        )

        file.write(
            f"Memory Usage : "
            f"{resources['memory']:.2f}%\n"
        )

        file.write(
            f"Disk Usage   : "
            f"{resources['disk']:.2f}%\n"
        )

        file.write("\n")

        # Statistics
        file.write("RESOURCE STATISTICS\n")
        file.write("-" * 60 + "\n")

        file.write(
            f"Average CPU    : "
            f"{statistics['cpu_average']:.2f}%\n"
        )

        file.write(
            f"Minimum CPU    : "
            f"{statistics['cpu_minimum']:.2f}%\n"
        )

        file.write(
            f"Maximum CPU    : "
            f"{statistics['cpu_maximum']:.2f}%\n"
        )

        file.write("\n")

        file.write(
            f"Average Memory : "
            f"{statistics['memory_average']:.2f}%\n"
        )

        file.write(
            f"Minimum Memory : "
            f"{statistics['memory_minimum']:.2f}%\n"
        )

        file.write(
            f"Maximum Memory : "
            f"{statistics['memory_maximum']:.2f}%\n"
        )

        file.write("\n")

        file.write(
            f"Average Disk   : "
            f"{statistics['disk_average']:.2f}%\n"
        )

        file.write(
            f"Minimum Disk   : "
            f"{statistics['disk_minimum']:.2f}%\n"
        )

        file.write(
            f"Maximum Disk   : "
            f"{statistics['disk_maximum']:.2f}%\n"
        )

        file.write("\n")

        # Alerts
        file.write("SYSTEM ALERTS\n")
        file.write("-" * 60 + "\n")

        if alerts:
            for number, alert in enumerate(
                alerts,
                start=1
            ):
                file.write(
                    f"{number}. {alert}\n"
                )
        else:
            file.write(
                "No resource threshold violations detected.\n"
            )

        file.write("\n")
        file.write("=" * 60 + "\n")
        file.write("End of Report\n")
        file.write("=" * 60 + "\n")

    return output_file


def main():
    print("===== SYSTEM REPORT GENERATOR =====")

    resources = {
        "cpu": 45.5,
        "memory": 62.3,
        "disk": 71.8
    }

    statistics = {
        "cpu_average": 42.6,
        "cpu_minimum": 25.4,
        "cpu_maximum": 67.8,
        "memory_average": 61.9,
        "memory_minimum": 58.2,
        "memory_maximum": 65.4,
        "disk_average": 71.8,
        "disk_minimum": 71.8,
        "disk_maximum": 71.8
    }

    alerts = []

    report = generate_report(
        resources,
        statistics,
        alerts
    )

    print(
        f"\nReport generated successfully: "
        f"{report}"
    )


if __name__ == "__main__":
    main()
