import sqlite3
from sqlite3 import Error

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

def pic2blob(file):
    with open(file, 'rb') as f:
        blob = f.read()
    return blob

""""
def insert_autor(conn):
    try:
        c = conn.cursor()
        sql = """ """INSERT INTO AUTOR (APELLIDO, NOMBRE) VALUES 
                                                        (?, ?), #Yazmín
                                                        (?, ?), #Yazmín
                                                        (?, ?), #Yazmín
                                                        (?, ?), #Yazmín
                                                        (?, ?), #Yazmín
                                                        (?, ?), #Yazmín
                                                        (?, ?), #Yazmín
                                                        (?, ?), #Yazmín
                                                        (?, ?), #Yazmín
                                                        (?, ?),#Yazmín
                                                        (?, ?),#Yazmín
                                                        (?, ?),#Yazmín
                                                        (?, ?),#Yazmín
                                                        (?, ?),#Yazmín
                                                        (?, ?), #Yazmín
                                                        (?, ?), #Yazmín
                                                        (?, ?), #Yazmín
                                                        (?, ?), #Yazmín
                                                        (?, ?), #Yazmín
                                                        (?, ?);"""#Yazmín
       """
        c.execute(sql)
        conn.commit()
    except Error as e:
        print(e)"""
"""
def insert_categoria(conn, categoria):
    try:
        c = conn.cursor()
        sql = """ """INSERT INTO CATEGORIAS (ID_CATEGORIA, NOMBRE) VALUES 
                                                                (?, ?), #Yazmín
                                                                (?, ?), #Yazmín
                                                                (?, ?), #Yazmín
                                                                (?, ?), #Yazmín
                                                                (?, ?), #Yazmín
                                                                (?, ?), #Yazmín
                                                                (?, ?), #Yazmín
                                                                (?, ?), #Yazmín
                                                                (?, ?);"""#Yazmín
    """c.execute(sql)
        conn.commit()
    except Error as e:
        print(e)"""
"""
def insert_libro(conn, libro):
    try:
        c = conn.cursor()
        sql = """ """INSERT INTO LIBRO (ID_LIBRO, TITULO, FECHA, 
                                    AID_AUTOR, CID_CATEGORIA, 
                                    QID_CATEGORIA) VALUES 
                                                    (?, ?, ?, ?, ?, ?,) #Yazmín 
                                                    (?, ?, ?, ?, ?, ?,) #Yazmín 
                                                    (?, ?, ?, ?, ?, ?,) #Yazmín 
                                                    (?, ?, ?, ?, ?, ?,) #Yazmín 
                                                    (?, ?, ?, ?, ?, ?,) #Yazmín 
                                                    (?, ?, ?, ?, ?, ?,) #Yazmín 
                                                    (?, ?, ?, ?, ?, ?,) #Yazmín 
                                                    (?, ?, ?, ?, ?, ?,) #Yazmín 
                                                    (?, ?, ?, ?, ?, ?,) #Yazmín
                                                    (?, ?, ?, ?, ?, ?,) #Yazmín 
                                                    (?, ?, ?, ?, ?, ?,) #Yazmín
                                                    (?, ?, ?, ?, ?, ?,) #Yazmín
                                                    (?, ?, ?, ?, ?, ?,) #Yazmín
                                                    (?, ?, ?, ?, ?, ?,) #Yazmín
                                                    (?, ?, ?, ?, ?, ?,) #Yazmín 
                                                    (?, ?, ?, ?, ?, ?,) #Yazmín 
                                                    (?, ?, ?, ?, ?, ?,) #Yazmín 
                                                    (?, ?, ?, ?, ?, ?,) #Yazmín 
                                                    (?, ?, ?, ?, ?, ?,) #Yazmín 
                                                    (?, ?, ?, ?, ?, ?,);""" #Yazmín
  """      c.execute(sql, libro)
        conn.commit()
    except Error as e:
        print(e)
"""

def insert_qr(ID_QR, IMAGEN):
    try:
        conn = sqlite3.connect('library.db')
        c = conn.cursor()
        sql = """INSERT INTO QR (ID_QR, IMAGEN) VALUES (?, ?);"""

        picture = pic2blob(IMAGEN)
        data_tuple = (ID_QR, picture)
        c.execute(sql, data_tuple)
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


    conn = create_conection(database)   #   CREACIÓN DE CONEXIÓN A BASE DE DATOS

    if conn is not None:
        ####    CREACIÓN DE TABLAS  ####
        create_table(conn, sql_create_autor_table)
        create_table(conn, sql_create_categoria_table)
        create_table(conn, sql_create_qr_table)
        create_table(conn, sql_create_libro_table)

        ####    LLENADO DE TABLAS   ####
        """
        insert_autor(conn)
        insert_categoria(conn)
        insert_libro(conn)
        """
        insert_qr(1, "img/1.png")
        insert_qr(2, "img/2.png")
        insert_qr(3, "img/3.png")
        insert_qr(4, "img/4.png")
        insert_qr(5, "img/5.png")
        insert_qr(6, "img/6.png")
        insert_qr(7, "img/7.png")
        insert_qr(8, "img/8.png")
        insert_qr(9, "img/9.png")
        insert_qr(10, "img/10.png")
        insert_qr(11, "img/11.png")
        insert_qr(12, "img/12.png")
        insert_qr(13, "img/14.png")
        insert_qr(15, "img/15.png")
        insert_qr(16, "img/16.png")
        insert_qr(17, "img/17.png")
        insert_qr(18, "img/18.png")
        insert_qr(19, "img/19.png")
        insert_qr(20, "img/20.png")

    else:
        print("Error! No se puede crear la conexión a la base de datos")

main() 