import requests, json
from BddScraperInterest import BddScraperInterest


if __name__ == '__main__':
    with open("config.json") as file:
        data = json.load(file)
        host = data["host"]
        username = data["username"]
        password = data["password"]
        database = data["database"]

    connexionDb = BddScraperInterest(host, username, password, database)
    if connexionDb.CreateConnexion():
        checkConnexion = True
    else:
        checkConnexion = False

    if checkConnexion:
        "https://www.google.com/search?q=missile+brahmo&tbs=cdr%3A1%2Ccd_min%3A3%2F20%2F2023%2Ccd_max%3A3%2F20%2F2023&tbm=nws"
        for search in connexionDb.SelectSearch():
            print(search[0], search[1], search[2])


