#Three visual studio code shortcuts must be validated if all three are met, you must inform the user that congratulations is correct otherwise you should indicate that it does not apply.

shortcuts_to_vsc= ["Ctrl+O","Ctrl+Y","Ctrl+A","Ctrl+P","Ctrl+K","Ctrl+S","Ctrl+X","Ctrl+Y","Ctrl+"]
print(f"These are several commands you have:\n{shortcuts_to_vsc}")

def commands (command_one,commands_two,commands_three):

    if command_one == "Ctrl+O" or command_one == "Ctrl+Y" or command_one == "Ctrl+A" or command_one == "Ctrl+P" or command_one == "Ctrl+K" or command_one == "Ctrl+S" or command_one == "Ctrl+X" or command_one == "Ctrl+Y" or command_one == "Ctrl+":
        print(f"{command_one} is a valid command")
    
    elif commands_two == "Ctrl+X" or commands_two == "Ctrl+Y" or commands_two == "Ctrl+" or commands_two == "Ctrl+P" or commands_two == "Ctrl+K" or commands_two == "Ctrl+S" or commands_two == "Ctrl+A" or commands_two == "Ctrl+Y" or commands_two == "Ctrl+O":
        print(f"{commands_two} is a valid command")
    
    elif commands_three == "Ctrl+" or commands_three == "Ctrl+Y" or commands_three == "Ctrl+X" or commands_three == "Ctrl+S" or commands_three == "Ctrl+K" or commands_three == "Ctrl+P" or commands_three == "Ctrl+A" or commands_three == "Ctrl+Y" or commands_three == "Ctrl+O":
        print(f"{commands_three} is a valid command")
    else:
        print("not apply")

commands(command_one=input("Insert a command: "),commands_two=input("Insert a command: "),commands_three=input("Insert a command: "))