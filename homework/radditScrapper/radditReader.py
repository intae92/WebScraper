import requests
from flask import Flask, render_template, request
from bs4 import BeautifulSoup
from operator import itemgetter

"""
When you try to scrape reddit make sure to send the 'headers' on your request.
Reddit blocks scrappers so we have to include these headers to make reddit think
that we are a normal computer and not a python script.
How to use: requests.get(url, headers=headers)
"""

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

"""
All subreddits have the same url:
i.e : https://reddit.com/r/javascript
You can add more subreddits to the list, just make sure they exist.
To make a request, use this url:
https://www.reddit.com/r/{subreddit}/top/?t=month
This will give you the top posts in per month.
"""

subreddits = [
    "javascript",
    "reactjs",
    "reactnative",
    "programming",
    "css",
    "golang",
    "flutter",
    "rust",
    "django"
]


app = Flask("DayEleven")

chooseDb = []


@app.route('/')
def home():
    return render_template("raddit_home.html")


@app.route('/read')
def read():
    languageArray = []
    for language in subreddits:
        print(language)
        if(request.args.get(language) == 'on'):
            languageArray.append('r/'+language)
            base_url = f"https://www.reddit.com/r/{language}/top/?t=month"
            webScrapper(base_url, language)
    for d in chooseDb:
        d[0] = int(d[0])
    chooseDb.sort(key=itemgetter(0), reverse=True)

    for db in chooseDb:
        if (db[0] >= 1000):
            db[0] = str(db[0]/1000)+'k'
        else:
            db[0] = str(db[0])

    return render_template("raddit_read.html", chooseDb=chooseDb, languages=' '.join(languageArray))


# base_url = f"https://www.reddit.com/r/{subreddits}/top/?t=month"


def webScrapper(URL, language):
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.text, "html.parser")
    blocks = soup.find_all("div", {"class": "_1oQyIsiPHYt6nx7VOmd1sz"})

    for block in blocks:
        promotion = block.find("span", {"class": "_2oEYZXchPfHwcf9mTMGMg8"})
        if promotion == None:
            votes = block.find(
                "div", {"class": "_1rZYMD_4xY3gRcSS3p8ODO"}).string
            votes = int(''.join(votes.replace('k', '00').split('.')))
            link = None or block.find(
                "a", {"class": "SQnoC3ObvgnGjWt90zD9Z"}).attrs['href']
            title = block.find("h3", {"class": "_eYtD2XCVieq6emjKBH3m"}).string
            chooseDb.append([votes, title, link, language])


# app.run(host="0.0.0.0")
app.run()
