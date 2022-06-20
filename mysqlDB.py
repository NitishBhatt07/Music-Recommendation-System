
import mysql.connector

def connectToDB():
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="music_recommendation"
    )
    mycursor = mydb.cursor()
    return mydb,mycursor