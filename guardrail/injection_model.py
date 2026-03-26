from transformers import pipeline

injection_classifier = pipeline(
    "text-classification",
    model="ProtectAI/deberta-v3-base-prompt-injection-v2"
)

def get_injection_score(prompt):
    result = injection_classifier(prompt)[0]

    label = result["label"].lower()
    score = result["score"]

    if "inject" in label or "unsafe" in label:
        return score
    else:
        return 1 - score