import mysql.connector
from mysql.connector import Error


class Connection:
    def startConnection(self):
        try:
            conexion = mysql.connector.connect(
                user="root",
                password="sebas2001",
                host="localhost",
                database="python",
                port="3306")
            return conexion
        except Error:
            print("Error de conexión")

    # === Methods Login ===
    def validateUser(self, email, password):
        conexion = self.startConnection()
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT * FROM user WHERE email='" + email + "' AND password='" + password + "'")
        result = False
        resultado = cursor.fetchone()
        if resultado:
            result = True
        elif not resultado:
            result = False
        return resultado, result

    def getDataUserStudent(self, idUser):
        conexion = self.startConnection()
        valores = None
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT * FROM student AS s INNER JOIN user AS u ON (s.idUser = u.idUser) "
            "WHERE u.idUser ='" + idUser + "'")
        resultado = cursor.fetchall()
        for n in resultado:
            valores = n[0] + " " + n[1]
        conexion.close()
        return valores

    def getDataUserTeacher(self, idUser):
        conexion = self.startConnection()
        valores = None
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT * FROM teacher AS t INNER JOIN user AS u ON (t.idUser = u.idUser) "
            "WHERE u.idUser ='" + idUser + "'")
        resultado = cursor.fetchall()
        for n in resultado:
            valores = n[0] + " " + n[1]
        conexion.close()
        return valores

    # === Methods Register ===
    def insertUser(self, email, password, avatar, flagType):
        conexion = self.startConnection()
        cursor = conexion.cursor()
        sql = "INSERT INTO user (email, password, avatar, flagType) VALUES ('{}', '{}', '{}', '{}')" \
            .format(email, password, avatar, flagType)
        cursor.execute(sql)
        conexion.commit()
        print("Ingreso exitoso user")
        conexion.close()

    def getLastIdUser(self):
        conexion = self.startConnection()
        cursor = conexion.cursor()
        cursor.execute("SELECT idUser FROM user ORDER BY idUser DESC")
        resultado = cursor.fetchone()[0]
        conexion.close()
        return resultado

    def insertUser_Student(self, name, lastname, age, degree, idUser):
        conexion = self.startConnection()
        cursor = conexion.cursor()
        sql = "INSERT INTO student (name, lastName, age, degree, idUser) VALUES ('{}', '{}', '{}', '{}', '{}')" \
            .format(name, lastname, age, degree, idUser)
        cursor.execute(sql)
        conexion.commit()
        print("Ingreso exitoso estudiante")
        conexion.close()

    def insertUser_Teacher(self, name, lastName, cellphone, idUser):
        conexion = self.startConnection()
        cursor = conexion.cursor()
        sql = "INSERT INTO teacher (name, lastName, cellphone, idUser) VALUES ('{}', '{}', '{}', '{}')" \
            .format(name, lastName, cellphone, idUser)
        cursor.execute(sql)
        conexion.commit()
        print("Ingreso exitoso teacher")
        conexion.close()

    # ===  ===
    def listUser(self):
        conexion = self.startConnection()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM user")
        resultado = cursor.fetchall()
        for r in resultado:
            print(r[0], r[1], r[2], r[3])
        conexion.close()

    def insertFile(self, urlFile, name, description, idUser):
        conexion = self.startConnection()
        cursor = conexion.cursor()
        sql = "INSERT INTO file (urlFile, name, description, idUser) VALUES ('{}', '{}', '{}', '{}')" \
            .format(urlFile, name, description, idUser)
        cursor.execute(sql)
        conexion.commit()
        print("Guardado exitoso")
        conexion.close()

    def listFile(self):
        conexion = self.startConnection()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM file")
        results = cursor.fetchall()
        quantity = cursor.rowcount
        conexion.close()
        return results, quantity
