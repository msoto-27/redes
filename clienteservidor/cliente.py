####CLIENTE####

#Variables
host = '127.0.0.1'
port = 8050
#Se importa el módulo
import socket
 
#Creación de un objeto socket (lado cliente)
obj = socket.socket()
 
#Conexión con el servidor. Parametros: IP (puede ser del tipo 192.168.1.1 o localhost), Puerto
obj.connect((host, port))
print("Conectado al servidor")
 
#Creamos un bucle para retener la conexion
while True:
    #Instanciamos una entrada de datos para que el cliente pueda enviar mensajes
    msg = input("Mensaje: > ")

    #Con el método send, enviamos el mensaje
    #Para finalizar la conexion cliente enviar "exit"
    obj.send(msg.encode('utf-8'))
    respuesta = obj.recv(1024)
    print("respuesta: {0}".format(respuesta.decode("utf-8")))
    if respuesta.decode("utf-8") == "exit":
        break
    

#Cerramos la instancia del objeto servidor
obj.close()

#Imprimimos la palabra Adios para cuando se cierre la conexion
print("Conexión cerrada")