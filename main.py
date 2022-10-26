from bs4 import BeautifulSoup
import requests

datum = input("Do jakého data se chceš přenést ? Zadej ve formátu YYYY-MM-DD ")
zdroj = f"https://www.billboard.com/charts/hot-100/{datum}/"

response = requests.get(zdroj)
billboard = response.text
soup = BeautifulSoup(billboard, "html.parser")
list = []
ahoj = soup.find(name ="div",class_="chart-results-list // lrv-u-padding-t-150 lrv-u-padding-t-050@mobile-max")
toto = ahoj.find_all(name="h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")
#print(toto)
for nazev in toto:
    toto = nazev.get_text().strip()
    list.append(toto)


print(list)





# Client ID 736b4c8c2def44ba83e65215ebcc27a9
# Client Secret 0e0cd991c1884348bf5e961ed469299c