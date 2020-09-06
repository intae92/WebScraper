from save_csv import save_to_file
# from exporter import save_to_file

from flask import Flask, render_template, request, redirect, send_file
from remoteok import get_jobs as get_remoteok_jobs
from weworkremotely import get_jobs as get_weworkremotely_jobs
from stackoverflow import get_jobs as get_stackoverflow_jobs

app = Flask("Remote Jobs Scrapper")

db = {}

# jobs = get_remoteok_jobs("vue")
# jobs = get_weworkremotely_jobs("vue")
# jobs = get_stackoverflow_jobs("vue")
# print(jobs)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/search')
def search():
    position = request.args.get('position')
    # word = request.args.get('word')
    if position:
        position = position.lower()
        existingjobs = db.get(position)
        if existingjobs:
            jobs = existingjobs
        else:
            jobs_remoteok = get_remoteok_jobs(position)
            jobs_wework = get_weworkremotely_jobs(position)
            jobs_stack = get_stackoverflow_jobs(position)
            db[position] = jobs_remoteok + jobs_wework + jobs_stack
            # db[position] = jobs_remoteok
            jobs = db[position]
    else:
        return redirect("/")
    return render_template("search.html", searchingBy=position, resultsNumber=len(jobs), jobs=jobs)


@app.route("/export")
def export():
    try:
        position = request.args.get("position")
        if not position:
            raise Exception()
        position = position.lower()
        jobs = db.get(position)
        if not jobs:
            raise Exception()
        save_to_file(jobs, position)
        return send_file(f"jobs/{position}.csv")
    except:
        return redirect("/")


app.run()
