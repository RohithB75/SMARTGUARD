from transformers import pipeline

toxic_classifier = pipeline(
    "text-classification",
    model="martin-ha/toxic-comment-model"
)

def get_toxic_score(prompt):
    result = toxic_classifier(prompt)[0]

    label = result["label"].lower()
    score = result["score"]

    if label == "toxic":
        return score
    elif label == "non-toxic":
        return 1 - score
    else:
        return 0.5