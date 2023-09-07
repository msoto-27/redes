import socket

####CLIENTE####

# Variables
host = '127.0.0.1'
port = 8050

# Creación de un objeto socket (lado cliente)
obj = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM, proto=0)

# Creamos un bucle para retener la conexion
while True:
    # Instanciamos una entrada de datos para que el cliente pueda enviar mensajes
    msg = input("Mensaje: > ")

    # Con el método send, enviamos el mensaje
    # Para finalizar la conexion cliente enviar "exit"
    obj.sendto(msg.encode('utf-8'), (host,port))
    data, addr = obj.recvfrom(4096)
    print("respuesta: {0}".format(data.decode("utf-8")))
    if data.decode("utf-8") == "exit":
        break

# Cerramos la instancia del objeto servidor
obj.close()

input("Presione ENTER para salir")