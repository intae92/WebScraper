# try:
#     url = "http://ww.naver.com"
#     response = requests.get(url)
#     print(response.status_code)
# except:
#     print('에러')

# https://blog.mailplug.com/647
# https://xn--3e0bx5euxnjje69i70af08bea817g.xn--3e0b707e/jsp/infoboard/law/domManRule.jsp
# 도메인 검사
# 1. 도메인이름은 영문자[A-Z][a-z], 숫자[0-9], 하이픈[-]으로 구성되어야 한다.
# 2. 도메인이름 길이는 2자 이상 63자 이하이어야 한다.
# 3. 도메인이름은 하이픈 또는 ‘xn--'로 시작하거나 하이픈으로 끝나지 않아야 한다

import requests
import os


def domainCheck(domain):
    if '.' not in domain:
        print(f"{domain} is not a valid URL")
        return False
    return True


def urlCheck(url):
    if domainCheck(url.split('/')[2]):
        try:
            response = requests.get(url)
            code_number = response.status_code
            if code_number >= 200 and code_number < 300:
                print(f"✅ {url} is up!")
            else:
                print(f"❌ {url} is down!")
        except:
            print(f"❌ {url} is down!")
    return


def askReset():
    responseYesNo = input("Do you want to start over? (y/n?)")
    if responseYesNo == 'y':
        os.system('clear')
        return False
    if responseYesNo == 'n':
        print("bye~~~~~~~~~~~😀")
        return True
    print("That's not a valid answer")
    return askReset()
    return


def init():
    while True:
        print("Welcome to IsItDown.py!\nPlease write a URL or URLs you want to check. (separated by comma)")
        for str in input().split(','):
            strLower = str.lower()
            if 'http://' not in strLower:
                urlCheck('http://' + strLower.strip())
            else:
                urlCheck(strLower.strip())

        if askReset():
            break
    return


init()


# text.lstrip()  text.rstrip()  text.strip()

#   google.com, youtube.com,   hTtp://rdadfas.com,  http://NAver.com
# google.com
# youtube.com
# http://rdadfas.com
# http://naver.com
