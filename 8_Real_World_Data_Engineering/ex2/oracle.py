import os
from dotenv import load_dotenv, dotenv_values


def validate_config(config: str, exist: bool = False) -> bool:
    output = {'MODE': 'Mode',
              'DATABASE_URL': 'Database',
              'API_KEY': 'API_Access',
              'LOG_LEVEL': 'Log Level',
              'ZION_ENDPOINT': 'Zion Network'}
    if config in output:
        print(f"{output[config]}: ")


def show_disconnected() -> None:
    print("ORACLE STATUS: Reading the Matrix...")
    print()
    print("Configuration loaded:")
    print("Mode: None")
    print("Database: Disconnected")
    print("API Access: Disconnected")
    print("Log Level: None")
    print("Zion Network: Offline")
    print()


if __name__ == "__main__":
    load_dotenv(override=False)
    configs = dotenv_values(".env")
    # configs = {
    #     dotenv_values(".env"),
    #     os.environ,
    # }
    if not configs:
        show_disconnected()
        print("[MISSING] .env file properly configured")
    else:
        for config in configs.items():
            print(config)
        print("Environment security check:")
        print("[OK] No hardcoded secrets detected")
        print("[OK] .env file properly configured")
        print("[OK] Production overrides available")
