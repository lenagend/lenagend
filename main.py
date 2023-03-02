

import feedparser, datetime

URL = "https://lenagend.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)

markdown_text = """## Hello, there!

I'm Kwangmin Kim

I'm interested in web developing

## Latest Blog Posts

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
