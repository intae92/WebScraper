# webScraper

Job Web Scraper

- [https://repl.it/@intae92/Day-Thirteen-and-Fourteen](https://repl.it/@intae92/Day-Thirteen-and-Fourteen)
- [https://github.com/intae92/WebScraper](https://github.com/intae92/WebScraper)

---

## 목표

- 세개의 사이트에서 크롤링 후 remote job scraper 구현하기
- 스크래퍼, 크롤러의 작동 원리 이해하기
- Requests로 웹페이지 요청하기
- BeautifulSoup로 웹페이지 데이터 추출하기
- csv 파일로 데이터 저장
- flask로 웹페이지 구현하기

- stackoverflow: stackoverflow.com/jobs?r=true&q=python
- weworkremotely: https://weworkremotely.com/remote-jobs/search?term=python
- remoteok.io: https://remoteok.io/reote-dev+python-jobs

---

## 화면

세개의 사이트 클로링 후 데이터 추출 및 웹 사이트 구현
![v1](https://github.com/intae92/WebScraper/blob/master/video/scraper1.gif?raw=true)
![v2](https://github.com/intae92/WebScraper/blob/master/video/scraper2.gif?raw=true)
![v3](https://github.com/intae92/WebScraper/blob/master/video/scraper3.gif?raw=true)

csv 파일로 데이터 저장

![v4](https://github.com/intae92/WebScraper/blob/master/video/scraper4.gif?raw=true)

---

## 구현 과정

Python, flask, html, css

1. Requests로 웹페이지 요청
2. BeautifulSoup로 웹페이지 html parser
3. 세개의 사이트에서 추출한 데이터 csv 파일로 저장
4. flask로 FrontEnd 구현
   - route 지정
     - '/': home.html 기본 화면
     - '/search?position={position}': search.html 세개의 사이트에서 검색한 직무(position)에 대한 크롤링 한 화면
     - '/export?position={{searchingBy}}': csv파일 다운받기

---

## 끝으로...

웹 스크래퍼를 구현하면서 스캐퍼, 크롤러에 대한 이해와 파이썬에 대한 흥미가 생겼으며
추후 Django 및 DB를 연동 하여 자동 웹 스크래퍼 사이트를 만들어 보겠습니다.
또한, 오픈 API를 활용하여 시각화 사이트를 만들어 볼 예정입니다.
