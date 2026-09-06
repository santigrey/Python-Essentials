# Requires colorama; install with: pip install colorama
# ALAB 356.1 - Task 3: Using PIP and an external package.

from colorama import Fore, Style, init

# autoreset=True puts the color back to normal after every print.
init(autoreset=True)

print(Fore.GREEN + "Green text: colorama is installed and working.")
print(Fore.RED + "Red text: this line is a warning.")
print(Fore.CYAN + "Cyan text: this line is a note.")
print(Style.BRIGHT + Fore.YELLOW + "Bright yellow text: this line stands out.")
print("Back to the normal terminal color.")
