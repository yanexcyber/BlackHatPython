# TCP Server

## Criar um servidor TCP em python é simples. E podemos utiliza-los para escrever shells ou craftar um proxy;
## No livro, nos ensinará como codar um standard multi-threaded TCP server 

import socket
import threading


ip = ('0.0.0.0')
port = (9998)

# Criando a função
def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen(5)
    print(f'[*] Ouvindo na porta {ip}:{port}')
                                                #Criação do Loop
    while True:
        client, address = server.accept()
        print(f'[*] Conexão aceita do {address[0]}:{address[1]}')
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Recebido: {request.decode("utf-8")}')
        sock.send(b'ACK')
        
if __name__ == '__main__':
    main()


