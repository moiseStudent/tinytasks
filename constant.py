import os 
import json
import datetime 
from colorama import Fore

#* en este archivo estan todas las constantes y ya xd
INTERFACE_TITLE = f"\t{Fore.BLUE}TINY TASKS V1{Fore.RESET}"

INTERFACE_OPTIONS = f"""{Fore.BLUE}___________________________________________________________{Fore.RESET}

[1] Agregar tarea
[2] Borrar tarea
[3] Cambiar orden de las tareas
[4] Marcar una tarea como hecha
[5] Salir
[R] Reinicio de fabrica

Elige que quieres hacer: """
DELETE_INTERFACE=f"\n{Fore.BLUE}Elige la tarea que quieras eliminar: {Fore.RESET}"
RESET_INTERFACE = f"""{Fore.RED}Estas seguro que quieres reiniciar de fabrica (se eliminaran todas tus tareas):{Fore.RESET}

[S] Si
[N] No

Eleccion: """

