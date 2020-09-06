import csv


def save_to_file(jobs):
    file = open("homework/Practice/testJobs1.csv", mode="w", encoding="UTF-8")
    writer = csv.writer(file)
    writer.writerow(["title", "company", "location", "link"])
    for job in jobs:
        writer.writerow(list(job.values()))
    return
