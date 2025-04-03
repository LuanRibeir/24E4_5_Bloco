import socket
import ssl

def run_tls_client(server_host='127.0.0.1', server_port=8443, message="Olá, servidor TLS!"):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Criar contexto TLS
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    # Estabelecer conexão segura
    ssl_sock = context.wrap_socket(sock, server_hostname=server_host)
    ssl_sock.connect((server_host, server_port))
    print("Cliente: conexão estabelecida")

    # Enviar mensagem ao servidor
    ssl_sock.sendall(message.encode())

    # Receber resposta do servidor
    data = ssl_sock.recv(1024)
    print("Cliente: recebido:", data.decode())

    # Fechar conexão
    ssl_sock.close()

if __name__ == '__main__':
    run_tls_client()

