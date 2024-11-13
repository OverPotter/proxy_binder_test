import os.path
from pathlib import Path

INPUT_DIR = Path(__file__).resolve().parents[1] / "input"
OUTPUT_DIR = Path(__file__).resolve().parents[1] / "output"

USER_FILE = "users.txt"
PROXY_FILE = "proxies.txt"
OUTPUT_FILE = "output.txt"

USER_FILE_PATH = os.path.join(INPUT_DIR, USER_FILE)
PROXY_FILE_PATH = os.path.join(INPUT_DIR, PROXY_FILE)
OUTPUT_FILE_PATH = os.path.join(INPUT_DIR, OUTPUT_FILE)

ENV_PATH = Path(__file__).resolve().parents[1] / "docker" / "backend" / ".env"
