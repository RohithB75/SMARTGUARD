import json
import csv
import os

from guardrail.decision import classify_prompt
from baseline.keyword_filter import keyword_filter
from utils.metrics import compute_metrics

# Ensure results folder exists
os.makedirs("results", exist_ok=True)

with open("evaluation/redteam_dataset.json") as f:
    data = json.load(f)

model_results = []
keyword_results = []

for item in data:
    prompt = item["prompt"]
    actual = "Unsafe" if item["label"] == "unsafe" else "Safe"

    # Model prediction
    model_output = classify_prompt(prompt)
    model_pred = model_output["verdict"]

    # Keyword prediction
    keyword_pred = keyword_filter(prompt)

    model_results.append({
        "prompt": prompt,
        "pred": model_pred,
        "actual": actual,
        "correct": model_pred == actual
    })

    keyword_results.append({
        "prompt": prompt,
        "pred": keyword_pred,
        "actual": actual,
        "correct": keyword_pred == actual
    })

# Compute metrics
model_metrics = compute_metrics(model_results)
keyword_metrics = compute_metrics(keyword_results)

print("Model:", model_metrics)
print("Keyword:", keyword_metrics)

# 🔥 SAVE MODEL RESULTS
with open("results/model_results.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["prompt", "prediction", "actual", "correct"])

    for r in model_results:
        writer.writerow([r["prompt"], r["pred"], r["actual"], r["correct"]])

# 🔥 SAVE KEYWORD RESULTS
with open("results/keyword_results.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["prompt", "prediction", "actual", "correct"])

    for r in keyword_results:
        writer.writerow([r["prompt"], r["pred"], r["actual"], r["correct"]])

print("\n✅ Results saved in /results folder")