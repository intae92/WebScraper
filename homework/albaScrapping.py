import os
import csv
import requests
import re
from bs4 import BeautifulSoup
import csv

os.system("clear")
alba_url = "http://www.alba.co.kr"


def tartgetJobs(job):
    place = re.sub('\xa0', ' ', job.find(
        "td", {"class": "local"}).get_text())
    title = job.find("td", {"class": "title"}).find(
        "span", {"class": "company"}).get_text()
    time = job.find("td", {"class": "data"}).get_text()
    pay = job.find("td", {"class": "pay"}).get_text()
    date = job.find("td", {"class": "regDate"}).get_text()
    jobs = {
        "place": place,
        "title": title,
        "time": time,
        "pay": pay,
        "date": date
    }
    return jobs


def targetWebScrap(link, company):
    print(company)
    targetWeb = requests.get(link)
    soup = BeautifulSoup(targetWeb.text, "html.parser")
    josbsList = soup.find("div", {"id": "NormalInfo"})
    tbody = josbsList.find("tbody")

    file = open(f"homework/jobs/{company}.csv", mode="w", encoding="UTF-8")
    writer = csv.writer(file)
    writer.writerow(["place", "title", "time", "pay", "date"])

    try:
        for jobsDetailList in tbody.find_all("tr", {"class": ""}):
            job = tartgetJobs(jobsDetailList)
            writer.writerow([job["place"], job["title"],
                             job["time"], job["pay"], job["date"]])

    except:
        print(f"❌ 일이 없음 {company} {link}")


def webScrap():
    targetWeb = requests.get(alba_url)
    soup = BeautifulSoup(targetWeb.text, "html.parser")
    brandBoard = soup.find("div", {"id": "MainSuperBrand"})
    goodsBoxList = brandBoard.find("ul", {"class": "goodsBox"})
    links = goodsBoxList.find_all("a", {"class": "goodsBox-info"})

    for link in links:
        company = link.find("span", {"class": "company"}).get_text()
        targetWebScrap(link.attrs["href"], company)


webScrap()

# place,title,time,pat,date
# 인천 미추홀,노랑통닭 인천 주안점,16:00~02:30,"월급2,300,000", 22분전

# id DetailAreaInfo
# class goodsList detailViewList curation

# local first
# title
# data
# pay
# regDate last

# NormalInfo
# goodsList goodsJob
