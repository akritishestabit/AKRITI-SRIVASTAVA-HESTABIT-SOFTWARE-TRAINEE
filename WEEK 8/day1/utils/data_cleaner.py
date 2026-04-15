import json

def load_data(path):
    data = []
    with open(path, "r") as f:
        for line in f:
            data.append(json.loads(line))
    return data


def clean_data(data):
    cleaned = []

    bad_outputs = ["ok", "yes", "no", "done", "n/a", "none", "1", "0"]

    for item in data:
        instruction = item.get("instruction", "").strip()
        input_text = item.get("input", "").strip()
        output = item.get("output", "").strip()

        if not instruction or not output:
            continue

        if output.lower() in bad_outputs:
            continue

        if len(output.split()) < 2 and "extract" not in instruction.lower():
            continue

        if len(input_text.split()) < 2:
            continue

        cleaned.append(item)

    return cleaned   


def save_data(data, path):
    with open(path, "w") as f:
        for item in data:
            f.write(json.dumps(item) + "\n")


if __name__ == "__main__":
    data = load_data("data/raw.jsonl")
    cleaned = clean_data(data)

    save_data(cleaned, "data/cleaned.jsonl")

    print(f"Cleaned samples: {len(cleaned)}")