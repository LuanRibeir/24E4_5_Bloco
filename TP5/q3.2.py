import socket
import ssl

HOST = '127.0.0.1'
PORTA = 8443

contexto_ssl_cliente = ssl.create_default_context()
contexto_ssl_cliente.check_hostname = False
contexto_ssl_cliente.verify_mode = ssl.CERT_NONE

cliente_socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente_tls_socket = contexto_ssl_cliente.wrap_socket(cliente_socket_tcp, server_hostname=HOST)

cliente_tls_socket.connect((HOST, PORTA))
print("Cliente: conexão estabelecida")

metodo_envio_original_cliente = cliente_tls_socket.send
metodo_receber_original_cliente = cliente_tls_socket.recv

def enviar_interceptado_cliente(dados, *args, **kwargs):
    print("Interceptado (envio):", dados)
    return metodo_envio_original_cliente(dados, *args, **kwargs)

def receber_interceptado_cliente(buffer_size, *args, **kwargs):
    dados = metodo_receber_original_cliente(buffer_size, *args, **kwargs)
    print("Interceptado (recebido):", dados)
    return dados

cliente_tls_socket.send = enviar_interceptado_cliente
cliente_tls_socket.recv = receber_interceptado_cliente

mensagem_para_envio = "Mensagem segura com logging de pacotes"
cliente_tls_socket.send(mensagem_para_envio.encode('utf-8'))

dados_recebidos_cliente = cliente_tls_socket.recv(1024)
print("Cliente: recebido:", dados_recebidos_cliente.decode('utf-8'))

cliente_tls_socket.close()

