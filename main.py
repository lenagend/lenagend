import feedparser
import datetime

URL = "https://lenagend.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)

markdown_text = """## Hello, there!

김광민. 1992/07/13.

경력 3년 7개월 (2024년 3월 기준)

선호분야 : 스프링을 이용한 웹 애플리케이션의 백엔드.
(리액트도 사용 가능합니다.)

기술스택 : 자바, 자바스크립트, 오라클&mySQl&몽고DB, 리액트 등


## Blog Posts

"""

# 게시물을 날짜별로 정렬
entries = sorted(RSS_FEED['entries'], key=lambda x: datetime.datetime.strptime(x['published'], "%a, %d %b %Y %H:%M:%S %z"), reverse=True)

# 정렬된 게시물을 markdown_text에 추가
for i in entries:
    dt = datetime.datetime.strptime(i['published'], "%a, %d %b %Y %H:%M:%S %z").strftime("%b %d, %Y")
    markdown_text += f"[{i['title']}]({i['link']}) - {dt}<br>\n"
    print(i['link'], i['title'])

markdown_text += """

## GitHub Stats
![Anurag's GitHub stats](https://github-readme-stats.vercel.app/api?username=lenagend&show_icons=true&theme=solarized-light)
"""

# 결과를 README.md 파일에 쓰기
with open("README.md", "w", encoding="utf-8") as f:
    f.write(markdown_text)
