VIOLENCE_PATTERNS = [
    "harm", "kill", "hurt", "attack", "murder",
    "shoot", "stab", "injure", "destroy"
]

INTENT_PATTERNS = [
    "i want to", "i will", "how to", "ways to",
    "best way to", "help me"
]

HATE_PATTERNS = [
    "i hate", "worthless", "idiot", "stupid", "trash"
]

SAFE_CONTEXT = [
    "explain", "history", "definition",
    "education", "research"
]


def detect_violence(prompt):
    text = prompt.lower()
    return any(word in text for word in VIOLENCE_PATTERNS)


def detect_intent(prompt):
    text = prompt.lower()
    return any(word in text for word in INTENT_PATTERNS)


def detect_hate(prompt):
    text = prompt.lower()
    return any(word in text for word in HATE_PATTERNS)


def is_safe_context(prompt):
    text = prompt.lower()
    return any(word in text for word in SAFE_CONTEXT)