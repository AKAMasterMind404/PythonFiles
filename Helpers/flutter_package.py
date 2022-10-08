from bs4 import BeautifulSoup
import requests


def getPackageVersion(package: str):
    try:
        link = f'https://pub.dev/packages/{package}'
        req = requests.get(link)
        soup = BeautifulSoup(req.text, 'html.parser')
        content = soup.find('div', {'class': 'detail-header-content-block'}).find('h1', {'class': 'title'})
        filtered = str(content).split('<h1 class="title">')[1].split('<')

        result = filtered[0]
        return ": ^".join(result.split())
    except:
        return None


if __name__ == '__main__':
    packages = [
        "firebase_core",
        "firebase_auth",
        "google_sign_in",
    ]

    for p in packages:
        res = getPackageVersion(p)
        print(res)
    # inp = input()
    # if inp.lower() == "exit": exit()
