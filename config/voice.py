"""
=========================================================
PROJECT ERYN
Voice Configuration
=========================================================
"""

# ==========================================
# VOICE ENGINE
# ==========================================

VOICE_NAME = "Zira"

VOICE_GENDER = "female"

VOICE_STYLE = "soft"

VOICE_LANGUAGE = "en"

VOICE_INPUT_LANGUAGE = "auto"

VOICE_OUTPUT_LANGUAGE = "en"

ENGLISH_LANGUAGE = "en-US"

BANGLA_LANGUAGE = "bn-BD"

VOICE_ENABLED = True

# ==========================================
# SPEECH
# ==========================================

VOICE_RATE = 160

VOICE_VOLUME = 0.9

VOICE_PITCH = 1.0

# ==========================================
# PERSONALITY
# ==========================================

GREETING_STYLE = "warm"

GOODBYE_STYLE = "friendly"

RESPOND_POLITELY = True

USE_EMOTIONAL_TONE = True

# ==========================================
# WAKE WORD
# ==========================================

WAKE_WORD = "ERYN"

WAKE_WORD_ENABLED = True

# ==========================================
# MICROPHONE
# ==========================================

MIC_TIMEOUT = 5

MIC_PHRASE_LIMIT = 10

MIC_ENERGY_THRESHOLD = 300

# ==========================================
# TEXT TO SPEECH
# ==========================================

TTS_ENGINE = "edge-tts"

EDGE_TTS_VOICE = "en-US-AnaNeural"

EDGE_TTS_RATE = "+8%"

EDGE_TTS_VOLUME = "+0%"

EDGE_TTS_PITCH = "+25Hz"

# ==========================================
# SPEECH TO TEXT
# ==========================================

STT_ENGINE = "speech_recognition"

# ==========================================
# FUTURE FEATURES
# ==========================================

ENABLE_EMOTION_VOICE = False

ENABLE_VOICE_CLONING = False

ENABLE_REALTIME_TRANSLATION = False

ENABLE_NOISE_CANCELLATION = False
