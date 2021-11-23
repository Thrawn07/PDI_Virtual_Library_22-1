#   Biblioteca virtual - Base de datos
import sqlite3

####    BASE DE DATOS   ####

connection = sqlite3.connect('library.db')                        #Crea la base y la conexión.
cursor = connection.cursor()                                      #Crea una instancia de cursor.