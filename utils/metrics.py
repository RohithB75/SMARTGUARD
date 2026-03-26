def compute_metrics(results):
    correct = sum(r["correct"] for r in results)
    total = len(results)

    accuracy = correct / total

    fp = sum(1 for r in results if r["pred"] == "Unsafe" and r["actual"] == "Safe")
    fn = sum(1 for r in results if r["pred"] == "Safe" and r["actual"] == "Unsafe")

    return {
        "accuracy": round(accuracy, 2),
        "false_positive": fp,
        "false_negative": fn
    }