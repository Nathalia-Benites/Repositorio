from colorama import init, Fore, Style
from termcolor import colored
class ConsoleColors:
    """Clase para definir códigos de colores ANSI para la consola."""
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
# Ejemplo de uso
print(ConsoleColors.BOLD + "Texto en negrita" + ConsoleColors.RESET)
print(ConsoleColors.RED + "Texto en rojo" + ConsoleColors.RESET)
print(ConsoleColors.GREEN + "Texto en verde" + ConsoleColors.RESET)
print(ConsoleColors.YELLOW + "Texto en amarillo" + ConsoleColors.RESET)
print(ConsoleColors.BLUE + "Texto en azul" + ConsoleColors.RESET)
print(ConsoleColors.MAGENTA + "Texto en magenta" + ConsoleColors.RESET)
print(ConsoleColors.CYAN + "Texto en cyan" + ConsoleColors.RESET)
# Ejemplo de uso
print(colored('Texto en rojo', 'red', attrs=['bold']))
print(colored('Texto en verde', 'green', attrs=['bold']))
# Inicializar colorama (solo es necesario en Windows)
init()
# Ejemplo de uso
print(Style.BRIGHT + Fore.RED + "Texto en negrita y rojo" + Style.RESET_ALL)
print(Fore.GREEN + "Texto en verde" + Style.RESET_ALL)
print(Fore.YELLOW + "Texto en amarillo" + Style.RESET_ALL)
