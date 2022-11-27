import re
import socket
import datetime
from http.client import responses

end_of_stream = '\r\n\r\n'


def parse_client_request(request: str):
    status_code = None
    status_str = None
    req_lines = request.split('\n')
    req_expr = '(?P<method>\w+) (?P<url>.+) '
    parse_string = re.search(req_expr, req_lines[0])
    method = parse_string.groupdict()['method'].upper()
    if method == 'GET':
        url = parse_string.groupdict()['url']
        if url.startswith('/?status='):
            status_code = int(url[9:])
    if status_code:
        status_str = responses[status_code]
    return method, status_code, status_str, req_lines[1:]


def handle_client(connection):
    client_data = ''
    with connection:
        while connection:
            data = connection.recv(1024)
            print("Received:", data)
            if not data:
               break
            client_data += data.decode()
            if end_of_stream in client_data:
                break

        method, status_code, status_str, headers = parse_client_request(client_data)
        if status_code is None:
            status_code = 200
            status_str = 'OK'

        serverTimeNow = "%s"%datetime.datetime.now()
        http_response = (
            f"HTTP/1.0 {status_code} {status_str}\r\n"
            f"Server: otushomework\r\n"
            f"Date: {serverTimeNow}\r\n"
            f"Content-Type: text/html; charset=UTF-8\r\n"
            f"Request method: {method}\r\n"
            f"Request headers: {headers}"
            f"\r\n"
        )
        connection.send(http_response.encode()
                + f"\r\n".encode())


with socket.socket() as serverSocket:
    # Bind the tcp socket to an IP and port
    serverSocket.bind(("127.0.0.1", 40404))
    serverSocket.listen()
    (clientConnection, clientAddress) = serverSocket.accept()
    handle_client(clientConnection)
    print(f"Sent request to {clientAddress}")
