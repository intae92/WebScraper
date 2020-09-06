import requests
from bs4 import BeautifulSoup

URL = 'https://www.stackoverflow.com'


def extract_max_pages(job_to_find="vue"):
    JOB_URL = f'{URL}/jobs?r=true&q={job_to_find}'
    print(f'Getting max pages in {JOB_URL}')
    result = requests.get(JOB_URL)
    soup = BeautifulSoup(result.text, 'html.parser')

    try:
        pagination = soup.find("div", attrs={"class": "s-pagination"})
        pages = pagination.find_all('a')
        spans = []

        print(pages)
        for page in pages[:-1]:
            span = page.find('span')
            print(span)
            spans.append(int(span.get_text()))
        max_page = spans[-1]
        print(max_page)
        return max_page
    except:
        return 1


def extract_jobs(max_pages, job_to_find="vue"):
    jobs = []
    JOB_URL = f'{URL}/jobs?r=true&q={job_to_find}'
    print(f'Now scraping {max_pages} stackoverflow job page...')
    try:
        for n in range(max_pages):
            print(f'Page {n+1} scraping...')
            req = requests.get(f'{JOB_URL}&pg={n}')
            soup = BeautifulSoup(req.text, 'html.parser')
            div_jobs = soup.find_all("div", {"class": "js-result"})

            for div in div_jobs:
                title = div.find('a', {'class': 's-link'})['title']
                job_link = div.find('a', {'class': 's-link'})['href']
                company = div.find(
                    'h3', {'class': 'fs-body1'}).find_all('span')[0].get_text().strip()
                location = div.find(
                    'h3', {'class': 'fs-body1'}).find_all('span')[1].get_text().strip()

                job_link = f'{URL}{job_link}'

                jobs.append({"title": title, "company": company,
                             "location": location, "apply_url": job_link})
        print('Scraping done')
        return jobs
    except:
        return []


def get_jobs(job_to_find="vue"):
    max_page = extract_max_pages(job_to_find)
    jobs = extract_jobs(max_page, job_to_find)
    count = 0
    for i in jobs:
        count += 1
        print(f'----{count}-----{i}')
    print(len(jobs))
    return jobs


get_jobs(job_to_find="vue")
