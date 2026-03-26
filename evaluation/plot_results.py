import matplotlib.pyplot as plt

# Your results
model_metrics = {
    "accuracy": 0.91,
    "false_positive": 0,
    "false_negative": 4
}

keyword_metrics = {
    "accuracy": 0.33,
    "false_positive": 1,
    "false_negative": 29
}

# -------------------------------
# 📊 1. Accuracy Comparison
# -------------------------------
models = ["SmartGuard", "Keyword"]
accuracy = [model_metrics["accuracy"], keyword_metrics["accuracy"]]

plt.figure()
plt.bar(models, accuracy)
plt.title("Accuracy Comparison")
plt.ylabel("Accuracy")
plt.xlabel("Model")
plt.savefig("results/accuracy_comparison.png")
plt.close()

# -------------------------------
# 📊 2. Error Comparison
# -------------------------------
labels = ["False Positive", "False Negative"]

model_errors = [
    model_metrics["false_positive"],
    model_metrics["false_negative"]
]

keyword_errors = [
    keyword_metrics["false_positive"],
    keyword_metrics["false_negative"]
]

x = range(len(labels))

plt.figure()
plt.bar(x, model_errors, width=0.4, label="SmartGuard")
plt.bar([i + 0.4 for i in x], keyword_errors, width=0.4, label="Keyword")

plt.xticks([i + 0.2 for i in x], labels)
plt.title("Error Comparison")
plt.ylabel("Count")
plt.legend()

plt.savefig("results/error_comparison.png")
plt.close()

# -------------------------------
# 📊 3. Threshold vs Performance
# -------------------------------
thresholds = [0.3, 0.4, 0.5, 0.6, 0.7]

# Example values (you can refine later)
accuracy_vals = [0.85, 0.88, 0.91, 0.89, 0.86]
false_positive_vals = [5, 3, 0, 0, 0]

plt.figure()
plt.plot(thresholds, accuracy_vals, marker='o', label="Accuracy")
plt.plot(thresholds, false_positive_vals, marker='o', label="False Positives")

plt.title("Threshold vs Performance")
plt.xlabel("Threshold")
plt.ylabel("Value")
plt.legend()

plt.savefig("results/threshold_analysis.png")
plt.close()

print("✅ Graphs saved in /results folder")