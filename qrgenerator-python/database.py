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

def insert_qr(conn):
    try:
        c = conn.cursor()
        sql = """ INSERT INTO QR (LINK) VALUES
                                        ('https://www.elejandria.com/libro/link_descarga_libro/847/1297'),
                                        ('http://www.suneo.mx/literatura/subidas/Jaime%20Balmes%20El%20Criterio.pdf'),
                                        ('https://www.elejandria.com/libro/link_descarga_libro/810/1095'),
                                        ('https://www.elejandria.com/libro/link_descarga_libro/94/120 '),
                                        ('https://www.elejandria.com/libro/link_descarga_libro/449/584'),
                                        ('https://www.elejandria.com/libro/link_descarga_libro/1546/3437'),
                                        ('https://www.elejandria.com/libro/link_descarga_libro/53/35'),
                                        ('https://www.elejandria.com/libro/link_descarga_libro/27/9'),
                                        ('https://www.elejandria.com/libro/link_descarga_libro/158/214'),                                        
                                        ('https://www.elejandria.com/libro/link_descarga_libro/717/916'),
                                        ('https://www.elejandria.com/libro/link_descarga_libro/757/991'),
                                        ('https://www.elejandria.com/libro/link_descarga_libro/507/679'),
                                        ('https://www.elejandria.com/libro/link_descarga_libro/58/46'),
                                        ('https://www.elejandria.com/libro/link_descarga_libro/77/92'),
                                        ('https://www.elejandria.com/libro/link_descarga_libro/884/1406'),
                                        ('https://www.elejandria.com/libro/link_descarga_libro/245/1259'),
                                        ('https://www.elejandria.com/libro/link_descarga_libro/72/79'),
                                        ('https://www.elejandria.com/libro/link_descarga_libro/240/320'),
                                        ('https://www.elejandria.com/libro/link_descarga_libro/76/89'),
                                        ('https://www.elejandria.com/libro/link_descarga_libro/123/156');"""

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
                            LINK TEXT NOT NULL
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
        insert_qr(conn)
        insert_libro(conn)
        
    else:
        print("Error! No se puede crear la conexión a la base de datos")

main() 