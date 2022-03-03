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
        print(f"Response time of {self.url} is: {resp_time}")


print('Lets check few websites response time:')
print('\nGOOGLE:')
google = ResponseTime('https://www.google.com')
google.check_response_time()
print('\nYNET:')
ynet = ResponseTime('https://www.ynet.co.il')
ynet.check_response_time()
print('\nIMDB:')
imdb = ResponseTime('https://www.imdb.com')
imdb.check_response_time()
print('\n')
