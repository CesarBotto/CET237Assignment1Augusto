import socket
# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 55555

# Put the socket into listening mode
print ("socket binded to %s" %(port))

# function for otp generation
import random as r

#declares/initialises string variable where otp will be written.
def otpgen():
    otp=""
#loops whilst 1 is in the range of 4 (so otp will be 5 characters long)
    for i in range(4):
#adds a random number to the otp variable from 1-9
        otp+=str(r.randint(1,9))
    print ("Your One Time Password is ")
    print (otp)
otpgen()
#calls otpgen function