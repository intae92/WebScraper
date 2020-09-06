import requests
from flask import Flask, render_template, request, redirect
from bs4 import BeautifulSoup


position = "vue"


def extract_jobs(url):
    jobs = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    jobsSection = soup.find("section", {"id": "category-2"})
    jobsBlock = jobsSection.find("ul")
    jobList = jobsBlock.find_all('li')
    for li in jobList:
        liLen = li.find_all('a')
        try:
            title = li.find("span", {"class": "title"}).get_text()
            company = li.find("span", {"class": "company"}).string
            location = li.find("span", {"class": "region"}).string
            try:
                date = li.find("span", {"class": "date"}).string
            except:
                date = "today"
            if len(liLen) > 1:
                jobBlock = li.find_all('a')[1]
            else:
                jobBlock = li.find_all('a')[0]

            apply_link = jobBlock.attrs['href']
        except:
            pass
        # print(date)
        jobs.append(
            {
                'title': title,
                'apply_link': f"https://weworkremotely.com{apply_link}",
                'company': company,
                'location': location,
                'date': date,
                'site': 'weworkremotely'
            }
        )
    # print(jobs)
    return jobs


def get_jobs(position):
    URL = f"https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term={position}"
    jobs = extract_jobs(URL)
    # print(len(jobs))
    # jobs = extract_jobs(URL)
    # print(len(jobs))
    return jobs


# get_jobs(position)
