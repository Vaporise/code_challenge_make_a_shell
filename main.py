import sys
import os


def main():

    commands = ["paper", "rock", "scissors"]
    # builtins = ["echo", "exit", "type"] due to code change no longer needed
    path_dirs = os.environ.get("PATH", "").split(":")

    while True: 
        sys.stdout.write("$ ")

        #Wait for user input
        inp = input()

        if inp in commands: # checks if the command is in the list
            print(f"{inp}: command found")
        elif inp.startswith("type "): #check if command starts with type for using the type command
            target = inp[5:] #ignores the first 5 characters (type ) and assigns all the string after.
            if target in ["echo", "exit", "type"]:
                sys.stdout.write(f"{target} is a shell builtin\n")
            else:

                found = False
                for directory in path_dirs:
                    full_path = os.path.join(directory, target)
                    if os.path.exists(full_path) and os.access(full_path, os.X_OK):
                        sys.stdout.write(f"{target} is {full_path}\n")
                        found = True
                        break
                if not found:
                    sys.stdout.write(f"{target}: not found\n")

        elif inp.startswith("echo "): #if the input starts with echo
            sys.stdout.write(inp[5:] + "\n") #skip the first 5 letters and then print.
        elif inp == "exit": # exits the infinite loop
            break
        else: # if command is not in the list
            print(f"{inp}: command not found")
        
        
        

if __name__ == "__main__":
    main()
