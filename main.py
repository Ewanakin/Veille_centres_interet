import requests, json
from BddScraperInterest import BddScraperInterest


if __name__ == '__main__':
    print("start")
    with open("config.json") as file:
        data = json.load(file)
        host = data["host"]
        username = data["username"]
        password = data["password"]
        database = data["database"]

    connexionDb = BddScraperInterest(host, username, password, database)
    if connexionDb.CreateConnexion():
        checkConnexion = True
        print("Connexion Ok")
    else:
        checkConnexion = False
        print("Error Connexion")

    if checkConnexion:
        "https://www.google.com/search?q=missile+brahmo&tbs=cdr%3A1%2Ccd_min%3A3%2F20%2F2023%2Ccd_max%3A3%2F20%2F2023&tbm=nws"
        listSearch = connexionDb.SelectAllSearch()
        for search in listSearch:
            print("""
###################
#
# """, search.getId(),"""
# """, search.getSearch(),"""
# """, search.getLastDate(),"""
#
###################
            """)


