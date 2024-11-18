from scr.conexion import CConexion
import re


class Usuarios:
    def __init__(self, nombre='', correo='', contrasena='', confirmar_contrasena =''):
        # Atributos del usuario
        self.nombre = nombre
        self.correo = correo
        self.contrasena = contrasena
        self.confirmar_contrasena = confirmar_contrasena
        # Crear una instancia de CConexion
        self.conexion = CConexion()

    def registrarusuarios(self):
        if not self.correo or not self.nombre or not self.contrasena:
            print("Tienes que ingresar todos los datos")
            return False,"Tienes que ingresar todos los datos"

        # Verificar que el correo contenga "@" y "."
        if "@" not in self.correo or "." not in self.correo.split("@")[-1]:
            print("Correo no válido")
            return False, "Correo no válido"


        # Validar nombre de usuario (3 a 30 caracteres y solo letras, números, guiones bajos y espacios)
        if not (3 <= len(self.nombre) <= 30 and re.match(r'^[a-zA-Z0-9_ ]+$', self.nombre)):
            print("Nombre de usuario no válido. Debe tener entre 3 y 30 caracteres y solo contener letras, números, guiones bajos y espacios.")
            return False, "Nombre de usuario no válido. Debe tener entre 3 y 30 caracteres y solo contener letras, números, guiones bajos y espacios."

        if self.contrasena != self.confirmar_contrasena:
            print("Error  Las contraseñas no coinciden.")
            return False,"Error  Las contraseñas no coinciden."

        if len(self.contrasena) <= 8:
            print("La contraseña debe tener más de 8 caracteres.")
            return False,"La contraseña debe tener más de 8 caracteres."

        if not re.search(r'\d', self.contrasena):
            print("La contraseña debe contener al menos un número.")
            return False,"La contraseña debe contener al menos un número."

        # Obtener la conexión a la base de datos
        conn = self.conexion.ConexionBaseDeDatos()
        if conn is None:
            print("Error al conectar a la base de datos.")
            return

        try:
            # Crear un cursor para ejecutar comandos SQL
            with conn.cursor() as cursor:
                # Verificar que el correo no esté registrado
                sql_verificar = "SELECT correo FROM usuarios WHERE correo = %s;"
                cursor.execute(sql_verificar, (self.correo,))
                resultado = cursor.fetchone()

                if resultado:
                    print("El correo ya está registrado")
                    return False,"El correo ya está registrado"

                # Consulta SQL para insertar un nuevo usuario
                sql = """
                    INSERT INTO usuarios (nombre_completo, correo, contraseña)
                    VALUES (%s, %s, %s);
                """
                valores = (self.nombre, self.correo, self.contrasena)

                # Ejecutar la consulta SQL
                cursor.execute(sql, valores)

                # Confirmar los cambios en la base de datos
                conn.commit()


                print("Usuario registrado exitosamente.")
                return True,"Usuario registrado exitosamente."

        except Exception as e:
            # Imprimir el error en caso de que algo salga mal
            print(f"Error al registrar el usuario: {e}")

        finally:
            # Cerrar la conexión a la base de datos
            conn.close()

    def login(self,correo,contrasena):
        # Obtener la conexión a la base de datos
        conn = self.conexion.ConexionBaseDeDatos()
        if conn is None:
            print("Error al conectar a la base de datos.")
            return

        try:
            # Crear un cursor para ejecutar comandos SQL
            with conn.cursor() as cursor:
                # Consulta SQL para obtener el usuario por correo
                sql = "SELECT id_usuario, nombre_completo, contraseña FROM usuarios WHERE correo = %s;"
                cursor.execute(sql, (correo,))

                # Obtener el resultado de la consulta
                resultado = cursor.fetchone()

                if resultado:
                    id_usuario, nombre, stored_password = resultado

                    # Comparar la contraseña ingresada con la almacenada en la base de datos
                    if contrasena == stored_password:
                        print("Inicio de sesión exitoso.")
                        return True, id_usuario,nombre
                    else:
                        print("Usuario o contraseña incorrecta .")
                        return None, "Usuario o contraseña incorrecta .", False
                else:
                    print("Usuario o contraseña incorrecta .")
                    return None,"Usuario o contraseña incorrecta.", False

        except Exception as e:
            # Imprimir el error en caso de que algo salga mal
            print(f"Error al intentar iniciar sesión: {e}")

        finally:
            # Cerrar la conexión a la base de datos
            conn.close()



