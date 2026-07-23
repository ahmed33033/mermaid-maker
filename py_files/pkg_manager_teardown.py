from subprocess import run
from os import environ


def teardown_pkg_manager(pkg_manager):
    if pkg_manager == "npm":
        print("Nothing to teardown")
    elif pkg_manager == "pnpm":
        run(["pnpm", "config", "set", "--location=project", "strictDepBuilds", "true"])
    elif pkg_manager == "yarn":
        print("Nothing to teardown")
    elif pkg_manager == "bun":
        print("Nothing to teardown")
    else:
        run(["exit", "1"])


if __name__ == "__main__":
    teardown_pkg_manager(environ["PKG_MANAGER"])
