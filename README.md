# Project ERYN

Personal AI Assistant

Version: 0.1.0

Developer:
Mashruf Mahmud Porosh

AI Partner:
ChatGPT

## Setup

Copy `.env.example` to `.env` and paste your actual API key into that file.

Your `.env` file should look like this once you replace the placeholder with your real secret:

```env
AI_BACKEND=openai
AI_API_KEY=sk-your-real-openai-key-goes-here
AI_OPENAI_MODEL=gpt-4o
AI_ANTHROPIC_MODEL=claude-3.5
AI_GOOGLE_MODEL=gemini-pro
AI_OPENAI_TEMPERATURE=0.7
AI_ANTHROPIC_TEMPERATURE=0.7
AI_GOOGLE_TEMPERATURE=0.7
```

### How to paste your key

1. Open `.env` in a text editor.
2. Find the line starting with `AI_API_KEY=`.
3. Replace the placeholder text with your real API key.
4. Save the file.

### Important

- `AI_API_KEY` must contain your backend's secret key.
- Choose `openai`, `anthropic`, or `google` with `AI_BACKEND`.
- Never commit `.env` to version control.

## Supported AI Backends

- `openai` — ChatGPT / OpenAI models
- `anthropic` — Claude
- `google` — Gemini
- `local` — fallback local backend

## Run

Use Python 3.11+ and run:

```bash
python main.py
```

## Notes

- ERYN will use the `.env` file for backend selection and API key.
- If a backend package is missing, the system will fall back to a friendly error message and you can switch to a provider you have installed.
