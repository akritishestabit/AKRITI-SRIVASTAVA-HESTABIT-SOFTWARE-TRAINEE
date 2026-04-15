import json
import random

def load_data(path):
    data = []
    with open(path, "r") as f:
        for line in f:
            data.append(json.loads(line))
    return data

def save_data(data, path):
    with open(path, "w") as f:
        for item in data:
            f.write(json.dumps(item) + "\n")


data = load_data("data/final.jsonl")


random.shuffle(data)

# Split
split = int(0.9 * len(data))

train = data[:split]
val = data[split:]

# Save
save_data(train, "data/train.jsonl")
save_data(val, "data/val.jsonl")

print("Train/Val split done!")