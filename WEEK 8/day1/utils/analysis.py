import json
import matplotlib.pyplot as plt

def load_data(path):
    data = []
    with open(path) as f:
        for line in f:
            data.append(json.loads(line))
    return data


def get_lengths(data):
    lengths = []
    for item in data:
        text = item["instruction"] + " " + item["input"] + " " + item["output"]
        lengths.append(len(text.split()))
    return lengths


# Load data
data = load_data("data/cleaned.jsonl")

print("\n===== DATA ANALYSIS START =====")
print(f"Total Samples (cleaned): {len(data)}")

# Get lengths
lengths = get_lengths(data)

# Basic stats
avg_len = sum(lengths) / len(lengths)
max_len = max(lengths)
min_len = min(lengths)

print(f"\nToken Stats:")
print(f"Average Length: {avg_len:.2f}")
print(f"Max Length: {max_len}")
print(f"Min Length: {min_len}")

# Histogram
plt.hist(lengths, bins=50)
plt.title("Token Length Distribution")
plt.xlabel("Token Length")
plt.ylabel("Frequency")
plt.savefig("length_dist.png")

print("\n Histogram saved as length_dist.png")


threshold = 40

filtered = [d for d, l in zip(data, lengths) if l < threshold]

print(f"\n Outlier Threshold: {threshold}")
print(f"Samples after removing outliers: {len(filtered)}")
print(f"Removed Samples: {len(data) - len(filtered)}")

# Save final
with open("data/final.jsonl", "w") as f:
    for item in filtered:
        f.write(json.dumps(item) + "\n")

print("\n Final dataset saved: data/final.jsonl")
print("===== DATA ANALYSIS COMPLETE =====\n")