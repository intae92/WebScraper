import csv


def save_to_file(jobs, position):
    file = open(f"jobs/{position}.csv", mode="w", encoding="UTF-8")
    writer = csv.writer(file)
    writer.writerow(["title", "link", "company", "location", "site"])
    for job in jobs:
        writer.writerow(list(job.values()))
    return
