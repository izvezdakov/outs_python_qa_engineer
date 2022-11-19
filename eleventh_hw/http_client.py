import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("localhost", 40404))


    def get_data():
        data = ''
        one_byte = s.recv(1)
        while one_byte:
            data += one_byte.decode()
            one_byte = s.recv(1)
        return data


    end_of_stream = '\r\n\r\n'

    # request_str = f'''GET /hello.htm HTTP/1.1\r\n
    #     User-Agent: Mozilla/4.0 (compatible; MSIE5.01; Windows NT)\r\n
    #     Host: www.tutorialspoint.com\r\n
    #     Accept-Language: en-us\r\n
    #     Accept-Encoding: gzip, deflate\r\n
    #     Connection: Keep-Alive\r\n
    # ''' + end_of_stream
    #
    # request_str = f'''POST /cgi-bin/process.cgi HTTP/1.1\r\n
    #     User-Agent: Mozilla/4.0 (compatible; MSIE5.01; Windows NT)\r\n
    #     Host: www.tutorialspoint.com\r\n
    #     Content-Type: application/x-www-form-urlencoded\r\n
    #     Content-Length: length\r\n
    #     Accept-Language: en-us\r\n
    #     Accept-Encoding: gzip, deflate\r\n
    #     Connection: Keep-Alive\r\n
    #     \r\n
    #     licenseID=string&content=string&/paramsXML=string\r\n
    # ''' + end_of_stream

    request_str = f'''GET /?status=404 HTTP/1.1\r\n
        User-Agent: Mozilla/4.0 (compatible; MSIE5.01; Windows NT)\r\n
        Host: www.tutorialspoint.com\r\n
        Accept-Language: en-us\r\n
        Accept-Encoding: gzip, deflate\r\n
        Connection: Keep-Alive\r\n
    ''' + end_of_stream

    s.send(request_str.encode())
    print(get_data())
