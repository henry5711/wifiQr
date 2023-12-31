# wifiQr
manejo de wifi mediante fastapi


paso 1 crear ambiente virtual 
py -m venv env

paso 2 activar ambiente virutal
.\env\Scripts\activate

paso 3 instalar fastapi
pip install fastapi

paso 4 instalar uvicor para ejecutar la api
pip install fastapi uvicorn

paso 5 inicar el servidor
uvicorn main:app --reload --port 5000

paso 6 si quiero que le lleguen dispositivos de la misma red
uvicorn main:app --reload --port 5000 --host 0.0.0.0

paso 7 entrar a la documentacion 
http://127.0.0.1:5000/docs

paso 8 instalar el modulo para conecxion a bdd
Instalar sqlalchemy con pip install sqlalchemy.

Crear la configuración para conectarse a la base de datos: para ello creamos la carpeta config y dentro de ella los archivos __init__.py y database.py
donde,

base_dir es el directorio del archivo database.py
sqlite:/// es la forma en la que se conecta a una base de datos.
engine representa el motor de la base de datos. Con el comando echo=True se muestra por consola lo que estaremos realizando.
Creamos una Session y la enlazamos a la base de datos a través del comando bind
declarative_base servirá para manipular las tablas de la base de datos.



Para conectarte a una base de datos MySQL utilizando FastAPI, necesitarás instalar el controlador de MySQL para Python y configurar la conexión en tu aplicación. Aquí tienes los pasos que puedes seguir:

Instalar el controlador de MySQL para Python. Puedes hacerlo ejecutando el siguiente comando en tu terminal:

Copy code
pip install mysql-connector-python
Importar el módulo mysql.connector en tu archivo FastAPI:

python
Copy code
import mysql.connector
Configurar la conexión a la base de datos MySQL. Puedes hacerlo creando una función que establezca la conexión y devuelva el objeto de conexión. Por ejemplo:

python
Copy code
def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",   # Cambia esto por la dirección de tu servidor MySQL si es diferente
        user="tu_usuario",
        password="tu_contraseña",
        database="nombre_de_tu_base_de_datos"
    )
    return connection
Asegúrate de reemplazar "tu_usuario", "tu_contraseña" y "nombre_de_tu_base_de_datos" con los valores correctos para tu configuración.

Utiliza la función get_db_connection() en tus rutas de FastAPI para obtener una conexión a la base de datos. Por ejemplo:

python
Copy code
from fastapi import FastAPI, Depends
from mysql.connector import connection

app = FastAPI()

@app.get("/usuarios")
async def obtener_usuarios(connection: connection.MySQLConnection = Depends(get_db_connection)):
    # Aquí puedes ejecutar consultas a la base de datos utilizando la conexión
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    return {"usuarios": usuarios}
En este ejemplo, la ruta /usuarios obtiene una conexión a la base de datos utilizando Depends(get_db_connection). Luego, ejecuta una consulta para obtener todos los usuarios de la tabla "usuarios" y devuelve los resultados como respuesta.

Recuerda adaptar la configuración de conexión y las consultas a tu estructura de base de datos específica. Además, ten en cuenta las mejores prácticas de seguridad, como almacenar información de conexión sensible en variables de entorno en lugar de codificarla directamente en el código.

¡Con estos pasos deberías poder conectarte a una base de datos MySQL utilizando FastAPI!


# para instalar requiremets
## pip install -r requirements.txt