import mysql.connector
class BddScraperInterest:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.mydb = ""

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


    def SelectSearch(self):
        cursor = self.mydb.cursor()
        cursor.execute("SELECT * FROM search")
        return cursor.fetchall()