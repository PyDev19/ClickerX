# import color modules
from src.colors.vtp import enable_vtp, disable_vtp
from src.colors.constants import *

# import module to manage terminal
from src.terminal import unlock_terminal, lock_terminal

enable_vtp()

colors = {
  1: BLACK,
  2: RED,
  3: GREEN,
  4: YELLOW,
  5: BLUE,
  6: MAGENTA,
  7: CYAN,
  8: WHITE,
  9: B_BLACK,
  10: B_RED,
  11: B_GREEN,
  12: B_YELLOW,
  13: B_BLUE,
  14: B_MAGENTA,
  15: B_CYAN,
  16: B_WHITE
}

def style_prompts():
  unlock_terminal()

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
      9. Light Black
      10. Light Red
      11. Light Green
      12. Light Yellow
      13. Light Blue
      14. Light Magenta
      15. Light Cyan
      16. Light White
  ''')
  
  try:
    prefered_prompt_color = int(input('What is your prefered prompt color (answer with the number of the color): '))
  except ValueError:
    print('Please enter a number from the given list of color')
    prefered_prompt_color = int(input('What is your prefered prompt color (answer with the number of the color): '))

  prefered_prompt_color = colors.get(prefered_prompt_color, None)

  lock_terminal()

disable_vtp()
