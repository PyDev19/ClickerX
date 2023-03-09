# AutoClicker
A simple terminal based autoclicker

## Latest Changes:
- Added doc string for some functions and classes to communicate the necessary information about the function to users who may need to use or modify it.
- Added colors using ANSI escape codes and enabling virtual terminal processing (vtp).
- Created a file with constants for all ANSI escape codes to decorate text to make it easier to identify which print statement has which color and other decorations

## Features of AutoClicker:
- Basically ever feature that an autoclicker already has.
- Terminal based meaning the autoclicker runs in a terminal window if you run the exe, this makes program size very small (about 10 mb).

## Future plans:
- ~~Add colors to print statements to make the app look better~~ (DONE!)
- Add a keyboard autoclicker mode, which will automatically press one key for you (I don't know where that would be usefull but still).
- Add a option where you can use your mouse to toggle the autoclicker (mainly for mouses that have sidebuttons)
- Add a config option that will allow you to save your settings and open them every time you run the app, so you do not have to enter the same thing over and over again.

## Supported Platforms:
- Windows
- That's it, I will try to get support for other platforms but right now I have made this app focused mainly with windows in mind.

## Some extra info:
- You don't need need to unistall previous version of this app to install a new version.
- If you run the installer with an older version installed it will automatically update it to a new verion.
- Thank Inno Setup!

## Customization:
- If you want you can download the source code and download the required libraries from `requirements.txt`
- Then you can customize the way it works or the colors of print statements using the new `constants.py` which contains constant values for every text decoration ANSI escape codes that can be used in print statements.
- If you want to distribute your own customized version of this app make sure to read the `LICENSE.md` to know what to do and not do, and crediting would also be nice.
