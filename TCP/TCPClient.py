from socket import *
# serverName = 'hostname'
serverName = '172.25.96.1'
serverPort = 65432

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName, serverPort))

sentence = input('Input lowercase sentence:')
clientSocket.send(sentence.encode())

modifiedSentence = clientSocket.recv(1024)

print ('From Server:', modifiedSentence.decode())

clientSocket.close()
