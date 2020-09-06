from homework.Practice.indeed import get_jobs as get_indeed_jobs
from homework.Practice.so import get_jobs as get_so_jobs
# from save import save_to_file
from homework.Practice.exporter import save_to_file
from flask import Flask, render_template, request, redirect, send_file

app = Flask("SuperScrapper")

db = {}


@app.route("/")
def home():
    return render_template("practice_home.html")


@app.route("/practice_report")
def report():
    word = request.args.get('word')
    if word:
        word = word.lower()
        existingjobs = db.get(word)
        if existingjobs:
            jobs = existingjobs
        else:
            jobs = get_so_jobs(word)
            db[word] = jobs
    else:
        return redirect("/")
    return render_template("practice_report.html", searchingBy=word, resultsNumber=len(jobs), jobs=jobs)


@app.route("/practice-export")
def export():
    try:
        word = request.args.get("word")
        if not word:
            raise Exception()
        word = word.lower()
        jobs = db.get(word)
        if not jobs:
            raise Exception()
        save_to_file(jobs)
        return send_file("homework/Practice/testJobs1.csv")
    except:
        return redirect("/")


app.run()


# indeed_jobs = get_indeed_jobs()
# so_jobs = get_so_jobs()
# jobs = indeed_jobs + so_jobs

# save_to_file(jobs)


# 10:00
