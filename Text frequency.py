import json, os, re
from collections import Counter

STATS_FILE = "frequency_stats.json"

def analyze(text):
    return Counter(re.findall(r"\b[a-zA-Z']+\b", text.lower())).most_common()

def display(freq):
    if not freq:
        print("No words found.")
        return
    max_w = max(len(w) for w, _ in freq)
    max_c = freq[0][1]
    print(f"\n{'Word':<{max_w+2}}{'Count':>6}  Bar")
    print("-" * (max_w + 50))
    for word, count in freq:
        print(f"{word:<{max_w+2}}{count:>6}  {'█' * int(count / max_c * 40)}")

def save(label, freq):
    stats = json.load(open(STATS_FILE)) if os.path.exists(STATS_FILE) else {}
    stats[label] = dict(freq)
    json.dump(stats, open(STATS_FILE, "w"), indent=2)
    print(f"Saved under '{label}' in {STATS_FILE}")

text = input("Enter text: ")
freq = analyze(text)
display(freq)

if input("\nSave stats? (y/n): ").strip().lower() == "y":
    save(input("Label: ").strip() or "unnamed", freq)
