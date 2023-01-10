import os
from pathlib import Path

from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parent.parent
print(ROOT_DIR)
dotenv_path = ROOT_DIR / '.env'

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
else:
    raise Exception('.env-файл со значениями переменных окружения не найден!')