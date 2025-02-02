import socket
import threading

# Global dictionary to store connected peers
peers = {}
exit_event = threading.Event()  # Event to signal exit

# Function to handle receiving messages
def handle_receive(sock):
    while not exit_event.is_set():  # Check if exit event is set
        try:
            # Receive message from the socket
            message, addr = sock.recvfrom(1024)  # Receive message and address
            message = message.decode('utf-8')  # Decode the message
            if message:
                print(f"\nReceived message: {message} from {addr}")  # Print the received message
                if message.lower() == "exit":  # Check if the message is an exit command
                    print(f"A peer has disconnected: {addr}")
                    # Remove the peer from the peers dictionary
                    peers.pop(addr, None)
                else:
                    # Add the peer to the peers dictionary if not already present
                    peers[addr] = message  # Store the message or name of the peer
        except Exception as e:
            if exit_event.is_set():  # If exit event is set, break without error
                break
            print(f"Error receiving message: {e}")  # Print any errors that occur
            break  # Exit the loop on error

# Function to send messages to peers
def send_message():
    # Get recipient's IP address and port number
    recipient_ip = input("Enter the recipient's IP address (or 'localhost' for local testing): ")  
    recipient_port = int(input("Enter the recipient's port number: "))  
    message = input("Enter your message: ")  # Get the message to send

    if message.lower() == "exit":  # Check if the message is an exit command
        exit_message = "exit"  # Prepare exit message
        sock.sendto(exit_message.encode('utf-8'), (recipient_ip, recipient_port))  # Send exit message
        peers.pop((recipient_ip, recipient_port), None)  # Remove the peer from the dictionary
        return  # Exit the function

    try:
        # Send the message to the specified recipient
        sock.sendto(message.encode('utf-8'), (recipient_ip, recipient_port))  
        print(f"Message sent to {recipient_ip}:{recipient_port}")  # Confirm message sent
        # Add the recipient to the peers dictionary if not already present
        peers[(recipient_ip, recipient_port)] = message  # Store the message or name of the peer
    except Exception as e:
        print(f"Error sending message: {e}")  # Print any errors that occur

# Function to query connected peers
def query_peers():
    if peers:  # Check if there are any connected peers
        print("Connected Peers:")  # Print header
        for peer in peers:  # Iterate through the peers
            print(f"Peer: {peer[0]}:{peer[1]}")  # Print each peer's IP and port
    else:
        print("No connected peers.")  # Notify if no peers are connected

# Main function
def main():
    global sock  # Declare sock as global to access it in other functions
    name = input("Enter your name: ")  # Get user's name
    port = int(input("Enter your port number: "))  # Get port number

    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
    sock.bind(('', port))  # Bind the socket to the specified port

    print(f"Server listening on port {port}")  # Notify that the server is listening

    # Start the receiving thread
    threading.Thread(target=handle_receive, args=(sock,), daemon=True).start()  # Start a thread to handle incoming messages

    # Main menu loop
    while True:
        print("\n******** Menu ********")  # Print menu header
        print("1. Send message")  # Option to send a message
        print("2. Query connected peers")  # Option to query connected peers
        print("0. Quit")  # Option to quit
        choice = input("Enter choice: ")  # Get user choice

        if choice == '1':
            send_message()  # Call function to send a message
        elif choice == '2':
            query_peers()  # Call function to query connected peers
        elif choice == '0':
            print("Exiting...")  # Notify that the program is exiting
            exit_event.set()  # Set the exit event to signal the receiving thread to stop
            break  # Exit the loop
        else:
            print("Invalid choice. Please try again.")  # Handle invalid choice

    sock.close()  # Close the socket when done

# Entry point of the program
if __name__ == "__main__":
    main()  # Call the main function to start the program