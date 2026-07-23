from subprocess import run
from os import environ


def setup_pkg_manager(pkg_manager):
    if pkg_manager == "npm":
        print("Nothing to setup")
    elif pkg_manager == "pnpm":
        run(["pnpm", "config", "set", "--location=project", "strictDepBuilds", "false"])
    elif pkg_manager == "yarn":
        print("Nothing to setup")
    elif pkg_manager == "bun":
        print("Nothing to setup")
    else:
        run(["exit", "1"])


if __name__ == "__main__":
    setup_pkg_manager(environ["PKG_MANAGER"])
