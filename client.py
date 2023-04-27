import socket

# Set up a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define the DNS server's address and port
server_address = ('localhost', 5354)

print('DNS client running...')

while True:
    # Prompt the user to enter a hostname
    hostname = input('Enter a hostname: ')

    # Send the website name to the server
    data_send = sock.sendto(hostname.encode(), ('localhost', 5354))

    # Receive the IP address of the requested website from the server
    ip_address, address = sock.recvfrom(2048)
    cname, address = sock.recvfrom(2048)

    # Decode the received data to get the IP address as a string
    server_rec = ip_address.decode()
    cname_rec = cname.decode()

    # Display the IP address to the user
    print('The IP address of', hostname, 'is', ip_address)
    print(f"The CNAME for the required host is : {cname_rec}")
    print('')

    # Prompt the user to continue or exit
    choice = input('Do you want to perform another DNS query? (y/n): ')
    if choice.lower() == 'n':
        break

# Close the socket
sock.close()
