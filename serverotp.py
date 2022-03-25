#imports the socket module
import socket

# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 55555

# Put the socket into listening mode
print ("socket binded to %s" %(port))

# Define the IP address and port number
HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 55555  # Port to listen on (non-privileged ports are > 1023)

#imports random module as r
import random as r

# function for otp generation
def otpgen():
    otp="" #declares/initialises string variable where otp will be written.
    #loops whilst i is in the range of 4 (so otp will be 5 characters long)
    for i in range(4):
        #adds a random number to the otp variable from 1-9
        otp+=str(r.randint(1,9))
    print ("Your One Time Password is ")
    #outputs the otp
    print (otp)

#calls otpgen function
otpgen()


#uses a with statement to handle exceptions when trying to connect with socket. s represents the socket.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #binds the host and port to s which was declared previously as 127.0.0.1 and 55555
    s.bind((HOST, PORT))
    #enables the server to listen
    s.listen()
    #accepts an incoming connection request from tcp client
    conn, addr = s.accept()

    with conn:
        #prints the address of client
        print(f"Connected by {addr}")
        #a while loop is created when connected
        while True:
            #puts data received from client into data variable
            data = conn.recv(1024)
            #loop is terminated when no data is received from client
            if not data:
                break
            #this echoes the data sent  by the client
            conn.sendall(data)