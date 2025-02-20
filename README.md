# 📡 The_Bandwidth_Brigade - Peer-to-Peer Chat Application

This project is a **TCP-based peer-to-peer chat application** developed for **Assignment 1 of CS 216: Introduction to Blockchain**. The application enables multiple peers to communicate over a decentralized network by sending and receiving messages, dynamically tracking active peers, and establishing direct connections.

---

### 👤 **Team Members**

| Roll no.      | Name                       |
|---------------|----------------------------|
| **230004005** | Ansh Jain                  |
| **230001068** | Rayavarapu Sreechand       |
| **230008030** | Shah Mahi Sachinkumar      |
| **230005011** | Bhumika Aggarwal           |
| **IR0035**    | Ahmad Ajmeer Shadoo-Buccus |

---

## 📌 Features

✅ **Decentralized Peer-to-Peer Communication**  
- Connect directly to other peers without a central server.  

✅ **Simultaneous Send and Receive**  
- Uses **multithreading** to handle multiple connections at the same time.  

✅ **Peer Discovery & Management**  
- Tracks connected peers dynamically, maintaining an updated list.  

✅ **Graceful Exit Handling**  
- Properly removes disconnected peers from the list.  

✅ **Interactive Menu System**  
- Allows users to send messages, view connected peers, and connect to new ones easily.  

---

## ⚙️ System Requirements

- **Python 3.x**
- **A working TCP/IP network**
- **VS Code or any Python-compatible IDE** *(Recommended)*  

---

## 📥 Installation & Setup

```sh
# Clone the repository
git clone https://github.com/anshjain1/The_Bandwidth_Brigade.git
cd The_Bandwidth_Brigade

# Run the Python script
python3 p2p_chat.py
```

---

## 📌 How It Works

### 🏁 **1. Start the Server**
- The script prompts you to enter:
  - **Team Name**
  - **Port Number**
- The server starts listening for incoming connections.  

---

### 🔗 **2. Initial Peer Connections (Optional)**
- The application **attempts to connect to predefined peers** upon startup.
- If these peers are online, they are **added to the active peer list**.

---

### 🎛️ **3. Menu Options**
Once the application is running, you’ll see a **menu** with the following options:

| Option | Function |
|--------|----------|
| **1** | Send a message to a peer |
| **2** | View connected peers |
| **3** | Connect to active peers |
| **0** | Quit the application |

---

## 🚀 Usage Guide

### 📩 **Sending a Message**
```sh
# Steps:
1. Select **option 1** from the menu.
2. Enter the recipient’s **IP Address**.
3. Enter the recipient’s **Port Number**.
4. Enter the recipient’s **Team Name**.
5. Type your **message** and hit Enter.
```
📌 If you send **"exit"**, the recipient will be removed from the peer list.

---

### 🔍 **Querying Active Peers**
```sh
# Steps:
1. Select **option 2** from the menu.
2. The application will list **all connected peers** with:
   - **IP Address**
   - **Port Number**
   - **Team Name**
   - **Status** (Active/Connected)
```

---

### 🔌 **Connecting to Active Peers**
```sh
# Steps:
1. Select **option 3** from the menu.
2. The application will attempt to establish a connection with all known active peers.
3. Successfully connected peers are updated in the list.
```

---

## 📝 Example Interaction

### **Starting the Application**
```sh
Enter your team's name: A
Enter your port number: 9991
A's server listening on port 9991
Message sent to 10.206.5.228:6555

******** Menu ********
1. Send message
2. Query active peers
3. Connect to active peers
0. Quit
Enter choice:  
Received message: Hi from B from ('10.213.8.143', 8080, 'B')
Connection closed for ('10.213.8.143', 55877)
```

---

### **Querying Active Peers**
```sh
******** Menu ********
1. Send message
2. Query active peers
3. Connect to active peers
0. Quit
Enter choice: 2
Connected Peers:
Peer Address: 10.206.5.228:6555, Team Name: Team_Subhra, Status: Connected
Peer Address: 10.213.8.143:8080, Team Name: B, Status: Active
```

---

### **Connecting to Active Peers**
```sh
******** Menu ********
1. Send message
2. Query active peers
3. Connect to active peers
0. Quit
Enter choice: 3
Connected to 10.213.8.143:8080
```

---

### **Sending a Message**
```sh
******** Menu ********
1. Send message
2. Query active peers
3. Connect to active peers
0. Quit
Enter choice: 1
Enter the recipient's IP address: 10.213.8.143
Enter the recipient's port number: 8080
Enter the recipient's team name: B
Enter your message: Hi from A 
Message sent to 10.213.8.143:8080 B
```

---

### **Disconnecting a Peer**
```sh
******** Menu ********
1. Send message
2. Query active peers
3. Connect to active peers
0. Quit
Enter choice: 1
Enter the recipient's IP address: 10.213.8.143
Enter the recipient's port number: 8080
Enter the recipient's team name: B
Enter your message: Exit
Disconnected from 10.213.8.143:8080
```

---

### **Exiting the Application**
```sh
******** Menu ********
1. Send message
2. Query active peers
3. Connect to active peers
0. Quit
Enter choice: 0
Exiting...
```

---

## 🛠 Code Overview

### 🏗 Key Functions
```sh
| Function                                        | Description                                                              |
|-------------------------------------------------|--------------------------------------------------------------------------|
| `handle_client_connection(client_socket, addr)` | Handles messages received from connected clients.                        |
| `send_message()`                                | Sends a message to a peer.                                               |
| `query_peers()`                                 | Displays the list of connected peers.                                    |
| `connect_to_peers()`                            | Connects to previously known peers.                                      |
| `accept_connections()`                          | Continuously listens for new peer connections.                           |
| `main()`                                        | Starts the server, initializes peer connections, and runs the user menu. |
```

---

## 🔄 Workflow Diagram

```
+-----------------------+
|  Start Application    |
+-----------+-----------+
            |
            v
+-----------------------+
|  Enter Team Name      |
|  Enter Port Number    |
+-----------+-----------+
            |
            v
+-----------------------+
|  Server Starts       |
|  Listening for Peers |
+-----------+-----------+
            |
            v
+-----------------------+
|  Initial Peer Connect |
+-----------+-----------+
            |
            v
+-----------------------+
|  Show Menu Options   |
+-----------+-----------+
            |
            v
+-----------------------------+
|  Send Message (Option 1)    |
|  Query Peers (Option 2)     |
|  Connect to Peers (Option 3)|
|  Quit (Option 0)            |
+-----------------------------+
```

---



🔥 **Developed as part of CS 216: Introduction to Blockchain - Assignment 1** 🔥  
