# import socket module
from socket import *
# In order to terminate the program
import sys



def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  
  #Preparing a server socket
  serverSocket.bind(("", port))
  
  #Fill in start
  serverSocket.listen(1)
  #Fill in end

  while True:
    #Establishing the connection
    
    print('Ready to serve...')
    connectionSocket, addr =  serverSocket.accept()#Fill in start -are you accepting connections?     #Fill in end
    
    try:
            message = connectionSocket.recv(1024).decode()
            filename = message.split()[1]

            try:
                # Opening the client requested file
                f = open(filename[1:], "rb")
                outputdata = b"HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n"

                # Reading the file content and add it to the response
                file_content = f.read()
                response = outputdata + file_content

                # Sending the entire response to the client
                connectionSocket.send(response)
                f.close()
                connectionSocket.close()
            except FileNotFoundError:
                # Sends a 404 response if the file is not found
                not_found_response = "HTTP/1.1 404 Not Found\r\n\r\nFile Not Found"
                connectionSocket.send(not_found_response.encode())
                connectionSocket.close()
    except Exception as e:
            print("An error occurred:", str(e))
            connectionSocket.close()

  #Commenting out the below, as its technically not required and some students have moved it erroneously in the While loop. DO NOT DO THAT OR YOURE GONNA HAVE A BAD TIME.
  #serverSocket.close()
  #sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)