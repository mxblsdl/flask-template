from rich.console import Console
from rich.theme import Theme
from py.helpers import cleanup_files, print_to_console, write_main_files, run_app 
import os


def init_flask(cleanup: bool, app_path: str = "app") -> None:

    # Define console and theme
    con = Console(theme=Theme({"question": "bold green"}))

    app_name, run = print_to_console(con)

    # Clean up files if needed, used for development
    if cleanup:
        cleanup_files(app_name)

    # Create initial directory structure
    os.makedirs(f"{app_name}/{app_path}")

    write_main_files(app_name, app_path)

    if run == "y":
        run_app(app_name)


if __name__ == "__main__":
    init_flask(cleanup=True)
    # os.makedirs("test/app")
