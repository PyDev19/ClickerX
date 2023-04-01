# import color modules
from src.colors.constants import *

import sys

def get_style(prompt: str):
  text_color = input(f'Would you like to cuztomize the text color of the {prompt}? (y/n): ')

  if text_color == 'y':
    text_color = int(input(f'What text color do you want the {prompt} to have (answer using the number of the color from the given list): '))
    text_color = COLORS.get(text_color, '')
  elif text_color == 'n':
    text_color = ''
    pass
  
  print('\n')

  background_color = input(f'Would you like to cuztomize the background color of the {prompt}? (y/n): ')

  if background_color == 'y':
    background_color = int(input(f'What background color do you want the {prompt} to have (answer using the number of the background color from the given list): '))
    background_color = BACKGROUND_COLORS.get(background_color, '')
  elif background_color == 'n':
    background_color = ''
    pass
  
  print('\n')
  
  decoration = input(f'Would you like to cuztomize the text decoration of the {prompt}? (y/n): ')
  
  if decoration == 'y':
    decoration = int(input(f'What text decoration do you want the {prompt} to have (answer using the number of the text decoration from the given list): '))
    decoration = TEXT_DECORATIONS.get(decoration, '')
  elif decoration == 'n':
    decoration = ''
    pass
  
  prompt_style = text_color + background_color + decoration
  
  return prompt_style

def style_example(prompt: str, input: str, info: str, starting: str, stopping: str, exit: str):
  sys.stdout.write("\033c")
  sys.stdout.flush()
  
  print('Here is an example of how the style you chose will look: ')
  
  print('\n')
  
  print(f'{prompt}Key to toggle autoclicker (press any key): {input}q{RESET}')
  print(f'{prompt}Key to exit program (press any key): {input}e{RESET}')
  print(f'{prompt}Delay between clicks (in seconds): {input}0.1{RESET}')
  print(f'{prompt}Button to be autoclicked (Left Mouse, Right Mouse, Middle Mouse): {input}Left Mouse{RESET}')
  
  print('\n')
  
  print(f'{info}Key to toggle autoclicker: q{RESET}')
  print(f'{info}Key to exit program: e{RESET}')
  print(f'{info}Delay between clicks: 0.1 seconds{RESET}')
  print(f'{info}Button to be autoclicked: Left Mouse Button{RESET}')
  
  print('\n')
  
  print(f'{starting}Autoclicker Started{RESET}')
  print(f'{stopping}Autoclicker Stopped{RESET}')
  print(f'{exit}Exiting Program{RESET}')

def style_prompts():  
  print('Text Colors Available: | Background Colors Available: | Text Decoration Available: ')
  print(f'{BLACK}1. Black{RESET}               | {B_BLACK}1. Background Black{RESET}          | {BOLD}1. Bold Text{RESET}')
  print(f'{RED}2. Red{RESET}                 | {B_RED}2. Background Red{RESET}            | {UNDERLINE}2. Underline Text{RESET}')
  print(f'{GREEN}3. Green{RESET}               | {B_GREEN}3. Background Green{RESET}          | {REVERSED}3. Reversed Text{RESET}')
  print(f'{YELLOW}4. Yellow{RESET}              | {B_YELLOW}4. Background Yellow{RESET}')
  print(f'{BLUE}5. Blue{RESET}                | {B_BLUE}5. Background Blue{RESET}')
  print(f'{MAGENTA}6. Magenta{RESET}             | {B_MAGENTA}6. Background Magenta{RESET}')
  print(f'{CYAN}7. Cyan{RESET}                | {B_CYAN}7. Background Cyan{RESET}')
  print(f'{WHITE}8. White{RESET}               | {B_WHITE}8. Background White{RESET}')
  print(f'{BRIGHT_BLACK}9. Bright Black{RESET}        | {BB_BLACK}9. Background Bright Black{RESET}')
  print(f'{BRIGHT_RED}10. Bright Red{RESET}         | {BB_RED}10. Background Bright Red{RESET}')
  print(f'{BRIGHT_GREEN}11. Bright Green{RESET}       | {BB_GREEN}11. Background Bright Green{RESET}')
  print(f'{BRIGHT_YELLOW}12. Bright Yellow{RESET}      | {BB_YELLOW}12. Background Bright Yellow{RESET}')
  print(f'{BRIGHT_BLUE}13. Bright Blue{RESET}        | {BB_BLUE}13. Background Bright Blue{RESET}')
  print(f'{BRIGHT_MAGENTA}14. Bright Magenta{RESET}     | {BB_MAGENTA}14. Background Bright Magenta{RESET}')
  print(f'{BRIGHT_CYAN}15. Bright Cyan{RESET}        | {BB_CYAN}15. Background Bright Cyan{RESET}')
  print(f'{BRIGHT_WHITE}16. Bright White{RESET}       | {BB_WHITE}16. Background Bright White{RESET}')
  
  prompt_style = get_style('prompts')
  print('\n')
  print('The prompts will look like this:')
  print(f'{prompt_style}Key to toggle autoclicker (press any key): {RESET}')
  
  print('\n')
  
  input_style = get_style('user inputs')
  print('\n')
  print('The user inputs will look like this:')
  print(f'{input_style}m, k, q, e, r{RESET}')
  
  print('\n')
  
  info_style = get_style('information prompts')
  print('\n')
  print('The information prompts will look like this:')
  print(f'{info_style}Autoclicker toggle key is: q{RESET}')
  
  print('\n')
  
  process_starting_stlye = get_style('process starting prompts')
  print('\n')
  print('The process starting prompts will look like this:')
  print(f'{process_starting_stlye}Autoclicker Started{RESET}')
  
  print('\n')
  
  process_ending_stlye = get_style('process ending prompts')
  print('\n')
  print('The process ending prompts will look like this:')
  print(f'{process_ending_stlye}Autoclicker Stopped{RESET}')
  
  print('\n')
  
  end_error_style = get_style('ending/error prompts')
  print('\n')
  print('The ending/error prompts will look like this:')
  print(f'{end_error_style}Exiting Programm{RESET}')
  
  style_example(prompt_style, input_style, info_style, process_starting_stlye, process_ending_stlye, end_error_style)
