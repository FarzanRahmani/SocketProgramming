from socket import *
serverPort = 65432
serverSocket = socket(AF_INET,SOCK_STREAM) # wellcoming Socket
serverSocket.bind(('',serverPort))
serverSocket.listen(3)
print ('The server is ready to receive')
while True:
    # connectionSocket, clientAddress = serverSocket.accept(5)
    connectionSocket, clientAddress = serverSocket.accept()
    
    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()
