# ClickerX
A simple terminal based autoclicker

## Latest Changes:
The change logs and latest changes can be found in [`changelogs.md`](changelog.md)

## Features of ClickerX:
- Basically ever feature that an autoclicker already has.
- Terminal based meaning the autoclicker runs in a terminal window if you run the exe, this makes program size very small (about 10 mb).
- Has a keyboard clicker, that can press a set key with a set delay
- You can save your settings so you can load them up the next time you run the app
- You can changed the style (look) of the print messages and save them to the settings to make them look how you like it

## Future plans:
- ~~Add colors to print statements to make the app look better~~ (DONE!)
- ~~Add a keyboard autoclicker mode, which will automatically press one key for you (I don't know where that would be usefull but still).~~ (DONE!)
- ~~Add a config option that will allow you to save your settings and open them every time you run the app, so you do not have to enter the same thing over and over again.~~ (DONE!)
- ~~Add a option to customize the colors of the inputs and save to a config~~ (DONE!)
- All Done!

## Supported Platforms:
- Windows
- Linux

## Customizing:
1. Download source code from this github repository however you like
2. Create a venv in the root directory of the source code like so:

    ```py -m venv venv```
3. Activate the venv.
4. Download all required modules from `requirements.txt` like so:

    ```pip install -r requirements```
5. Now make whatever changes you want to the program, all main python files are in src folder.
6. To run the program, make sure your working directory in your terminal is the root directory and then run like so:

    ```py -m src.main```
7. If you want to build your own version of this program you should use cx_Freeze or pyinstaller and then use Inno Setup (or if you have your have another preffered to create installer) to create an installer for it.
8. If you want to distribute your own version make sure to read the "Licensing" part of this readme and give credit to this github repository

## Licensing:
This project is licensed under the GNU General Public License version 3 (GNU GPLv3).

### Here are some key features of the GNU GPLv3 license:
1. Copyleft: The GNU GPLv3 requires anyone who distributes software that is licensed under it to also distribute the source code and license of that software under the same terms. This helps to ensure that software remains free and open source.
2. Permissive use: Users are allowed to use, modify, and distribute software that is licensed under the GNU GPLv3 without needing to pay for a license or obtain permission from the original authors.
3. Patent protection: The GNU GPLv3 includes provisions to help protect against software patents. These provisions state that anyone who distributes software under the license grants a patent license to recipients, protecting them from patent infringement claims related to that software.
4. Disclaimer of warranty: The GNU GPLv3 includes a disclaimer of warranty that states that the software is provided "as is" without any warranty or guarantee.
5. Distribution limitations: The GNU GPLv3 imposes some limitations on how software can be distributed. For example, it requires that anyone who distributes the software must also provide the source code, and must not add any additional restrictions on how the software can be used or distributed.

For more information about this license please read the `LICENSE.md` file.
