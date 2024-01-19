import os, sys # For file control and exception catching

def main():
    try:
        # Attempts to open config file for script
        f = open(os.path.dirname(os.path.realpath(__file__)) + "\\steam.txt", 'r')
        steam = f.readline()
        f.close()
        sys.exit("Script succeccful, your game should now be your " + rename_game(steam) + " install")
    # If the file didn't exist, run these lines
    except FileNotFoundError:
        # Creates file to write to
        f = open(os.path.dirname(os.path.realpath(__file__)) + "\\steam.txt", 'w')
        # Asks for the steam path
        location = input("Enter your steam game folder path: ")
        f.write(location)
        # This flush line shouldn't be neccesarry cause closing the program SHOULD do this but it never does for some reason; i should find a better way to do this
        f.flush()
        f.close()
        check = "fugfdgjg"
        while check != 'Y' and check != 'y' and check != 'n' and check != 'N':
            check = input("Is your game currently modded (Y/N): ")
        if check == 'Y' or check == 'y':
            try:
                os.rename(location + "\\Omori", location + "\\Omori (Modded)")
                print("Succefully renamed folder. Now reinstall Omori through Steam, then the script should auto switch your game version between modded and unmodded. Press enter to exit script")
                no = input("")
                sys.exit()
            except OSError:
                print("An error occured. This is usually caused by having the game directory open in file explorer while running the script. Please close the file explorer, then run the script again.")
                no = input("")
                sys.exit()
        elif check == 'N' or check == 'n':
            try:
                os.rename(location + "\\Omori", location + "\\Omori (Vanilla)")
                print("Succefully renamed folder. Now reinstall Omori through Steam, mod the game, then the script should auto switch your game between modded and unmodded. Press enter to exit script")
                no = input("")
                sys.exit()
            except OSError:
                print("An error occured. This is usually caused by having the game directory open in file explorer while running the script. Please close the file explorer, then run the script again.")
                input()
                sys.exit()

# The actual game switching script
def rename_game(game):
    if os.path.exists(game + "\\Omori\\www\\mods"):
        try:
            # Rename current install to modded
            os.rename(game + "\\Omori", game + "\\Omori (Modded)")
            # Rename vanilla to steam compatible name
            os.rename(game + "\\Omori (Vanilla)", game + "\\Omori")
            return "vanilla"
        except OSError:
            print("An error occured. This is usually caused by having the game directory open in file explorer while running the script. Please close the file explorer, then run the script again.")
            input()
            sys.exit()
    else:
        try:
            # Rename current install to vanilla
            os.rename(game + "\\Omori", game + "\\OMORI (Vanilla)")
            # Rename modded install to steam compatible name
            os.rename(game + "\\OMORI (Modded)", game + "\\OMORI")
            return "modded"
        except OSError:
            print("An error occured. This is usually caused by having the game directory open in file explorer while running the script. Please close the file explorer, then run the script again.")
            input()
            sys.exit()

# Run the program
main()