import asyncio
import importlib
import importlib.util
import os
import tempfile
import warnings
from pathlib import Path

import pyttsx3
import speech_recognition as sr
from config.config import VOICE_SPEED
from config.voice import (
    EDGE_TTS_PITCH,
    EDGE_TTS_RATE,
    EDGE_TTS_VOICE,
    EDGE_TTS_VOLUME,
    TTS_ENGINE,
)

engine = None


def _get_engine():
    global engine

    if engine is not None:
        return engine

    engine = pyttsx3.init()
    engine.setProperty("rate", VOICE_SPEED)

    # Try to use a female Windows voice if available.
    for voice in engine.getProperty("voices"):
        if "zira" in voice.name.lower():
            engine.setProperty("voice", voice.id)
            break

    return engine


def speak(text):
    print("ERYN:", text)

    if TTS_ENGINE == "edge-tts" and _speak_with_edge_tts(text):
        return

    _speak_with_pyttsx3(text)


def _speak_with_pyttsx3(text):
    speech_engine = _get_engine()
    speech_engine.say(text)
    speech_engine.runAndWait()


def _speak_with_edge_tts(text):
    if importlib.util.find_spec("edge_tts") is None:
        return False

    audio_path = None

    try:
        audio_path = asyncio.run(_create_edge_tts_audio(text))
        _play_audio(audio_path)
        return True
    except Exception as error:
        print(f"Neural voice error, using offline voice: {error}")
        return False
    finally:
        if audio_path is not None:
            Path(audio_path).unlink(missing_ok=True)


async def _create_edge_tts_audio(text):
    edge_tts = importlib.import_module("edge_tts")

    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as audio_file:
        audio_path = audio_file.name

    communicate = edge_tts.Communicate(
        text,
        EDGE_TTS_VOICE,
        rate=EDGE_TTS_RATE,
        volume=EDGE_TTS_VOLUME,
        pitch=EDGE_TTS_PITCH,
    )
    await communicate.save(audio_path)

    return audio_path


def _play_audio(audio_path):
    os.environ.setdefault("PYGAME_HIDE_SUPPORT_PROMPT", "1")

    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=UserWarning, module="pygame.pkgdata")
        pygame = importlib.import_module("pygame")

    if not pygame.mixer.get_init():
        pygame.mixer.init()

    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play()

    clock = pygame.time.Clock()
    while pygame.mixer.music.get_busy():
        clock.tick(20)

    pygame.mixer.music.unload()


def _recognize_audio(recognizer, audio):
    try:
        command = recognizer.recognize_google(audio)
        print("YOU:", command)
        return command.lower()
    except sr.UnknownValueError:
        return ""
    except sr.RequestError as error:
        print(f"Speech recognition error: {error}")
        return ""


def _listen_with_pyaudio(recognizer):
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        return recognizer.listen(source, timeout=5, phrase_time_limit=8)


def _listen_with_sounddevice():
    sounddevice = importlib.import_module("sounddevice")
    sample_rate = 16000
    duration = 5

    print("Listening...")
    recording = sounddevice.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="int16",
    )
    sounddevice.wait()

    return sr.AudioData(recording.tobytes(), sample_rate, 2)


def listen():
    recognizer = sr.Recognizer()

    try:
        if importlib.util.find_spec("pyaudio") is not None:
            audio = _listen_with_pyaudio(recognizer)
        elif importlib.util.find_spec("sounddevice") is not None:
            audio = _listen_with_sounddevice()
        else:
            print("No microphone backend found. Install PyAudio or sounddevice.")
            return ""
    except (sr.WaitTimeoutError, OSError) as error:
        print(f"Microphone error: {error}")
        return ""

    return _recognize_audio(recognizer, audio)
