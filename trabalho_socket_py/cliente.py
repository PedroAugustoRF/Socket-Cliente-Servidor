import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
porta = 45231

cliente.connect((host, porta))

while True:
    mensagem = input("Você: ")
    cliente.send(mensagem.encode())

    resposta = cliente.recv(1024).decode()
    print("Servidor:", resposta)