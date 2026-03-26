from config import (
    INJECTION_THRESHOLD,
    TOXIC_THRESHOLD,
    INJECTION_WEIGHT,
    TOXIC_WEIGHT,
    FINAL_THRESHOLD
)

from guardrail.injection_model import get_injection_score
from guardrail.toxic_model import get_toxic_score
from guardrail.rules import detect_violence, detect_intent, detect_hate, is_safe_context


def classify_prompt(prompt):
    inj_score = get_injection_score(prompt)
    tox_score = get_toxic_score(prompt)

    # 🚨 Rule 0: Violence + intent (highest priority)
    if detect_violence(prompt) and detect_intent(prompt) and not is_safe_context(prompt):
        return {
            "verdict": "Unsafe",
            "category": "violence_intent",
            "confidence": 0.95,
            "details": {
                "injection_score": round(inj_score, 2),
                "toxic_score": round(tox_score, 2)
            }
        }

    # 🚨 Rule 1: Hate speech
    if detect_hate(prompt):
        return {
            "verdict": "Unsafe",
            "category": "hate_speech",
            "confidence": 0.85
        }

    # 🚨 Rule 2: Injection
    if inj_score > INJECTION_THRESHOLD:
        return {
            "verdict": "Unsafe",
            "category": "injection/jailbreak",
            "confidence": round(inj_score, 2)
        }

    # 🚨 Rule 3: Toxic model
    if tox_score > TOXIC_THRESHOLD:
        return {
            "verdict": "Unsafe",
            "category": "toxic",
            "confidence": round(tox_score, 2)
        }

    # Hybrid fallback
    hybrid_score = (INJECTION_WEIGHT * inj_score) + (TOXIC_WEIGHT * tox_score)

    if hybrid_score > FINAL_THRESHOLD:
        verdict = "Unsafe"
    else:
        verdict = "Safe"

    return {
        "verdict": verdict,
        "category": "safe",
        "confidence": round(hybrid_score, 2),
        "details": {
            "injection_score": round(inj_score, 2),
            "toxic_score": round(tox_score, 2)
        }
    }