const fs = require('fs');
const Parser = require('rss-parser');
const parser = new Parser();

const rssFeed = 'https://lenagend.tistory.com/rss';
const readmePath = './README.md';
const startBlock = '<!-- BLOG-POST-LIST:START -->';
const endBlock = '<!-- BLOG-POST-LIST:END -->';

(async () => {
  const feed = await parser.parseURL(rssFeed);
  const posts = feed.items.slice(0, 5).map(item => `- [${item.title}](${item.link})`).join('\n');
  
  const readmeContent = fs.readFileSync(readmePath, 'utf8');
  const updatedContent = readmeContent.replace(
    new RegExp(`${startBlock}[\\s\\S]*${endBlock}`),
    `${startBlock}\n${posts}\n${endBlock}`
  );

  fs.writeFileSync(readmePath, updatedContent);
})();
