# import color modules
from src.colors.vtp import enable_vtp, disable_vtp
from src.colors.constants import RESET, GREEN, CYAN, RED

enable_vtp()

def style_prompts():
    print('''
          Colors available are:
            1. Black
            2. Red
            3. Green
            4. Yellow
            5. Blue
            6. Magenta
            7. Cyan
            8. White
          ''')

disable_vtp()
