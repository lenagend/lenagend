

import feedparser, datetime

URL = "https://lenagend.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 5
dt = datetime.datetime.strptime(i['published'], "%a, %d %b %Y %H:%M:%S %z").strftime("%b %d, %Y")

markdown_text = """## Hello, there!

I'm Kwangmin Kim

I'm interested in web developing

## Latest Blog Posts

"""  # list of blog posts will be appended here

for idx, feed in enumerate(RSS_FEED['entries']):
    if idx >= MAX_POST:
        break
    else:
        feed_date = feed['published_parsed']
        markdown_text += (str(idx+1) + ". ")
        markdown_text += f"[{feed['title']}]({feed['link']}) - {dt}<br/>\n"
 

markdown_text += """

## GitHub Stats
![Anurag's GitHub stats](https://github-readme-stats.vercel.app/api?username=lenagend&show_icons=true&theme=solarized-light)
"""

f = open("README.md",mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
