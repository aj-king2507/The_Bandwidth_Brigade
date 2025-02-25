import socket
import threading

# Dictionary to store connected peers (IP, server_port)
peers = {}
exit_event = threading.Event()  # Event to signal exit
DELIMITER = ":"  # Delimiter to separate port and ip

def normalize_ip(ip):
    try:
        return socket.gethostbyname(ip)
    except socket.gaierror:
        return ip  # If resolution fails, return the original IP

# Function to handle receiving messages from a specific client
def handle_client_connection(client_socket, addr):
    try:
        while not exit_event.is_set():
            # Receive data from the client
            data = client_socket.recv(1024).decode('utf-8').strip()
            if not data:
                break  # Client disconnected

            # Split the received data into port and message using the delimiter
            if " " in data:
                peer_server_address, peer_team_name, message = data.split(" ", 2)
                if DELIMITER in peer_server_address:
                    peer_server_ip, peer_server_port = peer_server_address.split(DELIMITER, 1)

                    # Validate if the received port is an integer
                    if peer_server_port.isdigit():
                        normalized_ip = normalize_ip(addr[0])  # Normalize the IP address
                        peer_info = (normalized_ip, int(peer_server_port), peer_team_name)  # (Normalized IP, server_port)
                        if peer_info not in peers:
                            peers[peer_info] = "Active"  # Add peer to the dictionary

                        print(f"\nReceived message: {message} from {peer_info}")

                        # Handle "exit" message
                        if message.lower() == "exit":
                            print(f"A peer has disconnected: {peer_info}")
                            peers.pop(peer_info, None)  # Remove the peer from the dictionary
                            break

                    else:
                        print(f"Invalid port received from {addr}: {peer_server_port}")

                else:
                    print(f"Invalid address received from {addr}: {peer_server_address}")

            else:
                print(f"Malformed data received from {addr}: {data}")

    except Exception as e:
        print(f"Error handling client {addr}: {e}")

    finally:
        client_socket.close()  # Close the client socket
        print(f"Connection closed for {addr}")

# Function to send messages to peers
def send_message():
    recipient_ip = input("Enter the recipient's IP address: ")
    recipient_port = int(input("Enter the recipient's port number: "))
    recipient_team_name = input("Enter the recipient's team name: ")
    message = input("Enter your message: ")

    normalized_ip = normalize_ip(recipient_ip)  # Normalize the recipient's IP address
    addr = (normalized_ip, recipient_port, recipient_team_name)

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as temp_sock:
            temp_sock.settimeout(5)  # Set a timeout for connection attempts
            temp_sock.connect((recipient_ip, recipient_port))

            # Send your server port and message in a structured format
            formatted_message = f"{server_ip}{DELIMITER}{server_port} {team_name} {message}"
            temp_sock.sendall(formatted_message.encode('utf-8'))

            if message.lower() == "exit":
                peers.pop(addr, None)  # Remove the peer from the dictionary if exiting
                print(f"Disconnected from {recipient_ip}:{recipient_port}")
            else:
                peers[addr] = "Connected"  # Add/update peer in the dictionary
                print(f"Message sent to {recipient_ip}:{recipient_port} {recipient_team_name}")

    except socket.timeout:
        print(f"Connection to {recipient_ip}:{recipient_port} timed out.")
    except Exception as e:
        print(f"Error sending message: {e}")

# Function to query connected peers
def query_peers():
    if peers:  # Check if there are any connected peers
        print("Connected Peers:")
        for peer,status in peers.items():  # Iterate through the peers dictionary
            print(f"Peer Address: {peer[0]}:{peer[1]}, Team Name: {peer[2]}, Status: {status}")  # Print each peer's IP and port
    else:
        print("No connected peers.")

# Function to connect to active peers and send a connection message (Bonus)
def connect_to_peers():
    for peer in list(peers.keys()):  # Iterate through all known peers
        if peers[peer] == "Active":
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as temp_sock:
                    temp_sock.settimeout(5)  # Set a timeout for connection attempts
                    temp_sock.connect((peer[0],peer[1]))  # Connect to the peer's server port

                    # Send your server port and connection message in a structured format
                    formatted_message = f"{server_ip}{DELIMITER}{server_port} {team_name} connection message"
                    temp_sock.sendall(formatted_message.encode('utf-8'))
                    print(f"Connected to {peer[0]}:{peer[1]}")
                    peers[peer] = "Connected"
            except socket.timeout:
                print(f"Connection to {peer[0]}:{peer[1]} timed out.")
            except Exception as e:
                print(f"Failed to connect to {peer[0]}:{peer[1]} - {e}")

# Start a thread to accept incoming connections
def accept_connections():
    while not exit_event.is_set():
        try:
            client_socket, addr = sock.accept()  # Accept a new connection
            threading.Thread(target=handle_client_connection, args=(client_socket, addr), daemon=True).start()
        except Exception as e:
            if exit_event.is_set():
                break

# Main function
def main():
    global sock, server_port, server_ip, team_name

    team_name = input("Enter your team's name: ")  # Enter your team name
    server_port = int(input("Enter your port number: "))  # Get port number

    # Create a TCP socket and bind it to the specified port
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', server_port))
    sock.listen(5)  # Start listening for incoming connections
    server_ip = socket.gethostbyname(socket.gethostname())

    print(f"{team_name}'s server listening on port {server_port}")

    threading.Thread(target=accept_connections, daemon=True).start()

    # try:
    #     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as temp_sock:
    #         temp_sock.settimeout(5)  # Set a timeout for connection attempts
    #         temp_sock.connect(("10.206.4.122", 1255))

    #         # Send your server port and message in a structured format
    #         formatted_message = f"{server_ip}{DELIMITER}{server_port} {team_name} Hi from The_Bandwidth_Brigade"
    #         temp_sock.sendall(formatted_message.encode('utf-8'))

    #         peers[("10.206.4.122",1255, "Team_Subhra")] = "Connected"  # Add/update peer in the dictionary
    #         print(f"Message sent to 10.206.4.122:1255")
    # except socket.timeout:
    #     print(f"Connection to 10.206.4.122:1255 timed out.")
    # except Exception as e:
    #     print(f"Error sending message: {e}")

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as temp_sock:
            temp_sock.settimeout(5)  # Set a timeout for connection attempts
            temp_sock.connect(("10.206.5.228", 6555))

            # Send your server port and message in a structured format
            formatted_message = f"{server_ip}{DELIMITER}{server_port} {team_name} Hi from The_Bandwidth_Brigade"
            temp_sock.sendall(formatted_message.encode('utf-8'))

            peers[("10.206.5.228",6555, "Team_Subhra")] = "Connected"  # Add/update peer in the dictionary
            print(f"Message sent to 10.206.5.228:6555")
    except socket.timeout:
        print(f"Connection to 10.206.5.228:6555 timed out.")
    except Exception as e:
        print(f"Error sending message: {e}")

    while True:
        print("\n******** Menu ********")
        print("1. Send message")
        print("2. Query active peers")
        print("3. Connect to active peers")
        print("0. Quit")
        choice = input("Enter choice: ")

        if choice == '1':
            send_message()
        elif choice == '2':
            query_peers()
        elif choice == '3':
            connect_to_peers()
        elif choice == '0':
            print("Exiting...")
            exit_event.set()  # Signal all threads to stop
            break
        else:
            print("Invalid choice. Please try again.")

    sock.close()  # Close the main socket when done

if __name__ == "__main__":
    main()
