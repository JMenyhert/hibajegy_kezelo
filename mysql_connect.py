import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="Vizsga",
    passwd="vizsga2024",
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE vizsga")

print("Adatbázis létrehozva")