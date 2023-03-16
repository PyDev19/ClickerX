import py_compile, time

from src.colors.constants import RESET, CYAN, GREEN
from src.colors.vtp import enable_vtp, disable_vtp

files = ["main.py", "classes/mouse_clicker.py", "classes/keyboard_clicker.py", "prompts.py", "classes/key.py", "mode.py", "colors/vtp.py", "colors/constants.py", "settings.py"]
files_directory = "src"
compiled_directory = "build/compiled_files"

enable_vtp()

for file in files:
    py_compile.compile(f'{files_directory}/{file}', cfile=f'{compiled_directory}/{file.split(".")[0]}.pyc')
    print(f"{CYAN}Compiled {file} -> {file.split('.')[0]}.pyc{RESET}")
    time.sleep(0.1)
    
print(f"{GREEN}Compiled files can be found in '{compiled_directory}' folder{RESET}")
print("\n")

disable_vtp()
