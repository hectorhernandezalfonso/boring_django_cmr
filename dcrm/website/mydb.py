import mysql.connector


#Inicializacion BD
dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'usuario',
    passwd = '123',

)

#Cursor

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE crm_app_db")

print('Completado')