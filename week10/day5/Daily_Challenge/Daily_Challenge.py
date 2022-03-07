import time
import requests


class ResponseTime:
    def __init__(self, url):
        self.url = url

    def check_response_time(self):
        start = time.time()
        requests.get(self.url)
        end = time.time()
        resp_time = end - start
        print(f"{resp_time}s")


print('Lets check websites response time:')
print(f"{'-'*60}\nGOOGLE Response time:")
google = ResponseTime('https://www.google.com')
google.check_response_time()
print(f"{'-'*60}\nYNET Response time:")
ynet = ResponseTime('https://www.ynet.co.il')
ynet.check_response_time()
print(f"{'-'*60}\nIMDB Response time:")
imdb = ResponseTime('https://www.imdb.com')
imdb.check_response_time()
print('\n')
