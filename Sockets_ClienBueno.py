import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host = socket.gethostname()                           
port = 9999
s.connect((host, port))   

while True:
    mensaje = input("> ")
    s.send(mensaje.encode('utf-8'))
    if (mensaje == 'exit' or mensaje == 'quit'):
        break
    #Para recibir mensajes del servidor:
    #msg = s.recv(1024)  
    #msg = msg.decode('utf-8')
    #El servidor debe mandarle mensaje, 
    #si no el cliente se va a quedar en espera y así se va a quedar (por eso comenté las líneas de codigo anterior)


s.close()