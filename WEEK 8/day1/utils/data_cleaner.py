import json

def load_jsonl(path):
    data = []
    with open(path, "r") as f:
        for line in f:
            data.append(json.loads(line))
    return data


def clean_data(data):
    cleaned = []

    for item in data:
        # Remove empty fields
        if not item["instruction"] or not item["output"]:
            continue

        # Trim spaces
        item["instruction"] = item["instruction"].strip()
        item["input"] = item["input"].strip()
        item["output"] = item["output"].strip()

        cleaned.append(item)

    return cleaned


def save_jsonl(data, path):
    with open(path, "w") as f:
        for item in data:
            f.write(json.dumps(item) + "\n")


if __name__ == "__main__":
    train_data = load_jsonl("../data/train.jsonl")
    cleaned = clean_data(train_data)
    save_jsonl(cleaned, "../data/train_cleaned.jsonl")

    print("✅ Data cleaned and saved!")