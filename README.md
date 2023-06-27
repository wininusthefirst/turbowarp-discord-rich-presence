# TurboWarp Rich Presence for Discord
As the name states, this Python script allows Rich Presence to be integrated with TurboWarp. For every release, there will be 3 versions available: the .pkg (macOS; Universal), .exe (Windows 32/64 bit) and the actual script that is being executed (.py).
This application utilizes various Python libraries such as **pygetwindow**, **time** and **pypresence**. The app was complied using the **pyinstaller** libary.

# How does this application work?
First, the script gets the window title of the TurboWarp window. It will most likely look something like this: "Project - TurboWarp Desktop". **If no TurboWarp windows are detected, the application will display an error that will look something like this: "No windows corresponding to TurboWarp were detected. The application will close in 15 seconds.**"
Then, it connects to Discord and gets time data. After that, it trims the "- TurboWarp Desktop" out of the name, so when it's displayed on Discord, it will only contain the filename.
After that, it continues to update Discord every 15 seconds, and will close itself when it detects that you closed TurboWarp.

# Known Issues
Since this application isn't attached to TurboWarp, you have to start it every time you open TurboWarp, which can get annoying. A fix for that will be coming soon.
