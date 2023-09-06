#!/usr/bin/env python

# Se importa el módulo
import socket
import threading

print_lock = threading.Lock()

# instanciamos un objeto para trabajar con el socket
ser = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Puerto y servidor que debe escuchar
ser.bind(("127.0.0.1", 8050))


# Hilos por cliente
def threadCli():
    while True:
        data, addr = ser.recvfrom(1024)
        upp = data.decode("utf-8").upper()

        if data.decode("utf-8") == "exit":
            respuesta = "exit"
            ser.sendto(str.encode(respuesta), addr)
            break
        else:
            ser.sendto(str.encode(upp), addr)



while True:

    # abrimos un nuevo hilo para el cliente
    threadCli()

# Cerramos la instancia del socket cliente y servidor
ser.close()

print("Conexiones cerradas")
input()