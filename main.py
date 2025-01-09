import sys


def main():

    commands = ["paper", "rock", "scissors"]
    # builtins = ["echo", "exit", "type"] due to code change no longer needed

    while True: 
        sys.stdout.write("$ ")

        #Wait for user input
        inp = input()

        if inp in commands: # checks if the command is in the list
            print(f"{inp}: command found")
        elif inp.startswith("type "):
            target = inp[5:]
            if target == "echo":
                sys.stdout.write("echo is a shell builtin\n")
            elif target == "exit":
                sys.stdout.write("exit is a shell builtin\n")
            elif target == "type":
                sys.stdout.write("type is a shell builtin\n")
            else: 
                sys.stdout.write(f"{target}: not found\n")


        elif inp.startswith("echo "): #if the input starts with echo
            sys.stdout.write(inp[5:] + "\n") #skip the first 5 letters and then print.
        elif inp == "exit 0": # exits the infinite loop
            break
        else: # if command is not in the list
            print(f"{inp}: command not found")
        

if __name__ == "__main__":
    main()
