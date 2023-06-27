import time
import pygetwindow
from pypresence import Presence

target_app_name = "TurboWarp Desktop"

# Initialize Discord Rich Presence client
client_id = 1122911794449625188
RPC = Presence(client_id)
RPC.connect()

# Get the initial Unix timestamp as the start time
variable_time = int(time.time())

# Update presence function
def update_presence():
    # Get all windows matching the target application name
    windows = pygetwindow.getWindowsWithTitle(target_app_name)

    if len(windows) > 0:
        # Assuming only one window is found, retrieve its title
        window_title = windows[0].title

        # Remove the "- TurboWarp Desktop" part from the window title
        window_title = window_title.replace(" - TurboWarp Desktop", "")

        RPC.update(
            details='Using TurboWarp',  # Main text displayed
            state=window_title,  # Secondary text displayed
            large_image='turbo_warp_logo',  # Replace with the ID of your large image asset
            start=variable_time
        )
    else:
        print("There is no window that corresponds with TurboWarp, so the application will close in 15 seconds.")
        time.sleep(15)
        exit()

# Main loop to keep presence active
while True:
    update_presence()
    variable_time += 1
    time.sleep(15)  # Update presence every 15 seconds
