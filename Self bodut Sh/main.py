import os
import subprocess

def py_shell():
    print("Welcome to PyShell! *Myshell Type 'exit' to quit.")
    
    while True:
        # display prompt to user
        command = input("PyShell> ")
        
        # Exit condition
        if command.lower() in ["exit", "quit"]:
            print("Exiting PyShell. Goodbye!")
            break
        
        # Execute built-in shell commands
        try:
            if command.strip():  # ignore mt commands
                # use subprocess to execute command
                result = subprocess.run(command, shell=True, text=True, 
                                        capture_output=True)
                
                # display output or error
                if result.stdout:
                    print(result.stdout.strip())
                if result.stderr:
                    print(result.stderr.strip())
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    py_shell()