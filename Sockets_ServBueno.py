import socket 

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

host = socket.gethostname()                           
port = 9999                                           

serversocket.bind((host, port))

serversocket.listen(1)  #Numero máximo de conexiones

conn, addr = serversocket.accept()   #regresa la conexión y dirección a donde se hizo la conexión                                      

while True: 
   msg = conn.recv(1024) 
   msg = msg.decode('utf-8')
   if msg  == 'exit':
      break
   print(msg)

conn.close()
serversocket.close()