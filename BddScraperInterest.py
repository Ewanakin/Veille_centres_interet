import mysql.connector
from Search import Search
class BddScraperInterest:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.mydb = ""
        self.listObject = []

    # initialisation de la connexion
    def CreateConnexion(self):
        try:
            self.mydb = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
            )
            return True
        except:
            return False


    def SelectAllSearch(self):
        cursor = self.mydb.cursor()
        cursor.execute("SELECT * FROM search")
        allSearch = cursor.fetchall()
        for search in allSearch:
            self.listObject.append(Search(search[0], search[1], search[2]))
        return self.listObject
