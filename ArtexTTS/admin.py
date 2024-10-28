import ctypes
import sys
import os

def run_as_admin():
    """Re-run the script as administrator if not already."""
    if not ctypes.windll.shell32.IsUserAnAdmin():
        # Re-run the script with admin privileges
        script = sys.argv[0]
        params = " ".join([f'"{arg}"' for arg in sys.argv[1:]])
        try:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, f'"{script}" {params}', None, 1)
            sys.exit(0)  # Exit the original script
        except Exception as e:
            print(f"Failed to elevate privileges: {e}")
            sys.exit(1)
    else:
        print("Running with admin privileges.")

# Example usage
if __name__ == "__main__":
    run_as_admin()
    # Your privileged code here
    print("This code is now running with admin privileges.")
