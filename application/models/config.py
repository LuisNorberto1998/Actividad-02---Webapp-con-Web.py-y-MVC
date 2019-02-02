import web
'''
Parametros de configuracion para conectarse a una base de datos
MySQL o MariaDB
'''

db = web.database(
    dbn='mysql',  # Motor de BD
    host='localhost', #Ruta del Servidor
    db='ria_iniciales', #Nombre de la BD
    user='ria', #Usuario de la BD
    pw='ria.2019', #Contrasena del usuario
    port=3307 #Puerto de mariadb
    )

