# Remote Administration Tool (RAT)

A simple server-client application for remote system administration.

## Server Application

The server application is built with Electron and provides a GUI interface for managing connected clients.

### Installation

1. Install dependencies:

````bash
npm install# Remote Access Tool (RAT)

A simple remote access tool built with Electron and Node.js.

## Features

- TCP Socket Communication
- Command Execution
- Screenshot Capture
- Client Management
- Real-time Command Output

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   npm install
````

3. Start the server:
   ```bash
   npm start
   ```
4. Run the client on target machines:
   ```bash
   node client.js
   ```

## Usage

1. Start the server application
2. Enter the port number (default: 3000)
3. Click "Start Server"
4. Run the client on target machines
5. Connected clients will appear in the list
6. Use the command window to execute commands

## LIST OF ALL COMMANDS

### System Information Commands

```
systeminfo
```

Shows detailed system information including:

- Operating System details
- Processor information
- Memory details
- System configuration
- Network adapter information

### Network Information

```
ipconfig /all
```

Displays all network adapter information including:

- IP addresses
- MAC addresses
- DNS settings
- Network adapters status

### Process Management

```
tasklist
```

Shows all running processes with:

- Process names
- Process IDs (PIDs)
- Memory usage
- Session information

### File System Commands

```
dir
```

Lists directory contents with:

- File names
- File sizes
- Creation dates
- File attributes

### System Uptime

```
systeminfo | find "System Boot Time"
```

Shows when the system was last booted

### Memory Usage

```
wmic OS get FreePhysicalMemory,TotalVisibleMemorySize /Value
```

Displays:

- Total available memory
- Free physical memory
- Memory usage statistics

### Disk Information

```
wmic logicaldisk get size,freespace,caption
```

Shows:

- Drive letters
- Total disk space
- Free disk space
- Drive types

### Service Management

```
net start
```

Lists all running services with:

- Service names
- Service status
- Service types

### User Information

```
net user
```

Displays:

- User accounts
- Account status
- Last login times
- Password requirements

### Network Connections

```
netstat -ano
```

Shows:

- Active connections
- Listening ports
- Process IDs
- Connection states

### Additional Useful Commands

#### System Performance

```
wmic cpu get loadpercentage
```

Shows current CPU usage

#### Running Services

```
sc query
```

Lists detailed service information

#### Network Statistics

```
netstat -s
```

Shows network statistics

#### System Path

```
echo %PATH%
```

Displays system PATH environment variable

#### System Architecture

```
systeminfo | findstr /B /C:"System Type"
```

Shows system architecture (32/64 bit)

#### Windows Version

```
ver
```

Displays Windows version information

#### System Uptime (Alternative)

```
wmic OS get LastBootUpTime
```

Shows system boot time

#### Memory Usage (Detailed)

```
wmic process get WorkingSetSize,ProcessId
```

Shows detailed memory usage per process

#### Disk Space (Detailed)

```
wmic logicaldisk get size,freespace,caption,volumename
```

Shows detailed disk information

#### Network Adapter Status

```
netsh interface show interface
```

Shows network adapter status

#### System Time

```
time /t
```

Shows current system time

#### System Date

```
date /t
```

Shows current system date

## Notes

- Some commands may require administrative privileges
- Command output format may vary depending on Windows version
- Some commands may take a few seconds to execute
- Use with caution on remote systems
- Always verify command output before taking action

## Security Considerations

- Use strong passwords
- Implement proper authentication
- Monitor system logs
- Regular security updates
- Network security best practices

## License

MIT

````

2. Start the server:

```bash
npm start
````

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
node client.js 192.168.1.235 8443
```

### Features

- Automatically collects and sends system information
- Executes commands received from the server
- Returns command execution results
- Gracefully handles connection termination

## Security Note

This application is for educational purposes only. Use it responsibly and only on systems you own or have permission to access.
