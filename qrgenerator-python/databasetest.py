import sqlite3
from sqlite3 import Error
import glob
####    FUNCIONES   ####

def create_conection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    
    return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
    except Error as e:
        print(e)



def main():
    database = r"library.db"

    sql_create_autor_table = """
                             CREATE TABLE IF NOT EXISTS AUTOR(
                                ID_AUTOR INTEGER PRIMARY KEY AUTOINCREMENT,
                                APELLIDO TEXT NOT NULL,
                                NOMBRE TEXT NOT NULL
                             );"""

    sql_create_categoria_table = """
                                 CREATE TABLE IF NOT EXISTS CATEGORIA(
                                    ID_CATEGORIA INTEGER PRIMARY KEY,
                                    NOMBRE TEXT NOT NULL
                                 );"""

    sql_create_qr_table = """
                          CREATE TABLE IF NOT EXISTS QR(
                            ID_QR INTEGER PRIMARY KEY AUTOINCREMENT,
                            IMAGEN BLOB NOT NULL
                          );"""

    sql_create_libro_table = """
                             CREATE TABLE IF NOT EXISTS LIBRO(
                                ID_LIBRO INTEGER PRIMARY KEY,
                                TITULO TEXT NOT NULL,
                                FECHA INTEGER NOT NULL,
                                AID_AUTOR INTEGER NOT NULL,
                                CID_CATEGORIA INTEGER NOT NULL,
                                QID_QR INTEGER NOT NULL,
                                FOREIGN KEY (AID_AUTOR) REFERENCES AUTOR (ID_AUTOR),
                                FOREIGN KEY (CID_CATEGORIA) REFERENCES CATEGORIA (ID_CATEGORIA),
                                FOREIGN KEY (QID_QR) REFERENCES QR (ID_QR)
                             );"""

    conn = create_conection(database)

    if conn is not None:
        create_table(conn, sql_create_autor_table)
        create_table(conn, sql_create_categoria_table)
        create_table(conn, sql_create_qr_table)
        create_table(conn, sql_create_libro_table)

    else:
        print("Error! No se puede crear la conexión a la base de datos")

####    IMÁGENES    ####
"""
folder = 'img'
files = glob.glob(folder + '/*.jpg') 
for 
"""        


main() 