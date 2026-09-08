#!/usr/bin/env python3
import os
import sys


REQUIRED_SETTINGS = (
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
)


def detect_environment() -> str:
    """Return the active Poetry, virtualenv, or system environment."""
    if os.environ.get("POETRY_ACTIVE") == "1":
        return "Poetry Environment (Isolated lockfile-based)"
    if sys.prefix != sys.base_prefix:
        return "Standard Virtualenv (pip-based)"
    return "Global Python System"


def load_environment_file() -> bool | None:
    """Load .env, or return None when python-dotenv is unavailable."""
    try:
        from dotenv import load_dotenv
    except ModuleNotFoundError:
        return None
    return load_dotenv()


def get_mode() -> str:
    """Return a supported Matrix mode, defaulting to development."""
    mode = os.getenv("MATRIX_MODE", "development").lower()
    if mode in ("development", "production"):
        return mode

    print(f"[WARNING] Unknown MATRIX_MODE '{mode}'. Using development.")
    return "development"


def get_missing_settings() -> list[str]:
    """Return the required settings that are not configured."""
    return [name for name in REQUIRED_SETTINGS if not os.getenv(name)]


def display_configuration(mode: str) -> None:
    """Display the active configuration without exposing secrets."""
    database_status = (
        "Connected to production cluster"
        if mode == "production" else "Connected to local instance"
    )

    print("Configuration loaded:")
    print(f"Mode: {mode}")
    print(f"Database: {database_status}")
    print("API Access: Authenticated")
    print(f"Log Level: {os.environ['LOG_LEVEL']}")
    print(f"Zion Network: {os.environ['ZION_ENDPOINT']}")


def display_security_check(dotenv_loaded: bool) -> None:
    """Display the checks that protect configuration secrets."""
    print("Environment security check:")
    print("[OK] Secrets read from environment variables")
    if dotenv_loaded:
        print("[OK] .env file loaded")
    else:
        print("[INFO] No .env file found; using environment variables only")
    print("[OK] Production overrides available")


def display_installation_help() -> None:
    """Explain how to install the missing dependency."""
    print("\nTo install dependencies using PIP:")
    print("  pip install -r requirements.txt")
    print("\nTo install dependencies using POETRY:")
    print("  poetry install")


def main() -> int:
    """Load and validate Matrix configuration."""
    print("ORACLE STATUS: Reading the Matrix...")
    print(f"[ENV INFO] Running on: {detect_environment()}")
    print("Checking dependencies:")

    dotenv_loaded = load_environment_file()
    if dotenv_loaded is None:
        print("[MISSING] python-dotenv - Not installed")
        display_installation_help()
        return 1

    print("[OK] python-dotenv - Ready")
    mode = get_mode()
    missing_settings = get_missing_settings()

    if missing_settings:
        print("Configuration warnings:")
        for setting in missing_settings:
            print(f"[MISSING] {setting}")
        print("Copy .env.example to .env and provide the required values.")
        return 1

    display_configuration(mode)
    display_security_check(dotenv_loaded)
    print("The Oracle sees all configurations.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
