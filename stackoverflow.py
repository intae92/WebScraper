import requests
from flask import Flask, render_template, request, redirect
from bs4 import BeautifulSoup


# URL = f"https://stackoverflow.com/jobs?q=python&sort=i"


def get_last_page(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
    last_page = pages[-2].get_text(strip=True)
    return int(last_page)


def extract_job(html):
    # title = html.find("div", {"class": "-title"}).find("h2").find("a")["title"]
    # print(title)
    # title = html.find("h2").text.strip()
    title = html.find("h2").find("a")["title"]
    company, location = html.find("h3").find_all("span", recursive=False)
    # company, location = html.find("h3", {"class": "fc-black-700"}).find_all("span", recursive=False)
    company = company.get_text(strip=True)
    location = location.get_text(strip=True).strip(
        '-').strip(' \r').strip('\n')
    job_id = html['data-jobid']
    date = html.find("div", {"class": "mt4"}).get_text().strip().split('\n')[0]
    return {'title': title, 'apply_link': f"https://stackoverflow.com/jobs/{job_id}", 'company': company, 'location': location, 'date': date, 'site': 'stackoverflow'}


def extract_jobs(last_page, url):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping SO: Page: {page}")
        result = requests.get(f"{url}&pg={page+1}")
        # print(result.status_code)
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "-job"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs


def get_jobs(position):
    url = f"https://stackoverflow.com/jobs?q={position}&sort=i&r=true"
    last_page = get_last_page(url)
    jobs = extract_jobs(last_page, url)
    return jobs


# get_jobs("python")
