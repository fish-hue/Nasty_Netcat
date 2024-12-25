---

# Nasty Netcat

## Overview

This project provides a simple command-line interface (CLI) to interactively prepare and execute common `nc` (netcat) commands based on user input. Netcat is a versatile networking utility used for various purposes, including debugging and network exploration.

## Features

- **Command Selection**: Users can select commands based on descriptions without seeing the commands themselves.
- **Dynamic Input**: Users can provide target IP addresses, port numbers, and filenames as needed.
- **Command Execution**: Users have the option to confirm command execution after reviewing the complete command.
- **Basic Error Handling**: The script includes basic error handling during command execution to ensure stability.

## Prerequisites

- Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
- Access to a terminal/command prompt for running the script.

## Installation

1. **Clone the Repository** or **Download the Script**:
   - Clone: 
     ```sh
     git clone https://www.github.com/fish-hue/Nasty_Netcat.git
     ```
   - Download the script directly as `nastync.py.py`.

2. **Navigate to the Script Directory**:
   Open your terminal and navigate to the directory where the script is located:
   ```sh
   cd /path/to/directory
   ```

## Usage

1. **Run the Script**:
   Execute the script using Python:
   ```sh
   python nastync.py
   ```

2. **Follow the Prompts**:
   - **Select a Command**: You’ll be presented with a list of commands. Enter the corresponding number for the command you wish to execute.
   - **Enter Required Information**: Provide the target IP address, port number, and optional filename based on the command's requirements.
   - **Command Review and Confirmation**: After inputting the required information, the complete command will be displayed. Confirm to execute or cancel if you wish.

## Commands

Here’s a list of netcat commands available in the script:

1. **Connect to a target IP and port.**
2. **Listen on a specified port.**
3. **Scan a range of ports on the target IP.**
4. **Listen on a port and send data from a file.**
5. **Connect to a target IP and port and save data to a file.**
6. **Listen on a port and write received data to a file.**
7. **Connect to a target IP and port and send data from a file.**
8. **Listen on a port and execute a bash shell.**
9. **Connect to local IP and port and execute a bash shell.**
10. **Listen on a port and execute cmd.exe on Windows.**
11. **Connect to local IP and port and execute cmd.exe on Windows.**

## Important Notes

- **Security**: Be cautious while executing netcat commands, especially those that run shells (`-e /bin/bash` or `-e cmd.exe`). Ensure the script is used in a secure environment.
- **Administration Rights**: Some commands may require administrative privileges depending on your system configuration. Ensure you have the necessary permissions to execute the commands.

---
