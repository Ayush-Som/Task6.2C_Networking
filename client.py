import socket

# Set up a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define the DNS server's address and port
server_address = ('localhost', 5354)

print('DNS client running...')

while True:
    # Prompt the user to enter a hostname
    hostname = input('Enter a hostname: ')

    # Construct a DNS query message
    query = bytearray(b'\x00\x01\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00') + bytearray(
        hostname.encode('utf-8')) + bytearray(b'\x00\x00\x01\x00\x01')

    # Send the DNS query message to the server
    sock.sendto(query, server_address)

    # Receive the server's response message
    response, address = sock.recvfrom(1024)

    # Extract the IP address from the response message
    ip_address = socket.inet_ntoa(response[-4:])

    # Display the IP address to the user
    print('The IP address of', hostname, 'is', ip_address)

    # Prompt the user to continue or exit
    choice = input('Do you want to perform another DNS query? (y/n): ')
    if choice.lower() == 'n':
        break

# Close the socket
sock.close()
