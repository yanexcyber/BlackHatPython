# A Simple TCP Client

# Importando o módulo de socket

import socket

#Definição das váriaveis de host e port que iremos enviar para onde iremos enviar os dados


target_host, target_port = ('0.0.0.0', 9998)

#Criação de um objeto socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Conecta-se ao client

client.connect((target_host, target_port))

#Envia dados ao host

client.send(b"GET / HTTP/1.1\r\r\nHost: 0.0.0.0\r\n\r\n")

#Recebe dados

response = client.recv(4096)

print(response.decode())
client.close()
