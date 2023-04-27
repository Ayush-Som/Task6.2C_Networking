import socket

# Set up a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('localhost', 5354))

# Define a dictionary of hostname-IP address mappings
hosts = {'ayush.com': '192.168.1.1', 'www.ayush.com': '192.168.1.4', 'mail.ayush.com': '192.168.1.2',
         'ftp.ayush.com': '192.168.1.3'}

cname = {'ayush.com': 'host.google.com', 'www.ayush.com': 'host.spotify.com', 'mail.ayush.com': 'host.facebook.com',
         'ftp.ayush.com': 'host.images.com'}

print('DNS server listening on port 5354...')

while True:
    # Receive the data sent by the client and the address of the client
    client_request, client_address = sock.recvfrom(2048)

    # Decode the data received from the client to get the domain name for which the IP address is requested
    client_request = client_request.decode()

    # Search for the IP address of the requested domain name in the dictionary
    sample_ip = hosts.get(
        client_request, "No website with this name available").encode()

    sample_cname = cname.get(
        client_request, "No website with this name available").encode()

    # Send the IP address of the requested domain name to the client
    sock.sendto(sample_ip, client_address)
    sock.sendto(sample_cname, client_address)
