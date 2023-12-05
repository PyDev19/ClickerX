# ClickerX

ClickerX is a terminal-based autoclicker written in Python. It allows users to automate mouse clicks at specified intervals.

## Warning: This app on linux only runs on a Xorg display

## Getting Started
To download and use ClickerX for linux follow the given steps below:
1. Download the tarball file from the [latest release](https://github.com/PyDev19/ClickerX/releases)
2. Extract the tarball to any directory you want and rename it to what you want
3. If you have a desktop enviorment that supports desktop icons then follow the steps bellow, if not then just run `launch.sh` from the terminal like so: `./launch.sh`
4. If you want to create a desktop shortcut for this app, then create a `ClickerX.desktop` file on the desktop.
5. Write in the desktop file like so:
    ```
    [Desktop Entry]
    Terminal=false
    Type=Application
    Name=ClickerX
    Exec=/path/to/application/folder/launch.sh
    Icon=/path/to/application/folder/icon.ico
    ```
6. Replace `/path/to/application/folder/` with the folder where you extracted the application tarball to. I recommend you put it somewhere inside the `home` folder.
7. After making the above changes, right click on the file and click `Allow Launching` if all the directories are correct then the icon of the app should appear on the desktop and if you run it, it should open a terminal window with the app running inside it. 

## Features

- Simulate mouse clicks at specified intervals.
- Adjust the click interval and duration according to your requirements.
- Choose between left, right, or middle mouse button clicks.
- Choose which key to press to start/stop autoclicker and exit the program
- Press '`' (backtick) to save your settings for future use
- Press '.' (dot) to change color and text decoration of prompts (saves in settings)
- Supports keyboard clicker to autoclick a key on your keyboard (saves in settings)

## Contributing

Contributions to ClickerX are always welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b my-new-feature`.
3. Make your changes and commit them: `git commit -am 'Add some feature'`.
4. Push your changes to the forked repository: `git push origin my-new-feature`.
5. Create a new Pull Request.

## License

ClickerX is licensed under the GNU-GPLv3 License. See the [LICENSE](LICENSE) file for more information.
