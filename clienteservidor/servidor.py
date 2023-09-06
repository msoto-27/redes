#!/usr/bin/env python
 
#Se importa el módulo
import socket
import threading
print_lock = threading.Lock() 

#instanciamos un objeto para trabajar con el socket
ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Puerto y servidor que debe escuchar
ser.bind(("127.0.0.1", 8050))

#Aceptamos conexiones entrantes con el metodo listen. Por parámetro las conexiones simutáneas.
ser.listen(5)

# Hilos por cliente
def threadCli(conexion, addr):

    while True :
        data = conexion.recv(1024)
        #respuesta = "Hola! tu me mandaste: "
        upp= data.decode("utf-8").upper()
        
        #respfinal= respuesta+upp
        if data.decode("utf-8") == "exit":
            respuesta="exit"
            conexion.send(str.encode(respuesta))
            break
        else:
            conexion.send(str.encode(upp))
            
    
    conexion.close()


while True:
    #Instanciamos un objeto cli (socket cliente) para recibir datos
    cli, addr = ser.accept()
    
    #abrimos un nuevo hilo para el cliente
    threading._start_new_thread(threadCli,(cli,addr))

    
#Cerramos la instancia del socket cliente y servidor
cli.close()
ser.close()

print("Conexiones cerradas")