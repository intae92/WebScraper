import requests
from flask import Flask, render_template, request

base_url = "http://hn.algolia.com/api/v1"

# This URL gets the newest stories.
new = f"{base_url}/search_by_date?tags=story"

# This URL gets the most popular stories
popular = f"{base_url}/search?tags=story"


# This function makes the URL to get the detail of a storie by id.
# Heres the documentation: https://hn.algolia.com/api
def make_detail_url(id):
    return f"{base_url}/items/{id}"


db = {}
app = Flask("DayNine")

# 24339034
# @app.route('/24339034')


@app.route('/<id>')
def detailPage(id):
    detail_url = make_detail_url(id)
    target_detail = requests.get(detail_url).json()
    # print(target_detail)
    header = {
        'title': target_detail['title'],
        'points': target_detail['points'],
        'author': target_detail['author'],
        'url': target_detail['url']
    }
    children = target_detail['children']
    return render_template('detail_news.html', header=header, children=children)


@app.route('/')
def home():
    isPopularPage = True
    order = request.args.get("order_by")
    order = order or 'popular'
    if order == 'new':
        isPopularPage = False
    return render_template('index_news.html', stories=db[order], isPopularPage=isPopularPage)


def webScrapper():
    popular_news = []
    new_news = []
    target_popular = requests.get(popular).json()['hits']
    target_new = requests.get(new).json()['hits']
    for t in target_popular:
        news = {
            'objectID': t['objectID'],
            'title': t['title'],
            'url': t['url'],
            'points': t['points'],
            'author': t['author'],
            'num_comments': t['num_comments']
        }
        popular_news.append(news)

    for t in target_new:
        news = {
            'objectID': t['objectID'],
            'title': t['title'],
            'url': t['url'],
            'points': t['points'],
            'author': t['author'],
            'num_comments': t['num_comments']
        }
        new_news.append(news)

    db['popular'] = popular_news
    db['new'] = new_news


webScrapper()
# app.run(host="0.0.0.0")
app.run()

#  'objectID', 'title', 'url', 'points', (By:)'author', 'num_comments'

# title=news['title'],
#                            url=news['url'],
#                            points=news['points'],
#                            author=news['author'],
#                            num_comments=news['num_comments']
# requests.get(url).json() 이랑 {% if %} ~ {% endif %}
# fake db , new, popular빠르게 보이게 하기 위해
# 기본 페이지 / => popular
# comment갈수 있는 링크 detail

# 댓글 작성자 없으면 [delete]


# flask.render_template(template_name_or_list, ** context)

# python_study/
# ├── templates/
# ├── main.py
# └── homework/
#   ├── templates/
#   └── todayWork.py
