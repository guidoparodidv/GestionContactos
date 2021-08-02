import mysql.connector
from mysql.connector import errorcode
import pymysql


class mysql_scrip:
    def __init__(
        self,
        host="127.0.0.1",
        name="root",
        psw="",
        database="",
        table="",
    ):

        self.host = host
        self.name = name
        self.psw = psw
        self.db = database
        self.table = table
        print("host", self.host)
        print("name", self.name)
        print("psw", self.psw)
        print("db", self.db)
        print("table", self.table)
        # Conexion con base de datos MySQL

        try:
            self.cnx = mysql.connector.connect(
                host=self.host,
                port=3306,
                database=self.db,
                user=self.name,
                password=None,
            )
            self.cursor = self.cnx.cursor()
            print("conectado")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            self.cnx.close()

    def select_id(self, id):
        sql = "SELECT id FROM contacto WHERE id = {}".format(id)
        try:
            self.cursor.execute(sql)
            row = self.cursor.fetchone()
            print("ID:", row[0])
            print("Nombre:", row[1])
            print("Apellido:", row[2])
            print("Email:", row[3])
            print("Telefono:", row[4])
            print("Mas:", row[5])
            self.cnx.close()
        except:
            raise


if __name__ == "__main__":
    mi_base = mysql_scrip(
        host="127.0.0.1", name="root", psw="", database="eloy", table="contactos"
    )
    # mi_base.select_id(1)