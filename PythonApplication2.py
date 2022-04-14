import requests
from bs4 import BeautifulSoup


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
}

r = requests.get('https://ani.gamer.com.tw/', headers=headers)
if r.status_code == 200:
    print(f'請求成功：{r.status_code}')

    soup = BeautifulSoup(r.text, 'html.parser')
    newanime_item = soup.select_one('.timeline-ver > .newanime-block')
    cartoon_items = newanime_item.select('.newanime-date-area:not(.premium-block)')

    for cartoon_item in cartoon_items:
        cartoon_name = cartoon_item.select_one('.anime-name > p').text.strip()
        print(cartoon_name)
        cartoon_watch_number = cartoon_item.select_one('.anime-watch-number > p').text.strip()
        print(cartoon_watch_number)
        cartoon_episode = cartoon_item.select_one('.anime-episode').text.strip()
        print(cartoon_episode)
        cartoon_href = cartoon_item.select_one('a.anime-card-block').get('href')
        print('https://ani.gamer.com.tw/'+cartoon_href)

        print('----------')
        if(cartoon_name=="史上最強大魔王轉生為村民 A"):
            break
else:
    print(f'請求失敗：{r.status_code}')
