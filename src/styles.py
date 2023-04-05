# import necessary modules
import termios
from src.settings import save_styles_settings
from src.colors.constants import *
from src.terminal import lock_terminal, unlock_terminal

import sys

def get_style(prompt: str) -> str:
    termios.tcflush(sys.stdin, termios.TCIOFLUSH)
    change_style = input(f'Would you like to cuztomize the style of the {prompt}? (y/n): ')
    
    if change_style == 'y':
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

    elif change_style == 'n':
        print('Ok going to next option...')
        return ''

def style_example(prompt: str, input: str, info: str, starting: str, stopping: str, exit: str) -> None:
    sys.stdout.write("\033c")
    sys.stdout.flush()
    
    print('Here is an example of how the style you chose will look: ')
    
    print('\n')
    if prompt == '':
        if input == '':
            print(f'{INPUT_COLOR}Key to toggle autoclicker (press any key): {USER_INPUT_COLOR}q{RESET}')
            print(f'{INPUT_COLOR}Key to exit program (press any key): {USER_INPUT_COLOR}e{RESET}')
            print(f'{INPUT_COLOR}Delay between clicks (in seconds): {USER_INPUT_COLOR}0.1{RESET}')
            print(f'{INPUT_COLOR}Button to be autoclicked (Left Mouse, Right Mouse, Middle Mouse): {USER_INPUT_COLOR}Left Mouse{RESET}')
        else:
            print(f'{INPUT_COLOR}Key to toggle autoclicker (press any key): {input}q{RESET}')
            print(f'{INPUT_COLOR}Key to exit program (press any key): {input}e{RESET}')
            print(f'{INPUT_COLOR}Delay between clicks (in seconds): {input}0.1{RESET}')
            print(f'{INPUT_COLOR}Button to be autoclicked (Left Mouse, Right Mouse, Middle Mouse): {input}Left Mouse{RESET}')
    else:
        if input == '':
            print(f'{prompt}Key to toggle autoclicker (press any key): {USER_INPUT_COLOR}q{RESET}')
            print(f'{prompt}Key to exit program (press any key): {USER_INPUT_COLOR}e{RESET}')
            print(f'{prompt}Delay between clicks (in seconds): {USER_INPUT_COLOR}0.1{RESET}')
            print(f'{prompt}Button to be autoclicked (Left Mouse, Right Mouse, Middle Mouse): {USER_INPUT_COLOR}Left Mouse{RESET}')
        else:
            print(f'{prompt}Key to toggle autoclicker (press any key): {input}q{RESET}')
            print(f'{prompt}Key to exit program (press any key): {input}e{RESET}')
            print(f'{prompt}Delay between clicks (in seconds): {input}0.1{RESET}')
            print(f'{prompt}Button to be autoclicked (Left Mouse, Right Mouse, Middle Mouse): {input}Left Mouse{RESET}')
    
    print('\n')
    
    if info == '':
        print(f'{FIRST_INFO_COLOR}Key to toggle autoclicker: q{RESET}')
        print(f'{FIRST_INFO_COLOR}Key to exit program: e{RESET}')
        print(f'{FIRST_INFO_COLOR}Delay between clicks: 0.1 seconds{RESET}')
        print(f'{FIRST_INFO_COLOR}Button to be autoclicked: Left Mouse Button{RESET}')
    else:
        print(f'{info}Key to toggle autoclicker: q{RESET}')
        print(f'{info}Key to exit program: e{RESET}')
        print(f'{info}Delay between clicks: 0.1 seconds{RESET}')
        print(f'{info}Button to be autoclicked: Left Mouse Button{RESET}')
    
    print('\n')
    
    if starting == '':
        print(f'{FIRST_INFO_COLOR}Autoclicker Started{RESET}')
    else:
        print(f'{starting}Autoclicker Started{RESET}')

    if stopping == '':
        print(f'{FINAL_INFO_COLOR}Autoclicker Stopped{RESET}')
    else:
        print(f'{stopping}Autoclicker Stopped{RESET}')
    
    if exit == '':
        print(f'{END_INFO_COLOR}Exiting Program{RESET}')
    else:
        print(f'{exit}Exiting Program{RESET}')

def style_prompts(toggle_key: str, exit_key: str):  
    print('Text Colors Available: | Background Colors Available: | Text Decoration Available: ', flush=True)
    print(f'{BLACK}1. Black{RESET}               | {B_BLACK}1. Background Black{RESET}          | {BOLD}1. Bold Text{RESET}', flush=True)
    print(f'{RED}2. Red{RESET}                 | {B_RED}2. Background Red{RESET}            | {UNDERLINE}2. Underline Text{RESET}', flush=True)
    print(f'{GREEN}3. Green{RESET}               | {B_GREEN}3. Background Green{RESET}          | {REVERSED}3. Reversed Text{RESET}', flush=True)
    print(f'{YELLOW}4. Yellow{RESET}              | {B_YELLOW}4. Background Yellow{RESET}', flush=True)
    print(f'{BLUE}5. Blue{RESET}                | {B_BLUE}5. Background Blue{RESET}', flush=True)
    print(f'{MAGENTA}6. Magenta{RESET}             | {B_MAGENTA}6. Background Magenta{RESET}', flush=True)
    print(f'{CYAN}7. Cyan{RESET}                | {B_CYAN}7. Background Cyan{RESET}', flush=True)
    print(f'{WHITE}8. White{RESET}               | {B_WHITE}8. Background White{RESET}', flush=True)
    print(f'{BRIGHT_BLACK}9. Bright Black{RESET}        | {BB_BLACK}9. Background Bright Black{RESET}', flush=True)
    print(f'{BRIGHT_RED}10. Bright Red{RESET}         | {BB_RED}10. Background Bright Red{RESET}', flush=True)
    print(f'{BRIGHT_GREEN}11. Bright Green{RESET}       | {BB_GREEN}11. Background Bright Green{RESET}', flush=True)
    print(f'{BRIGHT_YELLOW}12. Bright Yellow{RESET}      | {BB_YELLOW}12. Background Bright Yellow{RESET}', flush=True)
    print(f'{BRIGHT_BLUE}13. Bright Blue{RESET}        | {BB_BLUE}13. Background Bright Blue{RESET}', flush=True)
    print(f'{BRIGHT_MAGENTA}14. Bright Magenta{RESET}     | {BB_MAGENTA}14. Background Bright Magenta{RESET}', flush=True)
    print(f'{BRIGHT_CYAN}15. Bright Cyan{RESET}        | {BB_CYAN}15. Background Bright Cyan{RESET}', flush=True)
    print(f'{BRIGHT_WHITE}16. Bright White{RESET}       | {BB_WHITE}16. Background Bright White{RESET}', flush=True)
    
    unlock_terminal()

    prompt_style = get_style('prompts')
    print('\n')
    if prompt_style == '':
        print('The prompts will look like this:')
        print(f'{INPUT_COLOR}Key to toggle autoclicker (press any key): {RESET}')
    else:
        print('The prompts will look like this:')
        print(f'{prompt_style}Key to toggle autoclicker (press any key): {RESET}')
    
    print('\n')
    
    input_style = get_style('user inputs')
    print('\n')
    print('The prompts will look like this:')
    if input_style == '':
        print(f'{USER_INPUT_COLOR}User inputs: q, e, r, m, q, e{RESET}')
    else:
        print(f'{input_style}User inputs: q, e, r, m, q, e{RESET}')
    
    print('\n')
    
    info_style = get_style('information prompts')
    print('\n')
    print('The information prompts will look like this:')
    if info_style == '':
        print(f'{FIRST_INFO_COLOR}Key to toggle autoclicker is: q{RESET}')
    else:
        print(f'{info_style}Autoclicker toggle key is: q{RESET}')
    
    print('\n')
    
    process_starting_stlye = get_style('process starting prompts')
    print('\n')
    print('The process starting prompts will look like this:')
    if process_starting_stlye == '':
        print(f'{FIRST_INFO_COLOR}Autoclicker Started{RESET}')
    else:
        print(f'{process_starting_stlye}Autoclicker Started{RESET}')
    
    print('\n')
    
    process_ending_stlye = get_style('process ending prompts')
    print('\n')
    print('The process ending prompts will look like this:')
    if process_ending_stlye == '':
        print(f'{FINAL_INFO_COLOR}Autoclicker Stopped{RESET}')
    else:
        print(f'{process_ending_stlye}Autoclicker Stopped{RESET}')
    
    print('\n')
    
    end_error_style = get_style('ending/error prompts')
    print('\n')
    print('The ending/error prompts will look like this:')
    if end_error_style == '':
        print(f'{END_INFO_COLOR}Exiting Programm{RESET}')
    else:
        print(f'{end_error_style}Exiting Programm{RESET}')
    
    style_example(prompt_style, input_style, info_style, process_starting_stlye, process_ending_stlye, end_error_style)
    print('Press ENTER to continue...')
    input()
    
    print('\n')

    print('Saving styles to config...')
    save_styles_settings(prompt_style, input_style, info_style, process_starting_stlye, process_ending_stlye, end_error_style)
    print('Done saving styles to config')
    print('Restart app to see changes')
    
    print('\n')
    
    print('Press ENTER to continue...')
    input()
    
    sys.stdout.write("\033c")
    sys.stdout.flush()
    
    print(f"{FIRST_INFO_COLOR}Toggle autoclicker by pressing {toggle_key} key{RESET}")
    print(f"{FIRST_INFO_COLOR}Exit program by pressing {exit_key} key{RESET}")
    print(f"{FIRST_INFO_COLOR}Save your settings by pressing ` key{RESET}")
    print(f"{FIRST_INFO_COLOR}Change the style of the print messages by pressing . key{RESET}")

    lock_terminal()