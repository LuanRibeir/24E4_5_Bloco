import socket
import ssl

HOST = '127.0.0.1'
PORT = 8443

# Criar um socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)
print(f"Servidor TLS escutando em {HOST}:{PORT}")

# Criar contexto TLS
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile="certificado.pem", keyfile="chave.pem")

while True:
    # Aceitar conexões
    client_socket, addr = server_socket.accept()
    ssl_client_socket = context.wrap_socket(client_socket, server_side=True)

    print(f"Conexão estabelecida com {addr}")

    # Receber dados do cliente
    data = ssl_client_socket.recv(1024).decode()
    print(f"Recebido: {data}")

    # Ecoar a mensagem de volta
    ssl_client_socket.sendall(data.encode())

    # Fechar conexão segura
    ssl_client_socket.close()

