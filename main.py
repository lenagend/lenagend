

import feedparser, datetime

URL = "https://lenagend.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)

markdown_text = """## Hello, there!

김광민. 1992/07/13.
경력 2년 9개월 (2023년 4월 기준)
선호분야 : 스프링을 이용한 웹 애플리케이션의 백엔드.
(리액트도 사용 가능합니다.)
기술스택 : 자바, 자바스크립트, 오라클&mySQl&몽고DB, 리액트 등


## Blog Posts

"""  # list of blog posts will be appended here

lst = []

for i in RSS_FEED['entries']:
    dt = datetime.datetime.strptime(i['published'], "%a, %d %b %Y %H:%M:%S %z").strftime("%b %d, %Y")
    markdown_text += f"[{i['title']}]({i['link']}) - {dt}<br>\n"
    print(i['link'], i['title'])

markdown_text += """

## GitHub Stats
![Anurag's GitHub stats](https://github-readme-stats.vercel.app/api?username=lenagend&show_icons=true&theme=solarized-light)
"""

f = open("README.md",mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
