import requests
from flask import Flask, render_template, request, redirect
from bs4 import BeautifulSoup

position = 'react'


def extract_jobs(url):
    jobs = []
    reponse = requests.get(url)
    soup = BeautifulSoup(reponse.text, "html.parser")
    jobsTable = soup.find("table", {"id": "jobsboard"})
    jobBlock = jobsTable.find_all("tr", {"class": "job"})
    for jobCompany in jobBlock:
        companyTd = jobCompany.find("td", {"class": "company"})
        title = companyTd.find("h2").string
        apply_link = companyTd.find(
            "a", {"class": "preventLink"}).attrs['href']
        company = companyTd.find("h3", {"itemprop": "name"}).string
        try:
            location = companyTd.find(
                "div", {"class": "location"}).string.strip()
        except:
            location = ""
        date = jobCompany.find("time").string

        jobs.append(
            {
                'title': title,
                'apply_link': f"https://remoteok.io{apply_link}",
                'company': company,
                'location': location,
                'date': date,
                'site': 'remoteok'
            }
        )
    return jobs


def get_jobs(position):
    URL = f"https://remoteok.io/remote-{position}-jobs"
    jobs = extract_jobs(URL)
    return jobs


# get_jobs(position)
