import subprocess
import os
import winreg

def export_registry(key_path, export_path):
    """Export registry to a .reg file."""
    export_command = ["reg", "export", key_path, export_path, "/y"]
    subprocess.run(export_command, check=True)


key_path = r"SOFTWARE\Microsoft\Speech_OneCore\Voices\Tokens"

# with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path) as key:
#             for i in range(0, winreg.QueryInfoKey(key)[0]):
#                 voice_key = winreg.EnumKey(key, i)
#                 print(f"{key_path}\\{voice_key}")
#                 export_registry(f"HKEY_LOCAL_MACHINE\\{key_path}\\{voice_key}", os.path.join(os.getcwd(), "exp", f"{voice_key}.reg"))
#             print("Unlocked all voices successfully.")

# export_registry(key_path, export_path)




import os

def list_files_recursive(directory):
    file_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_paths.append(os.path.join(root, file))
    return file_paths

target_line = r"[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech_OneCore\Voices\Tokens"
def read_modify_and_write_file(filename):
    try:
        with open(filename, 'r', encoding="UTF-16") as file:
            content = file.read()
            lines = content.splitlines()  # Split content into lines

        # Modify only lines that start with the target line
        for i, line in enumerate(lines):
            if line.startswith(target_line):
                # Replace the specified text in the line
                lines[i] = line.replace("Speech_OneCore", "Speech")

        # Join the modified lines back and write to the file
        modified_content = "\n".join(lines)
        with open(filename, 'w', encoding="UTF-16") as file:
            file.write(modified_content)
        print(f"File '{filename}' updated successfully.")

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def import_f(reg_file_path):
    try:
        # Use 'reg import' command to import the registry file
        result = subprocess.run(["reg", "import", reg_file_path], check=True, capture_output=True, text=True)
        print("Registry file imported successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error importing registry file: {e.stderr}")

if __name__ == "__main__":
    directory_path = os.path.join(os.getcwd(), "exp")
    file_paths = list_files_recursive(directory_path)

    # Use a regular string but escape backslashes

    for file_path in file_paths:
        # read_and_print_file(file_path)
        # read_modify_and_write_file(file_path)
        import_f(file_path)