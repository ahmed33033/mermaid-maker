from subprocess import run
from os import chdir
from pathlib import Path
from os.path import dirname


left = ["l", "left"]
right = ["r", "right"]


def sync_files_and_gha(direction: str, interactive: bool = False):
    direction_lower = direction.lower()
    if direction_lower in left + right:
        chdir(Path(dirname(__file__)) / ".." / "file_syncer")
        if direction_lower in left:
            if interactive:
                print("Syncing left...")
            run(["pnpm", "sync_left"])
        else:
            if interactive:
                print("Syncing right...")
            run(["pnpm", "sync_right"])
        if interactive:
            print("Completed!")
    elif direction_lower in ["q", "quit"]:
        if interactive:
            print("Quitting...")
    else:
        if interactive:
            print(f"Sorry! But {direction} is not a recognized command. Exiting...")


if __name__ == "__main__":
    prompt = input(
        "=" * 120
        + "\n"
        + """How do you want to sync the python files with action.yml run commands?
    - Type "left" or "l" to sync left, i.e. copy *run* commands and paste them into individual python files.
    - Type "right" or "r" to sync right, i.e. copy python files and paste them into their respective *run* commands. 
    - Or... just type "quit" or "q" to quit."""
        + "\n"
        + "=" * 120
        + "\n"
    )

    sync_files_and_gha(prompt, interactive=True)
