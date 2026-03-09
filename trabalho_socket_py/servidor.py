import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

host = "127.0.0.1"
porta = 45231

servidor.bind((host, porta))
servidor.listen()

print("Servidor aguardando conexão...")
conexao, endereco = servidor.accept()
print("Conectado com", endereco)

while True:
    mensagem = conexao.recv(1024).decode()
    if not mensagem:
        break

    print("Cliente:", mensagem)

    resposta = input("Você: ")
    conexao.send(resposta.encode())

conexao.close()
servidor.close()