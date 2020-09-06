from flask import request VS import requests

---

이것은 완전히 다른 라이브러리 일뿐만 아니라 완전히 다른 목적입니다.

Flask는 클라이언트가 요청하는 웹 프레임 워크입니다. Flask request개체에는 클라이언트 (예 : 브라우저)가 앱에 보낸 데이터 (예 : URL 매개 변수, POST 데이터 등)가 포함됩니다.

요청 라이브러리는 앱이 다른 사이트 (일반적으로 API)에 HTTP 요청을하기위한 것 입니다. 나가는 요청을 만들고 외부 사이트에서 응답을 반환합니다.

http://flask.pocoo.org/docs/0.11/api/
http://docs.python-requests.org/en/master/
