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

def insert_autor(conn):
    try:
        c = conn.cursor()
        sql = """INSERT INTO AUTOR (APELLIDO, NOMBRE) VALUES 
                                                        ('Tzu', 'Sun'), 
                                                        ('Balmes', 'Jaime'), 
                                                        ('Spurgeon', 'Charles'), 
                                                        ('Carroll', 'Lewis'),
                                                        ('Rousseau', 'Jacques'), 
                                                        ('de Nebrija', 'Antonio'),
                                                        ('Darwin', 'Charles'),
                                                        ('Eguíluz', 'Javier'), 
                                                        ('Peñalver', 'José'),
                                                        ('Shelley', 'Mary'),
                                                        ('Trostky', 'Leon'),
                                                        ('Lovecraft', 'H. P.'),
                                                        ('Poe', 'Edgar'),
                                                        ('de Cervantes', 'Miguel'),
                                                        ('Alighieri', 'Dante'),
                                                        ('Doyle', 'Arthur Conan'),
                                                        ('Herman', 'Hesse'),
                                                        ('Verne', 'Julio'),
                                                        ('Hitler', 'Adolf'),
                                                        ('Wilde', 'Oscar');"""
        c.execute(sql)
        conn.commit()
    except Error as e:
        print(e)

def insert_categoria(conn):
    try:
        c = conn.cursor()
        sql = """INSERT INTO CATEGORIA (ID_CATEGORIA, NOMBRE) VALUES 
                                                                (0, 'Generalidades'),
                                                                (100, 'Filosofía y Psicología'),
                                                                (200, 'Religión'),
                                                                (300, 'Ciencias Sociales'),
                                                                (400, 'Lenguas'),
                                                                (500, 'Ciencias Naturales y Matemáticas'),
                                                                (600, 'Tecnología'),
                                                                (700, 'Artes'),
                                                                (800, 'Literatura y retórica'),
                                                                (900, 'Geografía e Historia');"""
        c.execute(sql)
        conn.commit()
    except Error as e:
        print(e)

def insert_libro(conn):
    try:
        c = conn.cursor()
        sql =  """INSERT INTO LIBRO (ID_LIBRO, TITULO, FECHA, 
                                    AID_AUTOR, CID_CATEGORIA, 
                                    QID_QR) VALUES 
                                            (101, 'El arte de la guerra', 400, 1, 100, 1),
                                            (102, 'El criterio', 1845, 2, 100, 2),
                                            (201, 'El tesoro de David', 2015, 3, 200, 3),
                                            (801, 'Alicia en el país de las Maravillas', 1865, 4, 800, 4),
                                            (301, 'El contrato social', 1762, 5, 300, 5),
                                            (401, 'Gramática castellana', 1492, 6, 400, 6),
                                            (501, 'EL origen de las especies', 1859, 7, 500, 7), 
                                            (601, 'CSS avanzado', 2005, 8, 600, 8),
                                            (701, 'Lenguaje musical II', 2006, 9, 700, 9),
                                            (802, 'Frankestein', 1818, 10, 800, 10),
                                            (901, 'Historia de la revolución rusa', 1930, 11, 900, 11),
                                            (803, 'Dagón', 1917, 12, 800, 12),
                                            (804, 'El gato negro', 1843, 13, 800, 13),
                                            (805, 'Don Quijote de la mancha', 1605, 14, 800, 14),
                                            (602, 'La Divina comedia', 1321, 15, 700, 15),
                                            (806, 'El sabueso de los Baskerville', 1902, 16, 800, 16),
                                            (807, 'El lobo Estepario', 1927, 17, 800, 17),
                                            (808, 'Viaje al centro de la tierra', 1864, 18, 800, 18),
                                            (103, 'Mi lucha', 1925, 19, 100, 19),
                                            (809, 'El fantasma de Canterville', 1887, 20, 800, 20);"""
        c.execute(sql)
        conn.commit()
    except Error as e:
        print(e)

"""
def insert_qr(ID_QR, IMAGEN):
    try:
        conn = sqlite3.connect('library.db')
        c = conn.cursor()
        sql =""" """INSERT INTO QR (ID_QR, IMAGEN) VALUES (?, ?);"""
"""
        picture = pic2blob(IMAGEN)
        data_tuple = (ID_QR, picture)
        c.execute(sql, data_tuple)
        conn.commit()
    except Error as e:
        print(e)"""

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
        
        insert_autor(conn)
        insert_categoria(conn)
        insert_libro(conn)
        
        """insert_qr(1, "img/1.png")
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
        insert_qr(20, "img/20.png")"""

    else:
        print("Error! No se puede crear la conexión a la base de datos")

main() 
