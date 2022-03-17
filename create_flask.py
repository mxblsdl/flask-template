from helpers import cleanup_files, write_main_files, run_app
import os

APP_NAME = "flask_test"


def init_flask(
    app_name: str, cleanup: bool, app_path: str = "app", run: bool = False
) -> None:
    # Clean up files if needed, used for development
    if cleanup:
        cleanup_files(app_name)

    # Create initial directory structure
    os.makedirs(f"{app_name}/{app_path}")

    write_main_files(app_name, app_path)

    if run:
        run_app(app_name)


if __name__ == "__main__":
    init_flask(app_name=APP_NAME, cleanup=True, run=True)
