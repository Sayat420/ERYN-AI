"""
=========================================================
PROJECT ERYN
Main Configuration File
=========================================================
"""

import os
from pathlib import Path

try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = None

# =========================================================
# PROJECT INFORMATION
# =========================================================

PROJECT_NAME = "ERYN"

VERSION = "0.1.0"

OWNER = "Mashruf Mahmud Porosh"

AI_NAME = "ERYN"

NAME = AI_NAME

WAKE_WORD = "ERYN"

LANGUAGE = "auto"

VOICE_STYLE = "soft"
VOICE_SPEED = 175

DEBUG = True

DEVELOPER_MODE = True

# =========================================================
# ROOT PATH
# =========================================================

ROOT_DIR = Path(__file__).resolve().parent.parent

if load_dotenv is not None:
    load_dotenv(ROOT_DIR / ".env", override=True)

# =========================================================
# FOLDERS
# =========================================================

ASSETS_DIR = ROOT_DIR / "assets"

DATA_DIR = ROOT_DIR / "data"

DOCS_DIR = ROOT_DIR / "docs"

LOGS_DIR = ROOT_DIR / "logs"

MODELS_DIR = ROOT_DIR / "models"

PLUGINS_DIR = ROOT_DIR / "plugins"

SRC_DIR = ROOT_DIR / "src"

TESTS_DIR = ROOT_DIR / "tests"

CONFIG_DIR = ROOT_DIR / "config"

# =========================================================
# DATABASE
# =========================================================

DATABASE_NAME = "eryn.db"

DATABASE_PATH = DATA_DIR / DATABASE_NAME

# =========================================================
# LOG FILE
# =========================================================

LOG_FILE = LOGS_DIR / "eryn.log"

# =========================================================
# MEMORY
# =========================================================

MEMORY_FOLDER = DATA_DIR / "memory"

SHORT_TERM_MEMORY = MEMORY_FOLDER / "short_term.json"

LONG_TERM_MEMORY = MEMORY_FOLDER / "long_term.json"

# =========================================================
# AI
# =========================================================

DEFAULT_AI_MODEL = "openai-gpt"

AI_BACKEND = os.getenv("AI_BACKEND", "openai").lower()
AI_API_KEY = os.getenv("AI_API_KEY", "").strip()

if not AI_BACKEND:
    AI_BACKEND = "openai"

if AI_BACKEND == "openai" and not AI_API_KEY:
    AI_BACKEND = "local"

if AI_BACKEND == "github" and not AI_API_KEY:
    AI_BACKEND = "local"
AI_OPENAI_MODEL = os.getenv("AI_OPENAI_MODEL", "gpt-4o")
AI_OPENAI_MODELS = [
    model.strip()
    for model in os.getenv(
        "AI_OPENAI_MODELS", "gpt-4o,gpt-4o-mini,gpt-3.5-turbo"
    ).split(",")
    if model.strip()
]
AI_OPENAI_TEMPERATURE = float(os.getenv("AI_OPENAI_TEMPERATURE", "0.7"))
AI_ANTHROPIC_MODEL = os.getenv("AI_ANTHROPIC_MODEL", "claude-3.5")
AI_ANTHROPIC_MODELS = [
    model.strip()
    for model in os.getenv("AI_ANTHROPIC_MODELS", "claude-3.5,claude-2.1").split(",")
    if model.strip()
]
AI_ANTHROPIC_TEMPERATURE = float(os.getenv("AI_ANTHROPIC_TEMPERATURE", "0.7"))
AI_GOOGLE_MODEL = os.getenv("AI_GOOGLE_MODEL", "gemini-pro")
AI_GOOGLE_MODELS = [
    model.strip()
    for model in os.getenv("AI_GOOGLE_MODELS", "gemini-pro,gemini-medium").split(",")
    if model.strip()
]
AI_GOOGLE_TEMPERATURE = float(os.getenv("AI_GOOGLE_TEMPERATURE", "0.7"))

SUPPORTED_AI_BACKENDS = ("openai", "anthropic", "google", "github", "local")

ENABLE_MEMORY = True

ENABLE_VISION = False

ENABLE_INTERNET = False

ENABLE_AUTONOMY = False

ENABLE_OVERLAY = False

# =========================================================
# DEVICE
# =========================================================

ALLOW_CAMERA = True

ALLOW_MICROPHONE = True

ALLOW_SPEAKER = True

ALLOW_FILE_ACCESS = True

ALLOW_DESKTOP_CONTROL = False

ALLOW_ANDROID_CONTROL = False

# =========================================================
# STARTUP MESSAGE
# =========================================================

STARTUP_MESSAGE = (
    "Hello Boss. "
    "Eryn has been initialized successfully."
)
