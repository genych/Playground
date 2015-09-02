import time
import requests
import re
from bs4 import BeautifulSoup as bs

start_time = time.clock()
init_url = 'https://www.youtube.com/watch?v=iFNbW6GSbl8'
youtube, watch, suffix = init_url.partition('/watch')
url = watch + suffix
counter = 0
visited = set()
stack = [url]

while stack:
    url = stack.pop()
    page = requests.get(youtube+url).content
    soup = bs(page)
    links = soup.find_all('a', {'class':
                                "content-link spf-link yt-uix-sessionlink"})
    recommended = {item.text.split('\n')[1].lower():
                {'link': item.get('href'),
                 'author': re.findall('autors: (.*?)\W', item.text)[0]}
                for item in links}
    for title in recommended:
        if 'sheldon' in title:
            print 'gotcha!', title
            print 'your link:', youtube + recommended[title]['link']
            exit(0)
        if recommended[title]['author'] not in visited:
            stack.append(recommended[title]['link'])
            visited.add(recommended[title]['author'])
    cur_time = time.clock() - start_time
    print '{} [{}]: {}'.format(counter, cur_time,
                    soup.title.text.encode('utf-8', errors='ignore'))
    counter += 1
    time.sleep(1)

    if not counter % 10:
        # print 'stack size:', len(stack)
        stack = stack[-len(stack)//4:]
