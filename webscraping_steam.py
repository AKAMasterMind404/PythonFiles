from bs4 import BeautifulSoup
import requests
import os

link = 'https://store.steampowered.com/tags/en/Action/'
head = {'cookie': 'sessionid=cd46137aee87759ca68f1347'}
req = requests.get(link)
soup = BeautifulSoup(req.text, 'html.parser')
images_to_download = []
folder_name = "steam_images"


def getPriceAndTags(string, rank):
    parsed = str(string)
    single_game = parsed.split("</a>")[0]
    single_game_blocks = single_game.split("\n")

    tag_block = single_game_blocks[7]
    tags_unparsed = ''.join(tag_block.split('<span class="top_tag">')[1::]).split("</span>, ")
    last_tag = tags_unparsed.pop(-1)
    tags_unparsed.append(last_tag.split("</span></div>")[0])
    tags = tags_unparsed

    game_name = single_game_blocks[5].split("\">")[1][:-6]
    price_block = single_game_blocks[4]
    price_attr = price_block.split("><")[0].split(" ")
    price_paise = price_attr[-1].split("=")[-1][1:-1]
    price = int(price_paise) / 100

    parsed = str(i)
    single_game = parsed.split("</a>")[0]
    single_game_blocks = single_game.split("\n")
    url = single_game_blocks[2].split("src=")[-1][1:-3]
    images_to_download.append(url)

    print(f"Rank: {rank + 1}")
    print(f"Name:{game_name}")
    print(f"Tags:{tags}")
    print(f"Price: Rs. {price} /-")
    print()


def getGameNameAndTag(iterable, rank):
    parsed = str(iterable)
    single_game = parsed.split("</a>")[0]
    single_game_blocks = single_game.split("\n")
    game_name = single_game_blocks[5].split("\">")[1][:-6]

    tag_block = single_game_blocks[7]
    tags_unparsed = ''.join(tag_block.split('<span class="top_tag">')[1::]).split("</span>, ")
    last_tag = tags_unparsed.pop(-1)
    tags_unparsed.append(last_tag.split("</span></div>")[0])
    tags = tags_unparsed

    print(f"Rank: {rank + 1}")
    print(f"Name:{game_name}")
    print(f"Tags:{tags}")
    print()


def downloadImage(url, unique):
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    response = requests.get(url)
    open(f"{folder_name}/img{unique + 1}.png", "wb").write(response.content)


if __name__ == '__main__':
    print("GETTING TRENDING GAMES TAGS AND PRICES...")
    content = soup.find('div', {'id': 'NewReleasesRows'}).find_all('a')
    for j, i in enumerate(content):
        getPriceAndTags(i, j)

    print("-----------")
    print("-----------")
    print("-----------")

    print("GETTING POPULAR GAMES AND THEIR TAGS")
    popular = soup.find('div', {'id': 'ConcurrentUsersRows'}).find_all('a')
    for j, i in enumerate(popular):
        getGameNameAndTag(i, j)

    print("-----------")
    print("-----------")
    print("-----------")

    print("GETTING TOP SELLER GAMES AND THEIR TAGS")
    top_seller = soup.find('div', {'id': 'TopSellersRows'}).find_all('a')
    for j, i in enumerate(top_seller):
        getGameNameAndTag(i, j)
    print("-----------")
    print("-----------")
    print("-----------")

    print("DOWNLOADING IMAGES....")
    for j, i in enumerate(images_to_download):
        downloadImage(i, j)
    print(f"IMAGES DOWNLOADED AT {os.path.abspath('.')}\{folder_name}!")
