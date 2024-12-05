# config/settings.py

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SETTINGS = {
    "DEBUG": True,
    "LOG_FILE": os.path.join(BASE_DIR, "../logs/app.log"),
    "KNOWLEDGE_BASE_DIR": os.path.join(BASE_DIR, "../knowledge_base/"),
}
