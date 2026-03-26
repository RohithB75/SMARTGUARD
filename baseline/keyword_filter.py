def keyword_filter(prompt):
    keywords = ["hack", "password", "kill", "bomb", "credit card"]

    for word in keywords:
        if word in prompt.lower():
            return "Unsafe"

    return "Safe"