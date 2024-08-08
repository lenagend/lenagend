import feedparser

# RSS 피드 URL
rss_url = 'https://lenagend.tistory.com/rss'

# RSS 피드 파싱
feed = feedparser.parse(rss_url)

# 최신 5개 게시물 정보 가져오기
latest_posts = feed.entries[:5]
latest_posts_html = "<p><strong>Latest Blog Posts:</strong></p>"

for post in latest_posts:
    title = post.title
    link = post.link
    pubdate = post.published
    latest_posts_html += f"<p><a href=\"{link}\">{title}</a><br>Published on: {pubdate}</p>"

# 리드미 파일에 HTML 코드 삽입
with open('README.md', 'r', encoding='utf-8') as file:
    readme_content = file.read()

# 리드미 파일에서 <!--블로그시작-->와 <!--블로그끝--> 사이를 최신 게시물 HTML로 교체
start_tag = '<!--블로그시작-->'
end_tag = '<!--블로그끝-->'

start_index = readme_content.find(start_tag) + len(start_tag)
end_index = readme_content.find(end_tag)

new_readme_content = readme_content[:start_index] + latest_posts_html + readme_content[end_index:]

# 수정된 리드미 파일 저장
with open('README.md', 'w', encoding='utf-8') as file:
    file.write(new_readme_content)

print('README.md has been updated with the latest blog posts.')
