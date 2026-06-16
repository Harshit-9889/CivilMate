def save_report(
        report,
        safe_project_name,
        estimate_id
        ):

    filename = (
         f"{safe_project_name}_{estimate_id}.txt"
    )

    with open(
        f"reports/TXT/{filename}",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(report)

    print("Report Saved Successfully!")