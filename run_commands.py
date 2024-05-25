import subprocess

def run_command(command, input_data):
    return subprocess.run(
        command,
        input=input_data,  # Encode input data to bytes
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        shell=True
    )

output_file_path = "./output.txt"
file_path = "./commands.txt"  # Path to the file containing commands

# Read commands from the file
with open(file_path, "r") as file:
    commands = file.readlines()

# Join all commands into a single string with newline separators for interactive input
input_data = "\n".join(command.strip() for command in commands)

command = "python main.py"

print("Executing commands...")
result = run_command(command, input_data)
print(result.stdout, result.stderr)

# Write the output to a file
with open(output_file_path, "w") as output_file:
    output_file.write(result.stdout)
    output_file.write(result.stderr)
