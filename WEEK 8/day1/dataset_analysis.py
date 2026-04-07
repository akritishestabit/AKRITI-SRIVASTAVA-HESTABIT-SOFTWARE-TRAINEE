import json
import matplotlib.pyplot as plt

def load_jsonl(path):
    data = []
    with open(path, "r") as f:
        for line in f:
            data.append(json.loads(line))
    return data


def analyze_lengths(data):
    lengths = []

    for item in data:
        text = item["instruction"] + " " + item["input"] + " " + item["output"]
        lengths.append(len(text.split()))

    return lengths


def plot_distribution(lengths):
    plt.hist(lengths, bins=20)
    plt.title("Token Length Distribution")
    plt.xlabel("Length")
    plt.ylabel("Frequency")
    plt.show()


if __name__ == "__main__":
    data = load_jsonl("data/train.jsonl")
    lengths = analyze_lengths(data)

    print("Min length:", min(lengths))
    print("Max length:", max(lengths))
    print("Average length:", sum(lengths)/len(lengths))

    plot_distribution(lengths)