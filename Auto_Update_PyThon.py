# Name: KrAizoT
# Create: 02/19/26
# Modify: 09/21/26
# Com: Auto Update - Git File for repo https://github.com/KrAizoT/wallpaper_GIT

# --- CODE START ---

import subprocess
from datetime import datetime

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

subprocess.run(["git", "add", "."], check=True)

# Check whether anything is staged
status = subprocess.run(
    ["git", "status", "--porcelain"],
    capture_output=True, text=True, check=True
)

if status.stdout.strip():
    subprocess.run(["git", "commit", "-m", f"autoupdate {timestamp}"], check=True)
    subprocess.run(["git", "push"], check=True)
    print("Changes committed and pushed.")
else:
    print("Nothing to commit.")

# --- CODE END ---