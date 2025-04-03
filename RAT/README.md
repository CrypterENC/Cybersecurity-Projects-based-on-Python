# Remote Administration Tool (RAT)

A simple server-client application for remote system administration.

## Server Application

The server application is built with Electron and provides a GUI interface for managing connected clients.

### Installation

1. Install dependencies:

```bash
npm install
```

2. Start the server:

```bash
npm start
```

### Features

- Start/Stop TCP server on specified port
- View connected clients in a table
- Execute commands on remote clients
- View command execution results
- Gracefully close client connections

## Client Application

The client application is a Node.js script that connects to the server and executes commands.

### Usage

```bash
node client.js <server_ip> <port>
```

Example:

```bash
node client.js 192.168.X.XXX 8443
```

### Features

- Automatically collects and sends system information
- Executes commands received from the server
- Returns command execution results
- Gracefully handles connection termination

## Security Note

This application is for educational purposes only. Use it responsibly and only on systems you own or have permission to access.
