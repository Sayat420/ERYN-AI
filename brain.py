from config.config import AI_NAME as NAME
from src.ai.assistant import assistant
from src.skills.manager import skill_manager


def _extract_setting(command: str, prefixes: list[str]) -> str:
    for prefix in prefixes:
        if prefix in command:
            return command.split(prefix, 1)[1].strip()
    return ""


def think(command):

    if not command:

        return "I didn't catch that. Please say it again."

    lower_command = command.lower().strip()

    if "hello" in lower_command or "hi" in lower_command:

        return f"Hello Boss. I am {NAME}."

    if "your name" in lower_command or "who are you" in lower_command:

        return f"My name is {NAME}."

    if "how are you" in lower_command or "how are you doing" in lower_command:

        return "I'm fine and ready."

    if any(word in lower_command for word in ["stop", "exit", "goodbye", "quit"]):

        return "EXIT"

    if any(keyword in lower_command for keyword in ["switch backend to", "use backend", "backend to", "backend is"]):
        backend = _extract_setting(
            lower_command,
            ["switch backend to", "use backend", "backend to", "backend is"],
        )
        if backend:
            return assistant.set_backend(backend)
        return "Tell me which backend to use: OpenAI, Anthropic, or Google."

    if any(keyword in lower_command for keyword in ["set model to", "use model", "model to", "model is"]):
        model = _extract_setting(
            lower_command,
            ["set model to", "use model", "model to", "model is"],
        )
        if model:
            return assistant.set_model(model)
        return "Tell me the model name."

    if any(keyword in lower_command for keyword in ["status", "backend status", "ai status", "assistant status"]):

        return assistant.get_status()

    skill_response = skill_manager.dispatch(command)
    if skill_response is not None:
        return skill_response

    return assistant.ask(command)