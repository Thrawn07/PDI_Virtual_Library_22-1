#   Biblioteca virtual - Base de datos
import sqlite3
from sqlite3 import Error

####    FUNCIONES   ####

def crear_conexion(base):
    try:
        conexion = sqlite3.connect(base)

        return conexion
    except sqlite3.Error as error:
        print('Se ha producido un error al crear la conexion:', error)

def crear_tabla(conexion, definicion):
    cursor = conexion.cursor()
    cursor.executescript(definicion)
    conexion.commit()

def convertir_a_binario(foto):                                      #Convierte las imágenes de QR a datos binarios
    with open(foto, 'rb') as f:
        blob = f.read()
    return blob

def llenar_autor(conexion, autor):
    sql = 'INSERT INTO AUTOR (APELLIDO, NOMBRE) VALUES (?, ?);'
    cursor = conexion.cursor()
    cursor.executescript(sql, autor)
    conexion.commit()

def llenar_categoria(conexion, categoria):
    sql = 'INSERT INTO CATEGORIAS (ID_CATEGORIA, NOMBRE) VALUES (?, ?);'
    cursor = conexion.cursor()
    cursor.execute(sql, categoria)
    conexion.commit()

def llenar_qr(conexion, qr):
    sql = 'INSERT INTO QR (IMAGEN) VALUES (?);'
    foto_binario = convertir_a_binario(qr[-1])
    qr = (foto_binario)
    cursor = conexion.cursor()
    cursor.execute(sql, qr)
    conexion.commit()

def llenar_libro(conexion, libro):
    sql = 'INSERT INTO LIBRO VALUES (?, ?, ?, ?, ? ,?);'
    cursor = conexion.cursor()
    cursor.execute(sql, libro)
    conexion.commit()

####    BASE DE DATOS   ####

conexion = crear_conexion('library.db')  

sql = """
    PRAGMA foreign_keys = ON;

        CREATE TABLE AUTOR(
            ID_AUTOR INTEGER PRIMARY KEY AUTOINCREMENT,
            APELLIDO TEXT NOT NULL,
            NOMBRE TEXT NOT NULL
        );

        CREATE TABLE CATEGORIA(
            ID_CATEGORIA INTEGER PRIMARY KEY,
            NOMBRE TEXT NOT NULL
        );

        CREATE TABLE QR(
            ID_QR INTEGER PRIMARY KEY AUTOINCREMENT,
            IMAGEN BLOB NOT NULL
        );

        CREATE TABLE LIBRO(
            ID_LIBRO INTEGER PRIMARY KEY,
            TITULO TEXT NOT NULL,
            FECHA INTEGER NOT NULL,
            AID_AUTOR INTEGER NOT NULL,
            FOREIGN KEY (AID_AUTOR) REFERENCES AUTOR (ID_AUTOR),
            CID_CATEGORIA INTEGER NOT NULL,
            FOREIGN KEY (CID_CATEGORIA) REFERENCES CATEGORIA (ID_CATEGORIA),
            QID_QR INTEGER NOT NULL,
            FOREIGN KEY (QID_QR) REFERENCES QR (ID_QR)
        );
        """
####    LLAMADAS A FUNCIONES    ####

crear_tabla(conexion, sql)

autor1 = ('Tzu', 'Sun')
llenar_autor(conexion, autor1)
categoria1 = ('100', 'Filosofía y Psicología')
llenar_categoria(conexion, categoria1)
foto1 = 'img/1.jpg'
qr1 = (foto1)
llenar_qr(conexion, qr1)
libro1 = ('101', 'El arte de la guerra', '400', '1', '100', '1')
llenar_libro(conexion, libro1)

if conexion:
    conexion.close()