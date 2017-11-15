import mysql.connector
""" Module to connect to a MySQL database """


class Data(object):
        """
        Class to connect to a database and manage data
        """

        def __init__(self, config, configDB={'user': 'PythonBot', 'password': 'B0TPython', 'host': '127.0.0.1', 'database': 'bittrex'}):
                """ Initialize Data object """
                self.market = config["market"]
                self.user = configDB['user']
                self.password = configDB['password']
                self.host = configDB['host']
                self.database = configDB['database']



        def connection(self):
                """ Connect to the database """ 
                self.cnx = mysql.connector.connect(user=self.user, password=self.password,
                                                host=self.host,
                                                database=self.database)

        def loadData(self , stmt=""):
                """ Return data requested by statement @stmt"""
                self.connection()
                if stmt == "":
                        stmt = "SELECT * FROM `{0}` ORDER BY ID".format(self.market)

                cursor = self.cnx.cursor()
                cursor.execute(stmt)
                data = cursor.fetchall()
                cursor.close()
                self.cnx.close()
                return(data)

        def insertData(self, stmt, data=None):
                """ Insert data @data by statement @stmt """
                self.connection()
                cursor = self.cnx.cursor()
                self.cnx.cursor().execute(stmt, data)
                self.cnx.commit()
                cursor.close()
                self.cnx.close()


